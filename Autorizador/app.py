from Autorizador import create_app
from flask_restful import Api
from flask_cors import CORS
from .modelos import db
from .vistas import VistaAutorizaUsuarios, VistaValidaToken
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

CORS(app)
api = Api(app)

api.add_resource(VistaValidaToken, '/validatoken')
api.add_resource(VistaAutorizaUsuarios, '/autorizacion')

jwt = JWTManager(app)