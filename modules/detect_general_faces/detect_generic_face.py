from threading import Thread
from cv2 import rectangle, imencode, CascadeClassifier, data
from time import sleep

class GenericFaceDetection(object):
    def __init__(self, fl, lock, fps=25):
        # Reference to lock > I'm not sure if I am doing this correctly
        self.lock = lock
        # Reference to the FrameLoop object (instance)
        self.fl_ref = fl
        # The target fps
        self.target_fps = fps
        
        # The current frame of the FrameLoop
        self.frame = None
        # The current frame of the FrameLoop (.jpg encoded)
        self.encodedFrame = None
        
        # Classifier reference
        self.face_cascade = CascadeClassifier(data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def detect_generic_face(self):
        while True:
            # Grab the lock
            with self.lock:
                # Make a copy of the frame loop's current frame 
                self.frame = self.fl_ref.frame.copy()
            
            # Try to detect faces in the current
            faces = self.face_cascade.detectMultiScale(self.frame, 1.35, 5)
            
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                rectangle(self.frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Sleep until the time for the next frame
            sleep(1/self.target_fps)

    def encoding_generator(self):
        while True:
            # Grab the lock
            with self.lock:
                # Encode the frame into the `encodedImage` variable
                (flag, self.encodedImage) = imencode(".jpg", self.frame)
                
            # Check if encoding was successful
            if flag:
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                        bytearray(self.encodedImage) + b'\r\n')
                
            # Else just skip
            else:
                print("Error encoding to .jpg ~(detect_generic_face)")
                continue

    def start(self):
        # Run the generic face detection in another thread
        self.t = Thread(target=self.detect_generic_face)
        self.t.daemon = True
        self.t.start()