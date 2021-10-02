from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
   
class logAutorizaciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String[50])
    recurso = db.Column(db.String[20])
    operacion = db.Column(db.String[10])
    estaAutorizado = db.Column(db.Boolean)
