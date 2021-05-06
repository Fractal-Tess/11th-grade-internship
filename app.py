from os.path import commonpath
from flask import Flask, render_template, Response
from modules.detect_motion import MotionDetector
from modules.frame_loop import FrameLoop
from modules.detect_general_faces import GenericFaceDetection
from modules.detect_specific_faces import FaceRecognition
from threading import Lock



#Configs
app = Flask(__name__)
PORT = 5000
HOST = "0.0.0.0"
lock = Lock()
fps = 24
fr_tolerance = 0.6
compression = 4
# Relative path to a sub-folder containing .jpg face file(s) examples
path = "faces/"

####
# TODO: Add "cnn" model classifier (need gpu instancing)
###

# Start capturing and processing stock frames 
fl = FrameLoop(fps=fps, lock=lock, width=1080, height=1920)
fl.start()

md = MotionDetector(fl=fl, lock=lock, accumWeight=0.5)
md.start()

gfd = GenericFaceDetection(fl=fl, lock=lock)
gfd.start()

fr = FaceRecognition(fl=fl, lock=lock, face_dir=path, 
                     tolerance=fr_tolerance, compression=compression,
                     debugging=True)
fr.start()


# Next 3 @app.routes create a video streaming 
# URLs for the respective encoding functions of each detection method
@app.route("/motion_detection_vs")
def motion_detection_vs():
	    return Response(md.encoding_generator(),
		    mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route("/generic_face_detection_vs")
def generic_face_detection_vs():
	return Response(gfd.encoding_generator(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")
 
@app.route("/face_recognition_vs")
def face_recognition_vs():
	return Response(fr.encoding_generator(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")
 

# Create 4 basic routes for our website
@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route('/motion-detection')
def motion_detection():
    return render_template("motion_detection.html", title="OpenCV Motion Detection")

@app.route('/generic-face-detection')
def face_detection():
    return render_template("generic_face_detection.html", title="OpenCV Generic Face detection")
    

@app.route('/face-recognition')
def face_recognition():
    return render_template("face_recognition.html", title="OpenCV & face_recognition")


# This page's frontend code does not work ~ because the webcam is already taken by the backend server.
# If you wish to use this, simply comment out everything from line 27 to 57.
@app.route('/frontend-face-api')
def face_api():
    return render_template("faceapi.html", title="Frontend face-detection")
    
    
if __name__ == '__main__':
	app.run(host=HOST, port=PORT, threaded=True)

# Because it is threading, sometimes the video streaming pointer would not be released
# Do this to avoid crashes
with lock:
	fl.vs.stop()