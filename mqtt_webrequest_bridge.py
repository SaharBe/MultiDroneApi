import requests
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish 
import threading
import json
    


drone_id={}
files=[]
headers = {'Authorization': 'Token 86fba008a1ae4c2407dc2846a676f9bc43d2b1a9'
}
added=[]
def del_old_drone():
	url_del_data = "http://127.0.0.1:8000/api/drones/"
	response = requests.request("GET", url_del_data, headers=headers)
	msg=response.json()
	for drone in msg:
          #print(j["id"])
          url=url_del_data+str(drone["id"])+"/"
          response = requests.request("DELETE", url, headers=headers)
          
          
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Drone/Info")

def send_commands():
 last_id = 0
 last_id_mission = 0
 while True:
    url_get_commands = "http://127.0.0.1:8000/api/commands"
    url_get_mission =  "http://127.0.0.1:8000/api/missions/"
    response = requests.request("GET", url_get_commands, headers=headers)
    if len(response.json()) !=0:
        send=response.json()[-1]
        if send["id"] != last_id:
            last_id=send["id"]
            publish.single("Drone/Command", str(json.dumps(send)), hostname="127.0.0.1") 
    response = requests.request("GET", url_get_mission, headers=headers)
    if len(response.json()) != 0:
        send_mission=response.json()[-1]
        if send_mission["id"] != last_id_mission:
            last_id_mission=send_mission["id"]
            publish.single("Drone/Mission", str(json.dumps(send_mission)), hostname="127.0.0.1")
            
            
            
def on_message(client, userdata, msg):  ## changing flights mdoe and arming / disarming
    url_send_data = "http://127.0.0.1:8000/api/drones/"
    message=msg.payload.decode('utf-8')
    message = message.replace("\'", "\'") 
    info=json.loads(message)    
    if info["name"] in drone_id.keys():
        url_send_data=url_send_data+str(drone_id[info["name"]])+'/'
        response = requests.request("PUT", url_send_data, headers=headers, data=info)
    else:
     response = requests.request("POST", url_send_data, headers=headers, data=info, files=files)
     i=response.json()
     print(i["id"])
     drone_id[info["name"]]=i["id"]
     #print(q)
     
     
     
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)      
if __name__=='__main__':
    del_old_drone()
    command_write=threading.Thread(target=send_commands)
    command_write.start()
    client.loop_forever()
