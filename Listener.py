import paho.mqtt.client as paho

class Broker:
    def __init__(self, host, username, password, topicSubList, messageHandler):
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(username, password)
        self.client.on_message = messageHandler
        
        if self.client.connect(host=host) != 0:
            raise RuntimeError("Couldn't connect to the MQTT host")
            
        try:
            for topic in topicSubList:
                self.client.subscribe(topic)
            print(f"Listening for messages on: {topicSubList}")
            print("Press CTRL+C to stop.")
            self.client.loop_forever()
        except KeyboardInterrupt:
            print("\nListener stopped by user.")
        except Exception as error:
            print(error)
        finally:
            self.client.disconnect()
            print("Disconnected from MQTT.")

def messageHandler(client, userdata, message):
    # This distinguishes between the two topics automatically
    print(f"[{message.topic}] -> {message.payload.decode('utf-8')}")

if __name__ == "__main__":
    # To be changed with actual credentials and host if needed
    Broker(
        host="mqtt.ics.ele.tue.nl", #or mqtt.ics.ele.tue.nl
        username="robot_26_1",
        password="L9bkrgZz",
        topicSubList=["topic1", "topic2", "/pynqbridge/26/test", "/pynqbridge/26/send"], 
        messageHandler=messageHandler
    )
