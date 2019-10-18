# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:43:22 2019
"""

import time
import paho.mqtt.client as mqtt
from conf import Conf

start_time = time.monotonic()

def on_connect(client, userdata, flags, rc):
    print("on_connect", rc)
    global start_time
    start_time = time.monotonic()
    client.subscribe([('test/topic/'+str(i)+'/+', 1) for i in range(0,100)])


def on_subscribe(client, userdata, mid, granted_qos):
    global start_time
    print("on_subscribe", time.monotonic()-start_time)
    

client = mqtt.Client(client_id=Conf["client_id"], clean_session=True)
client.tls_set_context(Conf["sslcontext"])
client.username_pw_set(username=Conf["username"], password=Conf["password"])

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.connect(host=Conf["hostname"], port=Conf["port"])

client.loop_forever()






