from flask import Flask, render_template, url_for

app = Flask(__name__)

#Configs
PORT = 5000
HOST = "0.0.0.0"



@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route('/openCV-stream')
def openCV_stream():
    return render_template("opencv_stream.html", title="OpenCV Stream")


@app.route('/frontend-face-api')
def face_api():
    return render_template("faceapi.html", title="Index")

if __name__ == '__main__':
    app.run(debug=True, port=PORT, host=HOST)
    