__author__ = 'Silent Anonym'

import os,cv2
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from detect import detect
UPLOAD_FOLDER = 'static/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'input.jpg'))
        print str(filename)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'input.jpg')
        detect(filename)
        return redirect(url_for('display'))
    return render_template('index.html')

@app.route('/display')
def display():
	return render_template('display.html')

if __name__ == '__main__':
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True)