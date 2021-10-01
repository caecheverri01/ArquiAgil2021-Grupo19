from colorama import Fore
import requests

def autenticar(usuario: str, password: str) -> str:
    """
    Invoca el microservicio de autenticación
    """
    print(Fore.GREEN + '\nCONSUME SERVICIO AUTENTICACION')
    data_post = {"nombre": usuario, "contrasena": password}
    resp = requests.post(url='http://127.0.0.1:5000/login', json = data_post)

    if resp.status_code == 401:
        return None
    else:
        print(Fore.BLUE + 'Respuesta exitosa')
        return resp.json()['token']

def consumir_facturacion(token: str, id_factura: int):
    """
    Invoca el microservicio de facturación
    """
    print(Fore.GREEN + '\nCONSUME SERVICIO FACTURACION')
    resp = requests.get(url='http://127.0.0.1:5000/facturacion/' + str(id_factura), headers={'Authorization': 'Bearer ' + token})
    
    if resp.status_code == 200:
        print(Fore.BLUE + 'Respuesta exitosa')
        print(resp.json())
    else:
        print(Fore.RED + 'Respuesta no exitosa')
        print(resp.json())

def consumir_hc(token: str, id_historia: int):
    """
    Invoca el microservicio de historia clínica
    """
    resp = requests.get(url='http://127.0.0.1:5000/historia/' + str(id_historia), headers={'Authorization': 'Bearer ' + token})
    print(resp.json())