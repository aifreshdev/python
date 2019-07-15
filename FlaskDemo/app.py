import config
from module import app, upload
from flask import url_for, render_template, jsonify

@app.route('/')
def index():
	return render_template('index.html', title="Flask Upload Demo")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=config.DEBUG)