from flask_jwt_extended import decode_token
import requests

def solicitar_validacion_acceso(token: str, recurso: str, operacion: str) -> int:
    """
    Extrae el usuario del token e invoca el servicio de autorización para validar
    si el usuario puede acceder al recurso solicitado
    """
    parametros = decode_token(token.split(' ')[1])

    #data_post = {"usuario": usuario, "recurso": recurso}
    #resp = requests.post(url='http://127.0.0.1:5002/autorizacion', json = data_post)
    
    resp = requests.get(url='http://127.0.0.1:5004/autorizacion', params={'usuario':parametros['sub'], 'recurso': recurso, 'operacion': operacion})

    return resp.status_code
