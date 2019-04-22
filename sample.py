from pynput.mouse import Listener, Button
from pynput import keyboard
from pynput.keyboard import Key
import socket
import json

with open("./config/config.json",'r',encoding='utf-8') as code:
    config = json.load(code)

TELLO_IP = config["ip"]
TELLO_PORT = config["drone_port"]
TELLO_VIDEO_PORT = config["video_port"]


tello_address = (TELLO_IP, TELLO_PORT)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def on_press(key):
    try:
        if key.char == 'f':
            send('flip f')
    except AttributeError:
        print("AttributeError")
        print(key)

    if key == Key.page_up:
        send('takeoff')
    elif key == Key.page_down:
        send('land')
    elif key == Key.up:
        send('forward 100')
    elif key == Key.down:
        send('back 100')
    elif key == Key.right:
        send('right 100')
    elif key == Key.left:
        send('left 100')
    elif key == Key.esc:
        exit()


def on_release(key):
    pass


def send(command):
    socket.sendto(command.encode('utf-8'), tello_address)

if __name__ == '__main__':
    send('command')

    with keyboard.Listener(on_press=on_press, on_release=on_release) as key_listener:
        key_listener.join()
