from flask import Flask, render_template, Response
from modules.detect_motion import MotionDetector
from modules.frame_loop import FrameLoop
from modules.detect_general_faces import GenericFaceDetection
from threading import Lock

app = Flask(__name__)

#Configs
PORT = 5000
HOST = "0.0.0.0"
lock = Lock()
fps = 60

# Start capturing and processing stock frames into normal and greyscale
fl = FrameLoop(fps=fps, lock=lock)
fl.start()

md = MotionDetector(fl=fl, lock=lock, fps=fps, accumWeight=0.5)
md.start()

fd = GenericFaceDetection(fl=fl, lock=lock, fps=fps)
fd.start()


@app.route("/motion_detection_vs")
def motion_detection_vs():
	    return Response(md.encoding_generator(),
		    mimetype = "multipart/x-mixed-replace; boundary=frame")


@app.route("/generic_face_detection_vs")
def generic_face_detection_vs():
	return Response(fd.encoding_generator(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

# Routes
@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route('/motion-detection')
def motion_detection():
    return render_template("motion_detection.html", title="OpenCV Motion Detection")

@app.route('/generic-face-detection')
def face_detection():
    return render_template("generic_face_detection.html", title="OpenCV Generic Face detection")
    
@app.route('/frontend-face-api')
def face_api():
    return render_template("faceapi.html", title="Index")


if __name__ == '__main__':
    
	# start the flask app
	# app.run(host=args["ip"], port=args["port"], debug=True,
	# 	threaded=True, use_reloader=False)
	app.run(host=HOST, port=PORT, debug=True,
		threaded=True, use_reloader=False)

# release the video stream pointer
fl.vs.stop()