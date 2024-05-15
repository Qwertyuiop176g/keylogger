import socketserver
from datetime import datetime

class LoggerServer(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        data = self.request[0].strip().decode("utf-8")  # Decode the incoming bytes
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
        with open("keystrokes.txt", "a") as f:
            f.write("[{}] {}: {}\n".format(timestamp, self.client_address[0], data))  # Add a formatted entry with timestamp

HOST, PORT = "0.0.0.0", 3008

try:
    # Create the server, binding to localhost on port 3008
    with socketserver.UDPServer((HOST, PORT), LoggerServer) as server:
        print("Server started...")
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
except Exception as e:
    print("An error occurred:", e)
