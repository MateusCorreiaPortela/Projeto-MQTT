import paho.mqtt.client as mqtt
import time
import json
from pydantic import BaseModel
import pika

credentials = pika.PlainCredentials('metam','metam')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='fila1')
channel.exchange_declare(exchange='exchange1')

channel.queue_bind(exchange='exchange1', queue='fila1', routing_key='chave1')




def on_messsage(client,userdata,message):
    try:
        payload = json.loads(message.payload.decode("utf-8"))
        mensagem = Validacao(**payload)
        print(mensagem)
        channel.basic_publish(exchange='exchange1',
                              routing_key='chave1',
                              body= json.dumps(payload))

    except:
        print('Erro')


class Validacao(BaseModel):
    ID : str
    data: str
    relogio: int
    vazao_instantanea : float



client = mqtt.Client(client_id='Cliente')
client.connect("mosquitto")
client.on_message = on_messsage
client.subscribe('topico1')
client.loop_forever()

time.sleep(10)
