from celery import Celery
import requests

celery_app = Celery(__name__, broker='redis://localhost:6379')

@celery_app.task()
def registrar_evento(trama):
    data_post = {"trama": trama}
    resp = requests.post(url='http://127.0.0.1:5001/monitor', json = data_post)