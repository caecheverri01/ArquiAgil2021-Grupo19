from ..modelo import EjecucionServicio
from ..modelo import db
import asyncio
import smtplib

def registrar_trama(trama):
    """
    Descompone y registra la trama recibida en la base de datos
    """
    campos = trama.split('|')
    
    nuevo_ejecucion = EjecucionServicio(servicio=campos[0], respuesta=campos[1], tiempo=campos[2])

    db.session.add(nuevo_ejecucion)
    db.session.commit()

    return campos[0]

def crear_conexion_notificacion():
    """
    Crea y retorna la conexión con el servidor de correos
    """
    _smtp = smtplib.SMTP('smtp.gmail.com', 587)
    _smtp.ehlo()
    _smtp.starttls()
    _smtp.login('caecheverri01@gmail.com', 'app password')

    return _smtp

def enviar_notificacion(_smtp, servicio):
    """
    Envía una notificación de adevertencia
    """
    msg = 'Subject: Advertencia' + '\n' + 'Hola\n\nSe te informa que se pueden estar presentando problemas de disponibilidad con el servicio ' + servicio
    _smtp.sendmail('caecheverri01@gmail.com', 'caecheverri01@gmail.com', msg)

def generar_advertencia_respuesta_error(total_registros, servicio): 
    """
    Procesa la información del servicio y determina si se debe generar una advertencia por
    la cantidad de respuestas erroneas (código 501). La advertencia se genera si la cantidad 
    de ejecuciones es mayor a 10 y las respuestas erroneas es mayor al 10%
    """   
    total_error = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio, EjecucionServicio.respuesta == '501').count()

    porcentaje_error = total_error / total_registros

    if(total_registros > 10 and porcentaje_error > 0.1):
        return True
    
    return False

def generar_advertencia_tiempos(servicio):
    """
    Procesa la información del servicio y determina si se debe generar una advertencia por
    la tendencia en los tiempos de respuesta de un servicio. La advertencia se genera si la 
    tendecia indica que los tiempos están incrementando
    """
    tiempo_base = 200
    tiempos = []
    total_exito = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio, EjecucionServicio.respuesta == '201')

    for ejecucion_servicio in total_exito:
        tiempos.append(ejecucion_servicio.tiempo - tiempo_base)
   
    incrementos = [num for num in tiempos if num > 0]
    porcentaje_incrementos = len(incrementos) / len(tiempos)

    if(len(tiempos) > 10 and porcentaje_incrementos > 0.5):
        return True

    return False


async def procesar_tramas(servicio):
    """
    Funciona asincrona que procesa las tramas registradas de un servicio
    """
    total_registros = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio).count()

    if(generar_advertencia_respuesta_error(total_registros, servicio) or generar_advertencia_tiempos(servicio)):
        _smtp = crear_conexion_notificacion()
        enviar_notificacion(_smtp, servicio)
        _smtp.quit()

async def main(servicio):
    """
    Funciona asincrona que crea la tarea de ejecución para el procesamiento de las tramas
    """
    task = asyncio.create_task(procesar_tramas(servicio))