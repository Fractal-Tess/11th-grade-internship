# from imutils import resize            # < Not used anymore
from imutils.video import VideoStream
from cv2 import cvtColor, COLOR_BGR2GRAY, GaussianBlur
from threading import Thread
from time import sleep


class FrameLoop(object):
    def __init__(self, fps, lock, width=320, height=200):
        self.frame = None
        self.grey_frame = None
        self.fps = fps
        self.vs =  VideoStream(src=0, framerate=self.fps,
                              resolution=(height, width))
        self.lock = lock
        
    def loop(self):
        while True:
            with self.lock:
                # Read the frame
                self.frame = self.vs.read()
                
                # self.frame = resize(self.frame, width=1080) # < Not used anymore

                #Convert it to greyscale
                self.grey_frame = cvtColor(self.frame, COLOR_BGR2GRAY)
                self.grey_frame = GaussianBlur(self.grey_frame, (7, 7), 0)
                
            # Sleep the thread until the time for the next frame comes
            sleep(1/self.fps)
            
    def start(self):
        # Create a new thread
        self.t = Thread(target=self.loop)
        self.t.daemon = True

        # Start the video stream on camera 0
        self.vs.start()
        
        # Start the thread
        self.t.start()