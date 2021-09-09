from ..modelo import EjecucionServicio
from ..modelo import db
from colorama import Fore, init
import asyncio
import smtplib

init(autoreset=True)

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
    _smtp.login('caecheverri01@gmail.com', 'srieyvupdyskwufw')
    
    return _smtp

def enviar_notificacion(servicio):
    """
    Envía una notificación de adevertencia
    """
    _smtp = crear_conexion_notificacion()
    msg = 'Subject: Advertencia' + '\n' + 'Hola\n\nSe te informa que se pueden estar presentando problemas de disponibilidad con el servicio ' + servicio
    _smtp.sendmail('caecheverri01@gmail.com', 'caecheverri01@gmail.com', msg)    
    _smtp.quit()

def generar_advertencia_respuesta_error(total_registros, servicio): 
    """
    Procesa la información del servicio y determina si se debe generar una advertencia por
    la cantidad de respuestas erroneas (código 501). La advertencia se genera si la cantidad 
    de ejecuciones es mayor a 10 y las respuestas erroneas es mayor al 10%
    """
    print(Fore.GREEN + '\nVERIFICACION ADVERTENCIA POR RESPUESTAS ERROR')

    total_error = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio, EjecucionServicio.respuesta == '501').count()

    porcentaje_error = total_error / total_registros * 100

    print(Fore.GREEN + 'Total tramas: {0} - Total con error: {1} - Porcentaje error: {2:3.0f}'.format(total_registros, total_error, porcentaje_error))

    if(total_registros > 5 and porcentaje_error > 10):
        return True
    
    return False

def generar_advertencia_tiempos(servicio):
    """
    Procesa la información del servicio y determina si se debe generar una advertencia por
    la tendencia en los tiempos de respuesta de un servicio. La advertencia se genera si la 
    tendecia indica que los tiempos están incrementando
    """
    print(Fore.BLUE + '\nVERIFICACION ADVERTENCIA DEGRADACION SERVICIO')    
    tiempo_base = 200
    tiempos = []
    registros_exito = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio, EjecucionServicio.respuesta == '201')

    for ejecucion_servicio in registros_exito:
        tiempos.append(ejecucion_servicio.tiempo - tiempo_base)
   
    incrementos = [num for num in tiempos if num > 0]
    porcentaje_incrementos = len(incrementos) / len(tiempos) * 100

    print(Fore.BLUE + 'Total respuesta exito: {0} - Total > base: {1} - Porcentaje > base: {2:2.0f}'.format(len(tiempos), len(incrementos), porcentaje_incrementos))

    if(len(tiempos) > 5 and porcentaje_incrementos > 50):
        return True

    return False

async def procesar_tramas(servicio):
    """
    Funciona asincrona que procesa las tramas registradas de un servicio
    """
    total_registros = db.session.query(EjecucionServicio).filter(EjecucionServicio.servicio == servicio).count()
    print(Fore.YELLOW + '\nINICIA PROCESAMIENTO TRAMAS SERVICIO {}'.format(servicio))

    if(generar_advertencia_respuesta_error(total_registros, servicio) or generar_advertencia_tiempos(servicio)):
        print(Fore.RED + 'supera porcentaje permitido se envia notificacion')
        enviar_notificacion(servicio)

async def main(servicio):
    """
    Funciona asincrona que crea la tarea de ejecución para el procesamiento de las tramas
    """
    task = asyncio.create_task(procesar_tramas(servicio))