from flask_restful import Resource
from flask import request
from ..modelos import logLogin, db
from ..controlador import validar_token, validar_usuarios_autorizados

class VistaAutorizaUsuarios(Resource):

    def get(self):
        print(request.args.get('usuario', None), request.args.get('recurso', None), request.args.get('operacion', None))
        servicio = validar_usuarios_autorizados(request.args.get('usuario', None), request.args.get('recurso', None), request.args.get('operacion', None))
        
        if servicio == 200:
            return 'Autorizado', 200
        else:
            return 'Unauthorized', 401

class VistaValidaToken(Resource):

    def post(self):
        u_usuario = request.json["usuario"]
        u_recurso = request.json["recurso"]
        u_operacion = request.json["operacion"]
        servicio = validar_token(u_usuario, u_recurso, u_operacion)
        
        if servicio == 200:
            return 'Autorizado', 200
        else:
            return 'Unauthorized', 401