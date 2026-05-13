import paho.mqtt.client as paho

HOST = "mqtt.ics.ele.tue.nl"  #or mqtt.ics.ele.tue.nl
USER = "robot_26_1"
PASS = "L9bkrgZz"
TOPIC = "/pynqbridge/26/test"

client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.username_pw_set(USER, PASS)

print("Single or Loop? (s/l)")
mode = input().lower()
if mode == "s":
    try:
        client.connect(HOST)
        msg = input(f"Message for {TOPIC}: ")
        client.publish(TOPIC, msg)
        print("Sent!")
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")
elif mode == "l":
    try:
        client.connect(HOST)
        print(f"Publishing to {TOPIC}. Press CTRL+C to stop.")
        while True:
            msg = input(f"Message for {TOPIC}: ")
            client.publish(TOPIC, msg)
            print("Sent!")
    except KeyboardInterrupt:
        print("\nPublisher stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.disconnect()
        print("Disconnected from MQTT.")