from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Historia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    IdCita = db.Column(db.Integer)
    idPaciente = db.Column(db.Integer)
    idMedico = db.Column(db.Integer)
    registro = db.Column(db.String[20])
    descripcion = db.Column(db.String[100])


class HistoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Historia
         include_relationships = True
         load_instance = True