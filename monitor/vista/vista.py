from flask_restful import Resource
from flask import request
from ..controlador import registrar_trama, main
import asyncio

class VistaMonitor(Resource):

    def post(self):
        trama = request.json["trama"]
        servicio = registrar_trama(trama)
        asyncio.run(main(servicio))

        return {'mensaje':'ok'}, 200
