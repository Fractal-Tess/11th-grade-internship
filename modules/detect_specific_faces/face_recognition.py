from face_recognition import face_locations, face_encodings, compare_faces, load_image_file
from cv2 import imencode, putText , FONT_HERSHEY_SIMPLEX, rectangle, FILLED, resize
import os
from threading import Thread
from time import sleep, time


class FaceRecognition:
    def __init__(self, fl, lock, face_dir, tolerance, compression=4, debugging:bool=False):
        # Reference to the FrameLoop object (instance)
        self.fl_ref = fl
        # Reference to lock > I'm not sure if I am doing this correctly
        self.lock = lock
        # The target fps
        self.one_frame = 1/fl.fps
        # Compression on each frame in order to make it go faster
        self.compresion = compression
        self.debugging = debugging
        
        
        # The current frame of the FrameLoop < Later on encoded and drawn on.
        self.frame = None
        self.mini_frame = None
        # The current frame of the FrameLoop (.jpg encoded)
        self.encodedFrame = None
        # Total number of frames so far
        self.total_frames = 0
        
        # Was going to use the "cnn" model
        # But opted not to ~ It's insanely slow on the cpu 
        # self.model = "cnn"
        
        self.know_faces, self.known_names = FaceRecognition.encodeBaseImages(face_dir)
        self.tolerance = tolerance
        self.frame_tickness = 3
        self.font = FONT_HERSHEY_SIMPLEX
        self.font_size = 0.5
        self.text_offset = 15
        self.text_color = (200, 200, 200)
        self.color = (255, 0, 0)
        

        # Kill me now
        self.can_yield = False
        
    def detect(self):
        while True:
            start_time = time()

            with self.lock:
                if self.fl_ref.frame is None:
                    sleep(1)
                    continue
                else:
                    self.frame = self.fl_ref.frame.copy()
                    # self.frame = cvtColor(self.fl_ref.frame, COLOR_RGB2BGR)
                    
            self.mini_frame = resize(self.frame, (0, 0), 
                                 fx=1/self.compresion, fy=1/self.compresion)
            self.mini_frame = self.mini_frame[:, :, ::-1]
            locations =face_locations(self.mini_frame)
            encoding = face_encodings(self.mini_frame, locations)
            
            
            for face_encoding, (top, right, bottom, left) in zip (encoding, locations):
                # Revert the locations to their original pos from the compresion
                top *= self.compresion
                right *= self.compresion
                bottom *= self.compresion
                left *= self.compresion
                
                result = compare_faces(self.know_faces, face_encoding, self.tolerance)
                match = None
                if True in result:
                    match = self.known_names[result.index(True)]
                    
                    # Draw around the face
                    rectangle(self.frame, (left, top), (right, bottom),
                              self.color, self.frame_tickness)
                    
                    # top_left = (face_location[3], face_location[2])
                    # bottom_right = (face_location[1], face_location[2]+22)
                    rectangle(self.frame,(left, bottom - 20), (right, bottom), self.color, FILLED)
                    putText(self.frame, match, (left + 6, bottom - 6),
                            self.font, self.font_size, self.text_color)

            # What is this abomination here? 
            # I don't understand why i need to use this in order not to cause flickering 
            # In the encoding generator
            self.can_yield = True
            
            time_for_this_iteration = time() - start_time 
            if (time_for_this_iteration < self.one_frame):
                sleep(self.one_frame - time_for_this_iteration)

            # Debugging
            if self.debugging:
                print(time_for_this_iteration)

            

    def encoding_generator(self):
        while True:
            # Grab the lock
            with self.lock:
                # Encode the frame into the `encodedFrame` variable
                (flag, self.encodedFrame) = imencode(".jpg", self.frame)
                
            # Check if encoding was successful
            if flag:
                if self.can_yield:
                    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                            bytearray(self.encodedFrame) + b'\r\n')
                    self.can_yield = False
                else:
                    sleep(self.one_frame)
                    continue
                
            # Else just skip
            else:
                print("Error encoding to .jpg ~(detect_motion)")
                continue

    @classmethod
    def encodeBaseImages(cls, path):
        # Init 2 empty placeholding lists
        known_faces = []
        known_names = []
        
        # Combine the path
        face_path = os.path.join(os.getcwd(), path)
        
        # Loop over all the files
        for filename in os.listdir(face_path):
            # Load & encode the image files
            image = load_image_file(f"{face_path}/{filename}")
            encoding = face_encodings(image)[0]
            
            # Append them to the placeholding lists
            known_faces.append(encoding)
            # [0:-4] to remove the '.jpg' or '.png' at the end of the files
            known_names.append(filename[0:-4])
        return known_faces, known_names
    
    
    def start(self):
        self.t = Thread(target=self.detect)
        self.t.daemon = True
        self.t.start()
        