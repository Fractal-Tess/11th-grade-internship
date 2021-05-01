from modules.motion_classifier import SingleMotionDetector
from threading import Thread
from cv2 import rectangle, imencode
from time import sleep


class MotionDetector(object):
    def __init__(self, fl, lock, fps=None, accumWeight=0.5):
        # Reference to lock > I'm not sure if I am doing this correctly
        self.lock = lock
        # Reference to the FrameLoop object (instance)
        self.fl_ref = fl
        # The target fps
        self.target_fps = fps if fps else fl.fps
        
        # The current frame of the FrameLoop
        self.frame = None
        # The current frame of the FrameLoop (.jpg encoded)
        self.encodedFrame = None
        
        # Total number of frames so far
        self.total_frames = 0
        # A motion detection object instance (classifier)
        self.md = SingleMotionDetector(accumWeight)

    def detect_motion(self):
        while True:
            if self.total_frames > self.target_fps:
                # Get the lock
                with self.lock:
                    # Run the motion detection
                    motion = self.md.detect(self.fl_ref.grey_frame)
                    # Create a copy of the current frame from the running frame loop
                    self.frame = self.fl_ref.frame.copy()
                    
                # Check if there is motion                
                if motion:
                    # Unpack the tuple and draw the box around the motion area
                    (_, (minX, minY, maxX, maxY)) = motion
                    rectangle(self.frame, (minX, minY), 
                              (maxX, maxY), (0, 0, 255), 2)
            
            # Update the background
            self.md.update(self.fl_ref.grey_frame)
            self.total_frames +=1
            
            # Sleep until the time for the next frame
            sleep(1/self.target_fps)
            
    def encoding_generator(self):
        while True:
            # Grab the lock
            with self.lock:
                # Encode the frame into the `encodedFrame` variable
                (flag, self.encodedFrame) = imencode(".jpg", self.frame)
                
            # Check if encoding was successful
            if flag:
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                        bytearray(self.encodedFrame) + b'\r\n')
                
            # Else just skip
            else:
                print("Error encoding to .jpg ~(detect_motion)")
                continue

    def start(self):
        # Run the detect motion in another thread
        self.t = Thread(target=self.detect_motion)
        self.t.daemon = True
        self.t.start()
