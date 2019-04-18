import socket
import json

with open("./ip.json","r",encoding="utf-8") as configCode:
    config = configCode

TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889

tello_address = (TELLO_IP, TELLO_PORT)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto("command".encode('utf-8'), tello_address)
socket.sendto("land".encode('utf-8'), tello_address)