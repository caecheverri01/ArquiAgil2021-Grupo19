from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db = SQLAlchemy()

class FormaPago(enum.Enum):
    Efectivo = 1
    TarjetaDebito = 2
    TarjetaCredito = 3
    Cheque = 4
    Tranferencia = 5

class Facturacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer)
    fecha = db.Column(db.String[20])
    valorTotal = db.Column(db.Integer)
    formaPago  =db.Column(db.Enum(FormaPago))
    estado = db.Column(db.String[20])
    descripcion = db.Column(db.String[100])
    consecutivo  = db.Column(db.Integer)


class FacturacionSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Facturacion
         include_relationships = True
         load_instance = True