import mosquitto
from time import sleep

client = mosquitto.Mosquitto("test-client")

client.connect('192.168.1.109', port = 1883)
client.publish("kitchen/light", "on")
sleep(2)
client.publish("kitchen/light", "off")

client.disconnect()