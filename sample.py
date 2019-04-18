from pynput.mouse import Listener, Button
from pynput import keyboard
from pynput.keyboard import Key
import socket

TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889


tello_address = (TELLO_IP, TELLO_PORT)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

"""
def on_move(x, y):
  pass

def on_click(x, y, button, pressed):
  print("clicked: {x} {y} {button} {pressed}".format(x=x, y=y, button=button, pressed=pressed))
  if button == Button.left:
    send('takeoff')
  elif button == Button.right:
    send('land')

def on_scroll(x, y, dx, dy):
  print("scrolled: {x} {y} {dx} {dy}".format(x=x, y=y, dx=dx, dy=dy))
"""

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
     

def on_release(key):
  pass


def send(command):
  socket.sendto(command.encode('utf-8'), tello_address)  

if __name__ == '__main__':
  send('command')
  """
  with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener:
    mouse_listener.join()
  """

  with keyboard.Listener(on_press=on_press, on_release=on_release) as key_listener:
    key_listener.join()
