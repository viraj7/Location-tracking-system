import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("connected")
    client.subscribe("nba")

def on_message(client, userdata, message):
    print("Message:", message.payload)

client=mqtt.Client("Viraj")
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs="m2mqtt_srv.crt")
client.connect('192.168.0.14' , 8883, 60)
client.loop_forever()
