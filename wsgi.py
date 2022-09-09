from flask import Flask, request
from config import Config
from controller import blueprint
from entity import db
from flask_cors import CORS
import logging

application = Flask(__name__, static_url_path='/static')
application.config.from_object(Config)
db.init_app(application)
application.register_blueprint(blueprint)
CORS(application, resources={r"/*": {"origins": "*"}})



@application.before_request
def fix_transfer_encoding():
    """
    Sets the "wsgi.input_terminated" environment flag, thus enabling
    Werkzeug to pass chunked requests as streams.  The gunicorn server
    should set this, but it's not yet been implemented.
    """

    transfer_encoding = request.headers.get("Transfer-Encoding", None)
    if transfer_encoding == u"chunked":
        request.environ["wsgi.input_terminated"] = True


@application.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    # application.run(port=8080)


    application.run(host='0.0.0.0', debug=True)