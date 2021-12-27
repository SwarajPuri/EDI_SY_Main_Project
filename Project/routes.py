import os
from flask import Flask, render_template, request,flash,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
from Combined.main_project_file import image_encrypt ,image_decrypt
from Combined.Audio_Steganography_Ultrasonic_Embedded.Main_Ultrasonic import sound_encrypt , sound_decrypt
Flask_App = Flask(__name__) # Creating our Flask Instance

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'wav'}

Flask_App.secret_key = "abcdefgh"

Flask_App.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
plaintext='HelloWorld'

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """
    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['GET','POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None
    filename=''
    # request.form looks for:
    # html tags with matching "name= "
    if request.method == 'POST':
        card_number = request.form['card_number']
        Month = request.form['Month']
        Year = request.form['Year']
        CVV = request.form['CVV']
        global plaintext
        plaintext = str(card_number+Month + Year +CVV)

        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # f2=f
            file2 = request.files['file2']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '' and file2.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if (file and allowed_file(file.filename)) and (file2 and allowed_file(file2.filename)):
                filename = secure_filename(file.filename)
                filename2 = secure_filename(file2.filename)

                file.save(UPLOAD_FOLDER + '/' + filename)
                file = filename
                filename = UPLOAD_FOLDER + '/' + filename
                filename = image_encrypt(plaintext, filename)


                file2.save(UPLOAD_FOLDER + '/' + filename2)
                filename2 = UPLOAD_FOLDER + '/' + filename2
                audiofile = sound_encrypt(plaintext, filename2)


            return render_template("index.html", result=plaintext,name=filename,uploaded=True,audio=audiofile)

    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@Flask_App.route('/upload_file', methods=['GET', 'POST'])
def upload_file(): #from flask file upload
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        file2 = request.files['file2']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' and file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if (file and allowed_file(file.filename) and (file2 and allowed_file(file2.filename))):

            filename = secure_filename(file.filename)
            file.save(os.path.join(Flask_App.config['UPLOAD_FOLDER'], filename))

            filename2 = secure_filename(file2.filename)
            file.save(os.path.join(Flask_App.config['UPLOAD_FOLDER'], filename2))

            return redirect(url_for('download_file', img=filename, audio=filename2))
    return render_template('file_upload_from_flask_doc.html')

#working code:

@Flask_App.route('/upload_file1/<img> <audio>')
def download_file(img,audio):
    #file=static/img file2=static/audio
    return render_template('file_display.html',file=UPLOAD_FOLDER+'/'+img,file2=UPLOAD_FOLDER+'/'+audio)

#working code:
"""
@Flask_App.route('/upload_file1/<name>')
def download_file(name):
    #Flask_App.config["UPLOAD_FOLDER"] instad of this , you can write path directly for ex: 'static'
    return send_from_directory(Flask_App.config["UPLOAD_FOLDER"], name) 
"""

#working code
@Flask_App.route('/upload')
def upload():
    return render_template("upload.html")


@Flask_App.route('/success', methods=['POST'])
def success():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        #f2=f
        file2 = request.files['file2']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' and file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if (file and allowed_file(file.filename)) and (file2 and allowed_file(file2.filename)):

            filename = secure_filename(file.filename)
            filename2 = secure_filename(file2.filename)

            file.save(UPLOAD_FOLDER+'/'+filename)
            file = filename
            filename=UPLOAD_FOLDER+'/'+filename
            filename=image_encrypt(plaintext,filename)
            result=image_decrypt(filename)

            file2.save(UPLOAD_FOLDER + '/' + filename2)

            filename2=UPLOAD_FOLDER + '/' + filename2
            audiofile = sound_encrypt(plaintext,filename2)
            audio_text=sound_decrypt(audiofile)
            return render_template("upload.html", name=filename,image1=filename,uploaded=True,img=True,result=result,audio=True,audio_text=audio_text,
                                   audiofile=audiofile)


@Flask_App.route('/uploadAudio')
def uploadAudio():
    return render_template("audioupload.html")


@Flask_App.route('/audiosuccess', methods=['POST'])
def audiosuccess():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        f2=f
        #f2 = request.files['file2']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if f.filename == '' and f2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):

            filename = secure_filename(f.filename)
            f.save(UPLOAD_FOLDER + '/' + filename)
            file1=UPLOAD_FOLDER + '/' + filename
            plaintext='hello world1'

            audiofile = sound_encrypt(plaintext,file1)

            s=sound_decrypt(audiofile)

            return render_template("audioupload.html", name=audiofile,uploaded=True,result=s)

#decode route
@Flask_App.route('/decode', methods=['GET','POST'])
def decode():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            if(f.filename.split('.')[1]!='wav') :
                filename = secure_filename(f.filename)
                f.save(UPLOAD_FOLDER + '/' + filename)
                filename = UPLOAD_FOLDER + '/' + filename
                result=image_decrypt(filename)

                return render_template("decode.html", name=filename,decoded=result,uploaded=True,img=True)

            if (f.filename.split('.')[1] == 'wav'):
                filename = secure_filename(f.filename)
                f.save(UPLOAD_FOLDER + '/' + filename)
                audiofile=UPLOAD_FOLDER + '/' + filename
                result = sound_decrypt(audiofile)
                return render_template("decode.html", name=filename, decoded=result,audiofile=audiofile ,uploaded=True,audio=True)

    return render_template("decode.html")

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
