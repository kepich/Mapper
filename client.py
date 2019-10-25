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

    server_ip = "127.0.0.1"
    server_port = 8889

    my_port = 8899
    my_ip = "localhost"

    message = my_ip + '_' + str(my_port) + '_' '00000001'
    app = Mapping_client(my_ip, my_port)
    app.start_server()
    app.send(server_ip, server_port, message)
    app.loop()
    app.stop_server()