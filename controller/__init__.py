from flask import Blueprint, Flask
from flask_restplus import Api


from controller.userController import api as user
from controller.chatController import api as chat


app = Flask(__name__)
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='SIMPLE CHAT API RAKAMIN-TEST Documentation',
          version='1.0',
          description='SIMPLE CHAT API RAKAMIN-TEST Documentation')

api.add_namespace(user, '/user')
api.add_namespace(chat, '/chat')

app.register_blueprint(blueprint)
