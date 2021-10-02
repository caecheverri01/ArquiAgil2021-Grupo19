from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..modelo import db, Historia, HistoriaSchema 

historia_schema = HistoriaSchema()

class VistaHistoria(Resource):

    @jwt_required()
    def get(self, id_historia):
        historia = Historia.query.filter(Historia.id == id_historia).first()
        db.session.commit()

        if historia is None:
            return {'mensaje':'La historia no existe'}, 400 
        else:            
            return historia_schema.dump(historia.query.get_or_404(id_historia))