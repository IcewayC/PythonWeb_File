from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('file')
    filename = secure_filename(file.filename)
    path = r'F:\Programming\Python\txt\static\files\%s' % filename
    file.save(path)
    return render_template('file.html', path='static/files/%s' % filename)

if __name__ == '__main__':
    app.run()
