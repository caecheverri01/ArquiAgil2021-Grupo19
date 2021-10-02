from ..modelos import logLogin, db
from colorama import Fore
import json

def validar_usuarios_autorizados(nombreu: str, rec: str, op: str) -> int:
    maxIntentos = 2
    autorizado=False
    autorizaciones = [{
        'usuario':
        'mgaitan',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get', 'post', 'put']
        }]
    }, {
        'usuario':
        'equintero',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get']
        }]
    }]

    """
    Validamos la autorización del usuario al recurso y operación
    """
    autorizacion = [x for x in autorizaciones if x['usuario'] == nombreu]
    if autorizacion:
        autorizacion = autorizacion[0]
        recurso = [
            x for x in autorizacion['recursos'] if x['nombre'] == rec
        ]
        if recurso:
            recurso = recurso[0]
            if op in recurso['opPermitidas']:
                autorizado = True
    
    """
    Guardamos log de movimiento por el autorizador
    """
    nuevo_registro = logLogin(usuario=nombreu, recurso=rec, operacion=op, estaAutorizado=autorizado)
    db.session.add(nuevo_registro)
    db.session.commit()
    
    """
    Analizamos log para validar si debemos bloquear el usuario
    """
    print(Fore.GREEN + '\nVERIFICACION INTENTOS PERMITIDOS A RECURSOS Y/O OPERACIONES')

    intentos = db.session.query(logLogin).filter(logLogin.usuario == nombreu, logLogin.estaAutorizado == False).count()

    if intentos > maxIntentos:
        return 401
    return 200

def validar_token(usuario: str, password: str) -> int:
    return 200