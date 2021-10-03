from flask_restful import Resource
from flask import request
from ..controlador import validar_token, validar_permisos, valida_bloqueo_usuario

class VistaAutorizaUsuarios(Resource):

    def get(self):
        servicio = validar_permisos(request.args.get('usuario', None), request.args.get('recurso', None), request.args.get('operacion', None))
        valida_bloqueo_usuario(request.args.get('usuario', None))
        
        if servicio == 200:
            return 'Autorizado', 200
        else:
            return 'Unauthorized', 401

class VistaValidaToken(Resource):

    def post(self):
        servicio = validar_token(request.args.get('usuario', None), request.args.get('recurso', None), request.args.get('operacion', None))
        
        if servicio == 200:
            return 'Autorizado', 200
        else:
            return 'Unauthorized', 401