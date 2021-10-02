from ..modelos import logAutorizaciones, db
from colorama import Fore
import requests

def validar_permisos(nombreu: str, rec: str, op: str) -> int:
    autorizado=False
    autorizaciones = [{
        'usuario':
        'mgaitan',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'historia',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'pacientes',
            'opPermitidas': ['get', 'post', 'put']
        }
        ]
    }, {
        'usuario':
        'equintero',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get']
        }, {
            'nombre': 'historia',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'pacientes',
            'opPermitidas': ['get', 'post', 'put']
        }
        ]
    }, {
        'usuario':
        'frojas',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'historia',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'pacientes',
            'opPermitidas': ['get', 'post', 'put']
        }
        ]
    }, {
        'usuario':
        'cecheverri ',
        'recursos': [{
            'nombre': 'facturacion',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'historia',
            'opPermitidas': ['get', 'post', 'put']
        }, {
            'nombre': 'pacientes',
            'opPermitidas': ['get', 'post', 'put']
        }
        ]
    }
    ]

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
    nuevo_registro = logAutorizaciones(usuario=nombreu, recurso=rec, operacion=op, estaAutorizado=autorizado)
    db.session.add(nuevo_registro)
    db.session.commit()

    if autorizado:
        return 200
    return 401

def valida_bloqueo_usuario(nombreu: str):
    maxIntentos = 2

    """
    Analizamos log para validar si debemos bloquear el usuario
    """
    print(Fore.GREEN + '\nVERIFICACION ACCESO A RECURSOS Y/O OPERACIONES PARA EL USUARIO '+ nombreu)

    intentos = db.session.query(logAutorizaciones).filter(logAutorizaciones.usuario == nombreu, logAutorizaciones.estaAutorizado == False).count()

    if intentos > maxIntentos:
        resp = requests.put(url='http://127.0.0.1:5001/bloqueo/' + str(2))
        if resp.status_code == 401:
            return "Se ha bloqueado el usuario "+ nombreu + " por exceder el límite de accesos no autorizados"

def validar_token(usuario: str, password: str) -> int:
    return 200