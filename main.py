#Passo 1 - Importar as bibliotecas
import paho.mqtt.client as mqtt #Biblioteca do protocolo MQTT
import time #Biblioteca responsável pelos "delays" do código
import os 
from dotenv import load_dotenv
load_dotenv()

#Passo 2 - Instanciar conexão

#Credenciais de acesso ao servidor
BROKER = os.getenv("BROKER") #177.8.167.89" - IP EXTERNO
PORT = 7500
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOPIC = "aula_iot_show"
CLIENT_ID = "Prof Little Luiz"

#Função de conexão
def on_connect(client, userdata,flgs, rc:int):
    if rc==0:
        print("Conexão bem sucedida ao servidor")
    else:
        print("Não foi possível se conectar ao servidor")

def on_message(client, userdata, mensagem):
    print(f"A mensagem foi recebida no tópico {mensagem.topic} foi {mensagem.payload.decode()}")

#Passo 3 - Criar o cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=CLIENT_ID)

#Passo 4 - Configurar a conexão com o servidor
client.on_connect = on_connect
client.on_message = on_message

#Passo 5 - looping de leitura
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT)
client.subscribe(topic=TOPIC)
client.publish(TOPIC, "Oi gente, me conectei!")

if __name__ == '__main__':
    client.loop_forever()
