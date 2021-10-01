from microservicio_facturacion import create_app
from flask_restful import Api
from .modelo import db
from .vista import VistaFacturacion
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)
api = Api(app)

api.add_resource(VistaFacturacion, '/facturacion/<int:id_factura>')