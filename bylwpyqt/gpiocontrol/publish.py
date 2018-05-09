import paho.mqtt.client as mqtt
import globallob.alllib as alllib

def on_publish(msg, rc):
    if rc == 0:
        print("publish success, msg = " + msg)

def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))

client = mqtt.Client(
    client_id="test_1", #client_id
    clean_session=True,
    userdata=None,
    protocol='MQTTv311'
)

trust = "/home/pi/mqtt-py/root_cert.pem" 
user = "xiaoxi/raspberry"
pwd = "XPJOqJxT68/RZPkiAgtwPecexPAKDoQ9ZknIHBPW524="
endpoint = "xiaoxi.mqtt.iot.gz.baidubce.com"
port = 1884

client.tls_set(trust) 
client.tls_insecure_set(True) 
client.username_pw_set(user, pwd) 
client.on_connect = on_connect 
client.connect(endpoint.encode(), port, 60) 
client.loop_start()

def sendwenshidu():
	msg = str(alllib.dh11date[0])
	rc , mid = client.publish("wendu", payload=msg, qos=1) #qos
	on_publish(msg, rc)

	msg = str(alllib.dh11date[1])
	rc , mid = client.publish("shidu", payload=msg, qos=1) #qos
	on_publish(msg, rc)
def sendcontrol():
	msg = str(alllib.cmdflag)
	rc , mid = client.publish("deng", payload=msg, qos=1) #qos
	on_publish(msg, rc)
