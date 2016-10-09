from flask import Flask
from fabric.tasks import execute
import fabfile

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Navigate to /start to start the pipeline. Navigate to /abort to stop the pipeline."

@app.route('/start')
def start():
    execute(getattr(fabfile, 'start'))
    return "Success, check your inbox!"

@app.route('/abort')
def abort():
    # TODO: Add code that aborts previous process
    return "Abort!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
