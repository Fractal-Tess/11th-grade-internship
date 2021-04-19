from flask import Flask, render_template, url_for, Response
from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from classes import Frame
import threading
import datetime
import imutils
import cv2

app = Flask(__name__)

#Configs
PORT = 5000
HOST = "0.0.0.0"
FPS = 24


# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)


motion_frame_object = Frame()
face_frame_object = Frame()

lock = threading.Lock()

# initialize the video stream and allow the camera sensor too
vs = VideoStream(src=0).start()

def detect_motion(frameCount):
    # grab global references to the video stream, output frame, and lock
	global vs, lock

	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

	# initialize the motion detector and the total number of frames read thus far
	md = SingleMotionDetector(accumWeight=0.3)
	total = 0

	# loop over frames from the video stream
	while True:
    		
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		frame = imutils.resize(frame, width=1080)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		# grab the current timestamp and draw it on the frame
		timestamp = datetime.datetime.now()
		cv2.putText(frame, timestamp.strftime(
			"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
		if total > frameCount:
			motion_frame = frame.copy()
			face_frame = frame.copy()

			# Detect motion
			motion = md.detect(gray)
			if motion:
			# 	# unpack the tuple and draw the box surrounding the
			# "motion area" on the output frame
				(thresh, (minX, minY, maxX, maxY)) = motion
				cv2.rectangle(motion_frame, (minX, minY), (maxX, maxY),
					(0, 0, 255), 2)

			faces = face_cascade.detectMultiScale(gray, 1.1, 4)
			# Draw the rectangle around each face
			for (x, y, w, h) in faces:
				cv2.rectangle(face_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


			# acquire the lock, set the output frame, and release the lock
			with lock:
				motion_frame_object.current_frame = motion_frame
				face_frame_object.current_frame = face_frame
		
		# update the background model and increment the total number
		# of frames read thus far
		md.update(gray)
		total += 1


def generate(frameObject):
    # grab global references to the output frame and lock variables
	global lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if frameObject.current_frame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", frameObject.current_frame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')


@app.route("/motion-detection-vs")
def motion_detection_vs():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(frameObject=motion_frame_object),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route("/face-detection-vs")
def face_detection_vs():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(frameObject=face_frame_object),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

# Routes
@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route('/motion-detection')
def motion_detection():
    return render_template("motion_detection.html", title="OpenCV Motion Detection")

@app.route('/face-detection')
def face_detection():
    return render_template("face_detection.html", title="OpenCV Face Detection")
    
@app.route('/frontend-face-api')
def face_api():
    return render_template("faceapi.html", title="Index")


if __name__ == '__main__':
	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(FPS,))
	t.daemon = True
	t.start()

	# start the flask app
	# app.run(host=args["ip"], port=args["port"], debug=True,
	# 	threaded=True, use_reloader=False)
	app.run(host=HOST, port=PORT, debug=True,
		threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()