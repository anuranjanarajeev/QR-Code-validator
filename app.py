from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
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
app.config['UPLOAD_FOLDER'] = 'sample/files'


def DecodeQRCode(qrcodeimg):  # pass path of img
    decocdeQR2 = decode(Image.open(qrcodeimg))
    if (decocdeQR2):
        a = "VALID QR CODE"
        # data=decocdeQR2[0].data.decode('ascii')
    else:
        a = "INVALID QR CODE"
    return a


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/upload', methods=['GET', "POST"])
def upload_files():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        s = file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
        filename = secure_filename(file.filename)
        userFile = "sample\\files\\"+filename
        result = DecodeQRCode(userFile)
        return render_template("upload.html", form=form, result=result)
    else:
        return render_template('upload.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
