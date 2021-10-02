from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..modelo import db, Facturacion, FacturacionSchema 

facturacion_schema = FacturacionSchema()

class VistaFacturacion(Resource):

    @jwt_required()
    def get(self, id_factura):
        facturacion = Facturacion.query.filter(Facturacion.id == id_factura).first()
        db.session.commit()

        if facturacion is None:
            return {'mensaje':'La facturacion del paciente no existe'}, 400 
        else:            
            return facturacion_schema.dump(facturacion.query.get_or_404(id_factura))