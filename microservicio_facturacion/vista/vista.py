from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..modelo import db, Facturacion, FacturacionSchema 

facturacion_schema = FacturacionSchema()

class VistaFacturacion(Resource):

    @jwt_required()
    def get(self, id_factura):
        return {'mensaje':'Respuesta servicio facturacion OK para ID: ' + str(id_factura)}, 200 