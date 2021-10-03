from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..modelo import db, Historia, HistoriaSchema 

historia_schema = HistoriaSchema()

class VistaHistoria(Resource):

    @jwt_required()
    def get(self, id_historia):
        return {'mensaje':'Respuesta servicio historia clinica OK para ID: ' + str(id_historia)}, 200 