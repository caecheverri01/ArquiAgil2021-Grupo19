from flask_restful import Resource
from flask import request 
import random
from ..modelo import db, Cita, CitaSchema 
from tarea_cola import registrar_evento

cita_schema = CitaSchema()

class VistaCita(Resource):

    def get(self, id_cita):
        cita = Cita.query.filter(Cita.id == id_cita).first()
        db.session.commit()

        al1 = random.randrange(1, 1000, 1)
        al2 = random.randrange(900, 1200, 1)
        
        def es_primo(nro):
            for n in range(2, nro):
                if nro % n == 0:
                    return False
            return True

        if es_primo(al1):
            registrar_evento.delay("srv_cita_001|501|"+str(al2))
        else:
            registrar_evento.delay("srv_cita_001|200|"+str(al2))

        if cita is None:
            return {'mensaje':'La cita no existe'}, 400 
        else:            
            return cita_schema.dump(cita.query.get_or_404(id_cita))