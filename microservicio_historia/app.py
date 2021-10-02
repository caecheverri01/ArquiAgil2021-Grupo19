from microservicio_historia import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .modelo import db
from .vista import VistaHistoria
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
jwt = JWTManager(app)
cors = CORS(app)
api = Api(app)

api.add_resource(VistaHistoria, '/historia/<int:id_historia>')