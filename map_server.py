from server import Server

class Mapping_server(Server):
    def handle(self, message):
        try:
            print("Got: {}".format(message))
        except Exception as e:
            print("Error: {}".format(e))

if __name__ == "__main__":
    print("Server started.")
    app = Mapping_server("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()