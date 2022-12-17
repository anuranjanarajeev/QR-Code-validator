from flask import Flask, flash, request, redirect, url_for, render_template
from pyzbar.pyzbar import decode
from PIL import Image
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = 'static/files'


def DecodeQRCode(qrcodeimg):  # pass path of img
    decocdeQR1 = decode(Image.open(qrcodeimg))
    print("VALID QR CODE")
    print(decocdeQR1[0].data.decode('ascii'))

    decocdeQR2 = decode(Image.open(qrcodeimg))
    if (decocdeQR2):
        a = "VALID QR CODE"
        # data=decocdeQR2[0].data.decode('ascii')
    else:
        a = "INVALID QR CODE"
    return a


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/login')
def upload_files():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                  app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
        return "Image has been uploaded."
    return render_template('login2.html', form=form)


"""@app.route('/login')
def login():
    if request.method == 'POST':
        qrcodeimg = request.form['qrcodeimg']
        a = request.form['inputGroupFile02']
        result = DecodeQRCode(a)
    return render_template("login.html",)"""


if __name__ == "__main__":
    app.run(debug=True)
