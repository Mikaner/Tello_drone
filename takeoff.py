import socket
import json

with open("./config/config.json",'r',encoding="utf-8") as code:
    config = code

TELLO_IP = config["ip"]
TELLO_PORT = config["drone_port"]
TELLO_VIDEO_PORT = config["video_port"]

tello_address = (TELLO_IP, TELLO_PORT)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto("command".encode('utf-8'), tello_address)
socket.sendto("takeoff".encode('utf-8'), tello_address)
