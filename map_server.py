from server import Server
from level_map import Level_map

class Mapping_server(Server):
    def __init__(self, ip, port):
        super(Mapping_server, self).__init__(ip, port)
        self.map_file = Level_map()

    def handle(self, message):
        try:
            print("Got: {}".format(message))
        except Exception as e:
            print("Error: {}".format(e))

if __name__ == "__main__":
    print("Server started...")
    app = Mapping_server("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()