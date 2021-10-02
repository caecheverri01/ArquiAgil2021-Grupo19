from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

usuario_schema = UsuarioSchema()

class VistaLogIn(Resource):

    def post(self):
            u_nombre = request.json["nombre"]
            u_contrasena = request.json["contrasena"]
            usuario = Usuario.query.filter_by(nombre=u_nombre, contrasena = u_contrasena).first()
            if usuario:
                if usuario.bloqueo !=1:
                    token_de_acceso = create_access_token(identity = usuario.nombre)
                    return {"mensaje":"Inicio de sesión exitoso", "token": token_de_acceso}
                else:
                    return {'mensaje':'Usuario Bloqueado'}, 401    
            else:
                return {'mensaje':'Nombre de usuario o contraseña incorrectos'}, 401

class VistaSignIn(Resource):
    
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"], contrasena=request.json["contrasena"])
        token_de_acceso = create_access_token(identity=request.json['nombre'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {'Mensaje':'Usuario creado exitosamente','token de acceso': token_de_acceso},201

    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Usuario Eliminado',410

class VistaBloqueo(Resource):

    def put(self, id_usuario):
        #bloqueo = Usuario(bloqueo=request.json["bloqueo"])
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.bloqueo =  True 
         #request.json.get("bloqueo",usuario.bloqueo)
        db.session.commit()
        return {'Mensaje':'Bloqueado', 'Usuario':usuario.nombre},401
        

    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return usuario_schema.dump(usuario)


