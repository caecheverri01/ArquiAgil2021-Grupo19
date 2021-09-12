from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String[150])
    apellidos = db.Column(db.String[150])
    telefono = db.Column(db.String[20])
    email = db.Column(db.String[100])

class PacienteSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Paciente
         include_relationships = True
         load_instance = True