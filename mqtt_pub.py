import paho.mqtt.client as mqtt
from random import randint
from time import sleep
def on_connect(client, userdata, flags, rc):
	print("connected")




client=mqtt.Client("rangita")
client.on_connect=on_connect

client.tls_set(ca_certs="m2mqtt_srv.crt")
client.connect('192.168.0.14' , 8883, 60)
client.loop_start()

while(1):
	client.publish("nba",randint(1,100))
	sleep(2)
	
	
