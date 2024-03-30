from dotenv import load_dotenv, find_dotenv
import paho.mqtt.client as mqtt 
import os
import ssl


load_dotenv(find_dotenv())

def on_status(client, userdata, msg):
    print(f"messsage: {msg.payload.decode()}")

# logging for debugging
def on_log(client, userdata, level, buf):
    print("log: ", buf)



client_id = os.environ['CLIENT_ID']
broker_address = os.environ['MQTT_BROKER']
username = os.environ['MQTT_USERNAME']
password = os.environ['MQTT_PASSWORD']
port = os.environ['MQTT_PORT']
topic = os.environ['MQTT_TOPIC']

print(f"Client ID: {client_id}")
print(f"Broker Adress: {broker_address}")
print(f"Username: {username}")
print(f"port: {port}")
print(f"topic: {topic}")

# Create the client and set the message callback
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, transport='tcp', protocol=mqtt.MQTTv311, clean_session=True)

#logging 
client.on_log = on_log

client.username_pw_set(username, password)
client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)
client.on_message = on_status  # Set the callback before connecting

# Connect and subscribe
client.connect(broker_address, port=int(port))
client.subscribe(topic)

# Start the loop
client.loop_forever() 