from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer)
    idPaciente = db.Column(db.Integer)
    idMedico = db.Column(db.Integer)
    fecha = db.Column(db.String[20])
    sede = db.Column(db.String[100])
    descripcion = db.Column(db.String[100])


class CitaSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Cita
         include_relationships = True
         load_instance = True