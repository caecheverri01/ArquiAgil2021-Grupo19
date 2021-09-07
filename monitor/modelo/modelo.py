from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EjecucionServicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servicio = db.Column(db.String[128])
    respuesta = db.Column(db.String[10])
    tiempo = db.Column(db.Integer)