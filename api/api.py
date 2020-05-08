
import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xlsx', 'xlsb', 'xlsm', 'xls'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def file_upload():
    target = os.path.join(UPLOAD_FOLDER, 'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    # session['uploadFilePath'] = destination
    response = "Whatever you wish too return"
    return response


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
