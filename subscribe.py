import paho.mqtt.client as mqtt

broker = "152.67.164.1"
port = 1883
timelive = 60

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("TOPIC_HERE")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


client = mqtt.Client()
client.connect(broker, port, timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
