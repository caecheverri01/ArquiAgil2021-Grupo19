from microservicio_pacientes import create_app

app = create_app('default')
app_context = app.app_context()
app_context.push()