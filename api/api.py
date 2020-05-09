
import os
from flask import Flask, request, redirect, url_for, send_from_directory, current_app
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'xlsb', 'xlsm', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    # process data and send

    return redirect(url_for('download', filename=filename))


@app.route('/files/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = os.path.abspath(os.path.join(current_app.root_path, os.pardir))
    return send_from_directory(directory=os.path.join(path, app.config['UPLOAD_FOLDER']), filename=filename, as_attachment=True)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

CORS(app, expose_headers='Authorization')
