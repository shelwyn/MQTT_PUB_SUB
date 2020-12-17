import paho.mqtt.client as paho

broker = "152.67.164.1"
port = 1883
timelive = 60

def on_publish(client, userdata, result):
    print("Published Message")
    pass
   
client = paho.Client("CLIENT_NAME")
client.on_publish = on_publish
client.connect(broker, port)
message = "MESSAGE_TO_PUBLISH"

PUB = client.publish("TOPIC", message)
