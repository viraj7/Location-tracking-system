 #!/usr/bin/python3

import sys, ssl, json, time
import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect(mqttc, obj, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

def on_connect2(mqtt2, obj, flags, rc):
    if rc==0:
        print("Connected")
        mqtt2.subscribe("zanzito/Viraj/location")

def on_subscribe(mqtt2, obj, mid, granted_qos):
    print("Subscribed")

def on_message(mqtt2, obj, msg):
    #print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))
    data = msg.payload
    mqttc.publish("rasp3/viraj", data)
    print(data)

mqttc = mqtt.Client(client_id="rasp3")
mqtt2 = mqtt.Client(client_id="rasp")
mqttc.on_connect = on_connect
mqtt2.on_connect = on_connect2
mqtt2.on_subscribe = on_subscribe
mqtt2.on_message = on_message
mqttc.tls_set(ca_certs="/Users/virajj/cert/rootCA.pem.crt",
	            certfile="/Users/virajj/cert/abaf0fb0ba-certificate.pem.crt",
	            keyfile="/Users/virajj/cert/abaf0fb0ba-private.pem.key",
              tls_version=ssl.PROTOCOL_TLSv1_2,
              ciphers=None)

#connecting to aws-account-specific-iot-endpoint
mqtt2.connect("localhost", port=1883)
mqttc.connect("a5r3prb5qjzff.iot.us-west-2.amazonaws.com", port=8883) #AWS IoT service hostname and portno
mqttc.loop_start()
mqtt2.loop_forever()
