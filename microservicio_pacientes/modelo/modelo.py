from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String[150])
    apellidos = db.Column(db.String[150])
    telefono = db.Column(db.String[20])
    email = db.Column(db.String[100])