import socket
from server import Server
import sys

class Mapping_client(Server):
    def handle(self, message):
        try:
            print("Got: {}".format(message))
        except Exception as e:
            print("Error: {}".format(e))

if __name__ == "__main__":
    print("Client started...")
    app = Mapping_client("localhost", 8899)
    app.start_server()
    app.send("localhost", 8889, "message")
    app.stop_server()