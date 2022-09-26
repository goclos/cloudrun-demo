import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    simplePage = """
                '<title>helloRun</title>
                <center>
                <p><img src=/static/helloworld.jpeg width="640" alt="hackerman!"></p>
                <p></p>
                <p><img src=/static/qrcode-git.png width="300" alt="qrCode"></p>
                <p style="font-family:sans">https://github.com/goclos/cloudrun-demo</p>
                </center>'"""
    return simplePage
    #return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))