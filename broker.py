#!/usr/bin/python

import mosquitto
import RPi.GPIO as GPIO

#GPIO.cleanup(17)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

#Define '#' char
topic = chr(35)

#define what happens after connection
def on_connect(rc):
	print "Connected"

#On recipt of a message create a pynotification and show it
def on_message(msg):
	print((msg.topic, msg.payload))
	if msg.payload == 'on':
		GPIO.output(17, True)
	elif msg.payload == 'off':
		GPIO.output(17, False)

#create a broker
mqttc = mosquitto.Mosquitto("BROKER-PI")

#define the callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect

#connect
mqttc.connect("192.168.1.109", 1883, 60, True)

#subscribe to all topic`s
mqttc.subscribe(topic, 2)

#keep connected to broker
while mqttc.loop() == 0:
	pass

