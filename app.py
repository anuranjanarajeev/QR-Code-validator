from flask import Flask, render_template

app = Flask(__name__)
qrcodeData = "sdwajk"


@app.route('/')
def hello_world():
    return "Main page!"


@app.route('/login')
def login():
    return render_template("login.html", qrcodeData=qrcodeData)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
