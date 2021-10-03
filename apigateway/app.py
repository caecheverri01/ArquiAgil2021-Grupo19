from flask_restful import Api
from flask_cors import CORS
from apigateway import create_app
from flask_jwt_extended import JWTManager
from .vista import VistasAutenticador, VistasFacturacion, VistasHistoriaClinica

app = create_app('default')
app_context = app.app_context()
app_context.push()

cors = CORS(app)
jwt = JWTManager(app)
api = Api(app)

api.add_resource(VistasAutenticador, '/login')
api.add_resource(VistasFacturacion, '/facturacion/<int:id_factura>')
api.add_resource(VistasHistoriaClinica, '/historia/<int:id_historia>')