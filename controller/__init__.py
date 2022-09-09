from flask import Blueprint, Flask
from flask_restplus import Api


from controller.testController import api as test


app = Flask(__name__)
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='SIMPLE CHAT API RAKAMIN-TEST Documentation',
          version='1.0',
          description='SIMPLE CHAT API RAKAMIN-TEST Documentation')

api.add_namespace(test, '/test')

app.register_blueprint(blueprint)
