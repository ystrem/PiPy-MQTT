import mosquitto

client = mosquitto.Mosquitto("test-client")

client.connect('192.168.1.109', port = 1883)
client.publish("rbpi", "hello world")

client.disconnect()