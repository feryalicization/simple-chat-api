from flask import jsonify, request
from flask_restplus import Namespace, Resource
from service.chatService import Create, chat_list_user, list_conversation
from service.userService import token_required
import jwt



api = Namespace('Chat API')

auth_header = {'token': {'name': 'token',
                           'in': 'header',
                           'type': 'string',
                           'description': 'Token JWT!'}}




secrets = 'secretindependent'

def token_required_jwt(token):
    try:
        payload = jwt.decode(token, secrets)
        if not payload['id']:
            return None
    except:
        payload = None
    return payload

    
@api.route('/create')
@api.doc(params=auth_header)
class CreateChatController(Resource):
    @staticmethod
    def post():
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        param = request.json

        data = Create(param, user_id)
        return data
        




    
@api.route('/list-chat-user')
@api.doc(params=auth_header)
class CreateChatController(Resource):
    @staticmethod
    def get():
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        data = chat_list_user(user_id)
        return data





    
@api.route('/list-conversation/<int:receiverId>')
@api.doc(params=auth_header)
class ListConversationController(Resource):
    @staticmethod
    def get(receiverId):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        data = list_conversation(user_id, receiverId)
        return data