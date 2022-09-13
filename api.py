# the api should be able to take a photo from the user and send it to the model and then recieve the response from the model with 1(wearing a mask) or 0(not wearing a mask) and then send it back to the user as a string output
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from dbconnection import *
from predicting import *
from dbconnection import ConnectDb
from datalocaltransfer import *
database = ConnectDb(key = "firebase-certifications/key.json", dburl = "https://face-mask-detection-171299-default-rtdb.firebaseio.com/")

app = Flask(__name__, template_folder = './templates')
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators = [InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        status = is_masked(path = file_path)
        filename = secure_filename(file.filename)
        database.upload_report(ref = filename, file = file_path, status = status)
        transfer_data_to_local(filename, status, )
        return f"File '{filename}' has been uploaded.\nThe person in the image is {status}"
    
    return render_template('index.html', form = form)


@app.route("/reciever", methods = ['POST', 'GET'])
def reciever():
    # take the file (image) from the user and send it to the model to recognize if it with_mask or without_mask
    pass


@app.route("/response", methods = ['POST', 'GET'])
def response():
    # take the resonse from the modle and send it back to the user with values "with_mask" or "without_mask"
    pass

if __name__ == '__main__':
    app.run(debug = True)
    