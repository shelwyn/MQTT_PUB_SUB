import paho.mqtt.client as paho

broker = "<broker ip address>"
port = 1883

def on_publish(client, userdata, result):
    print("Message published")
   
client = paho.Client("<client name>")
client.on_publish = on_publish
client.connect(broker, port)
message = "MESSAGE_TO_PUBLISH"

PUB = client.publish("TOPIC", message)
