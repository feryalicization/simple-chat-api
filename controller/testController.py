from flask import jsonify
from flask_restplus import Namespace, Resource
from service.testService import List



api = Namespace('Test API')





@api.route('/list')
class ListCountryController(Resource):
    @staticmethod
    def get():
        data = List()

        if data:
            return jsonify(
                {'code': '1', 'msg': 'Get Data Successfull!', 'data':data})

        return jsonify(
            {'code': '0', 'msg': 'Data Not Found!', 'data': []})