from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request
import requests
from ..controlador import solicitar_validacion_acceso

class VistasFacturacion(Resource):

    @jwt_required()
    def get(self, id_factura):
        token = request.headers.get('Authorization')
        status = solicitar_validacion_acceso(token, 'facturacion', 'get')

        if status == 200:
            return requests.get(url='http://127.0.0.1:5003/facturacion/' + str(id_factura), headers={'Authorization': token}).json()
        else:
            return 'Unauthorized', 401

class VistasHistoriaClinica(Resource):
    def get(self):
        print("hola mundo get HC")

    def post(self):
        print("hola mundo post HC")

class VistasAutenticador(Resource):
    def post(self):
        resp = requests.post(url='http://127.0.0.1:5001/login', json = request.json)
        return resp.json()