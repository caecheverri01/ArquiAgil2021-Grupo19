from flask_restful import Resource
from flask import request 
from flask import random
from ..modelo import db, Cita, CitaSchema 
from ..tareas import registrar_evento

cita_schema = CitaSchema()

class VistaCita(Resource):

    def get(self, id_cita):
        cita = cita.query.filter(cita.id == id_cita).first()
        db.session.commit()

        al1 = random.randrange(1, 1000, 1)
        al2 = random.randrange(900, 1200, 25)
        c = 0

        def es_primo(nro):
            for n in range(2, nro):
                if nro % n == 0:
                    return False
            return True

        while c < 25:
            if es_primo(al1):
                registrar_evento.delay("srv_cita_001|501|"+str(al2))
            else:
                registrar_evento.delay("srv_cita_001|200|"+str(al2))
            time.sleep(5)
            c += 1

        if cita is None:
            return {'mensaje':'La cita no existe'}, 400 
        else:            
            return cita_schema.dump(cita.query.get_or_404(id_cita))