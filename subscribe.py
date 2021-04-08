import paho.mqtt.client as mqtt

broker = "<broker ip address>"
port = 1883
timelive = 60

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("<topic>")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


client = mqtt.Client()
client.connect(broker, port, timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
