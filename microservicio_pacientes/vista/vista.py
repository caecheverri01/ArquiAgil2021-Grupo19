from flask_restful import Resource
from flask import request
import random
from ..modelo import db, Paciente, PacienteSchema 
from ..tareas import registrar_evento

paciente_schema = PacienteSchema()

class VistaPaciente(Resource):

    def get(self, id_paciente):
        paciente = Paciente.query.filter(Paciente.id == id_paciente).first()
        db.session.commit()

        al1 = random.randrange(1, 2000, 1)
        al2 = random.randrange(1, 1200, 1)

        def es_primo(nro):
            for n in range(2, nro):
                if nro % n == 0:
                    return False
            return True

        if es_primo(al1):
            registrar_evento.delay("srv_paciente_001|200|"+str(al2))
        else:
            registrar_evento.delay("srv_paciente_001|501|"+str(al2))            

        if paciente is None:
            return {'mensaje':'El usuario no existe'}, 400 
        else:            
            return paciente_schema.dump(Paciente.query.get_or_404(id_paciente))

class VistaPacientes(Resource):

    def post(self):
        #realizamos las validaciones del caso
        paciente = Paciente.query.filter(Paciente.nombres == request.json["nombres"], Paciente.apellidos == request.json["apellidos"]).first()
        db.session.commit()
        if paciente is None:
            nuevo_paciente = Paciente(nombres=request.json["nombres"], apellidos=request.json["apellidos"], telefono=request.json["telefono"], email=request.json["email"])
            db.session.add(nuevo_paciente)
            db.session.commit()
            return paciente_schema.dump(nuevo_paciente)
        else:                
            return {'mensaje':'El Pacinete ya existe, no se puede crear de nuevo'}, 400 

         