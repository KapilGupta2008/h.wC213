import socket
from  threading import Thread
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller


SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your computer IP ADDR : ").strip()
screen_width = None
screen_height = None

keybord = Controller()

def getDeviceSize():
    global screen_width
    global screen_height
    for m in get_monitors():
        screen_width = int(str(m).split(",")[2].strip().split('width=')[1])
        screen_height = int(str(m).split(",")[3].strip().split('height=')[1])


def recivemessage(client_socket):
    global keybord
    while True:
        try:
            message=client_socket.recv(2048).decode()
            if message :
                newmessage=eval(message)
                if newmessage["data"]=="left_click":
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                
                elif newmessage["data"]=="right_click":
                    mouse.press(Button.rigt)
                    mouse.release(Button.right)
                else:
                    xpos=newmessage['data'][0]*screen_width
                    ypos=screen_height*(1-(newmessage['data'][1]-0.2)/0.6)
        except Exception as error:
            pass
                    
