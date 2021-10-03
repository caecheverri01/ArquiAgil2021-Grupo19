from cliente import create_app
from .controlador import autenticar, consumir_facturacion
from colorama import Fore, init
import time

init(autoreset=True)

app = create_app('default')
app_context = app.app_context()
app_context.push()

usuarios = [{'usuario':'mgaitan', 'contrasena':'987654'}, {'usuario':'equintero', 'contrasena':'654321'}]

with app.app_context():
    i = 0
    while(i < 5):
        i = i + 1
        for usuario in usuarios:
            print(Fore.YELLOW + '\nINICIA PETICIONES CON USUARIO {}'.format(usuario['usuario']))
            token = autenticar(usuario['usuario'], usuario['contrasena'])
            time.sleep(1)
            consumir_facturacion(token, 1)
            time.sleep(2)