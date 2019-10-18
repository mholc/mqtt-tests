import paho.mqtt.publish as publish
import sys
from conf import Conf

topics = [x.strip() for x in sys.stdin.readlines()]

publish.multiple([(t, b'data', 1, True) for t in topics], 
    hostname=Conf["hostname"], 
    port=Conf["port"], client_id=Conf["client_id"], 
    tls=Conf["sslcontext"],
    auth={'username':Conf["username"], 'password':Conf["password"]})

