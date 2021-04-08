from flask import Flask, render_template, url_for

app = Flask(__name__)

#Configs
PORT = 5000
HOST = "0.0.0.0"

@app.route('/')
def index():
    return render_template("index.html", title="Index")

if __name__ == '__main__':
    app.run(debug=True, port=PORT, host=HOST)
    