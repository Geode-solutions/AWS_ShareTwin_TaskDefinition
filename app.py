''' Packages '''
import os

import flask
import flask_cors


''' Global config '''
app = flask.Flask(__name__)

def kill():
    if not os.path.exists(LOCK_FOLDER):
        os.mkdir(LOCK_FOLDER)
    if len(os.listdir(LOCK_FOLDER)) == 0:
        os._exit(0)
    if os.path.isfile(LOCK_FOLDER + '/ping.txt'):
        os.remove(LOCK_FOLDER + '/ping.txt')

''' Config variables '''
FLASK_ENV = os.environ.get('FLASK_ENV', default=None)

if FLASK_ENV == "production" or FLASK_ENV == "test":
    app.config.from_object('config.ProdConfig')
else:
    app.config.from_object('config.DevConfig')

ID = app.config.get('ID')
PORT = int(app.config.get('PORT'))
CORS_HEADERS = app.config.get('CORS_HEADERS')
UPLOAD_FOLDER = app.config.get('UPLOAD_FOLDER')
LOCK_FOLDER = app.config.get('LOCK_FOLDER')
DEBUG = app.config.get('DEBUG')
TESTING = app.config.get('TESTING')
ORIGINS = app.config.get('ORIGINS')
SSL = app.config.get('SSL')

flask_cors.CORS(app, origins=ORIGINS)

# For development
@app.route('/', methods=['GET'])
def root():
    return flask.make_response({"message": "root"}, 200)

# ''' Main '''
if __name__ == '__main__':
    print('Python is running in ' + FLASK_ENV + ' mode')
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT, ssl_context=SSL)
