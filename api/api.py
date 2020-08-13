
import os
from flask import Flask, request, redirect, url_for, send_from_directory, current_app
from flask_cors import CORS
from werkzeug.utils import secure_filename
from algorithms.main import controller, TMP_PARAMS

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'xlsb', 'xlsm', 'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_params(args):
    event_speaker = args.get("eventSpeaker")
    measures = args.get("measures")
    transcription = args.get("transcription")
    dyad = args.get("dyad")
    speakers = args.get("speakers")
    params = {'dyad': dyad if dyad else TMP_PARAMS['dyad'],
              'transcription': transcription if transcription else TMP_PARAMS['transcription'],
              'speakers': speakers.split(',') if (speakers and len(speakers) != 0) else TMP_PARAMS['speakers'],
              'num_of_words': 'num_of_words'}
    if measures:
        if len(measures) == 0:
            measures = None
        else:
            measures = measures.split(',')
    return params, measures, event_speaker

@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return filename


@app.route('/lsm-table/<filename>', methods=['GET'])
def lsm_table(filename):
    params, measures, event_speaker = get_params(request.args)
    file_name = controller(filename, params, measures, table=True, lsm=True)
    return redirect(url_for('download', filename=file_name))


@app.route('/coor-table/<filename>', methods=['GET'])
def coor_table(filename):
    file_name = controller(filename, TMP_PARAMS, table=True, lsm=False)
    return redirect(url_for('download', filename=file_name))


@app.route('/coor-graph/<filename>', methods=['GET'])
def coor_graph(filename):
    file_name = controller(filename, TMP_PARAMS, graphs=True, lsm=False)
    return redirect(url_for('download', filename=file_name))


@app.route('/lsm-graph/<filename>', methods=['GET'])
def lsm_graph(filename):
    file_name = controller(filename, TMP_PARAMS, graphs=True, lsm=True)
    return redirect(url_for('download', filename=file_name))


@app.route('/files/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = os.path.abspath(os.path.join(current_app.root_path, os.pardir))
    return send_from_directory(directory=os.path.join(path, app.config['UPLOAD_FOLDER']), filename=filename, as_attachment=True)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

CORS(app, expose_headers='Authorization')
