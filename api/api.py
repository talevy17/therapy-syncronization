
import os
from flask import Flask, request, redirect, url_for, send_from_directory, current_app
from flask_cors import CORS
from werkzeug.utils import secure_filename
from algorithms.main import controller, TMP_PARAMS

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'xlsb', 'xlsm', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return filename


@app.route('/lsm-table/<filename>', methods=['GET'])
def lsm_table(filename):
    file_name = controller(filename, TMP_PARAMS, table=True, lsm=True)
    return redirect(url_for('download', filename=file_name))


@app.route('/coor-table/<filename>', methods=['GET'])
def coor_table(filename):
    file_name = controller(filename, TMP_PARAMS, table=True, lsm=False)
    return redirect(url_for('download', filename=file_name))


@app.route('/coor-graph/<filename>', methods=['GET'])
def coor_graph(filename):
    file_name = controller(filename, TMP_PARAMS, graph=True, lsm=False)
    return redirect(url_for('download', filename=file_name))


@app.route('/lsm-graph/<filename>', methods=['GET'])
def lsm_graph(filename):
    file_name = controller(filename, TMP_PARAMS, graph=True, lsm=True)
    return redirect(url_for('download', filename=file_name))


@app.route('/files/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = os.path.abspath(os.path.join(current_app.root_path, os.pardir))
    return send_from_directory(directory=os.path.join(path, app.config['UPLOAD_FOLDER']), filename=filename, as_attachment=True)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

CORS(app, expose_headers='Authorization')