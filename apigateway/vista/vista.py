from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request
import requests
from ..controlador import solicitar_validacion_acceso

class VistasFacturacion(Resource):

    @jwt_required()
    def get(self, id_factura):
        token = request.headers.get('Authorization')
        status = 200 #solicitar_validacion_acceso(token, 'facturacion', 'get')

        if status == 200:
            resp = requests.get(url='http://127.0.0.1:5003/facturacion/' + str(id_factura), headers={'Authorization': token})
            return resp.json(), resp.status_code
        else:
            return 'Unauthorized', 401

class VistasHistoriaClinica(Resource):

    @jwt_required()
    def get(self, id_historia):
        token = request.headers.get('Authorization')
        status = 200 #solicitar_validacion_acceso(token, 'historia', 'get')

        if status == 200:
            resp = requests.get(url='http://127.0.0.1:5002/historia/' + str(id_historia), headers={'Authorization': token})
            return resp.json(), resp.status_code
        else:
            return 'Unauthorized', 401

class VistasAutenticador(Resource):
    def post(self):
        resp = requests.post(url='http://127.0.0.1:5001/login', json = request.json)        
        return resp.json(), resp.status_code