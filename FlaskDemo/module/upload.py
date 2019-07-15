import config
from module import os, app, Result, objToDict, isAllowedFile
from flask import request, json, jsonify
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print('Root : ' + config.ROOT_DIR)
    results = []
    if request is not None:
        if request.method == 'POST':
            images = request.files.getlist("image[]")
            if not images:
                return "{}"
            else:
                for image in images:
                    print('info [file ' + image.filename +
                          ', ' + image.name + ']')
                    if image and isAllowedFile(image.filename):
                        filename = secure_filename(image.filename)
                        image.save(os.path.join(
                            config.UPLOAD_FOLDER, filename))
                        results.append(Result(filename))
        return json.dumps(results, default=objToDict)
