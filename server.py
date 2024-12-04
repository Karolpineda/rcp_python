import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("Cliente conectado")

    def on_disconnect(self, conn):
        print("Cliente desconectado")

    # Método de adición (asegúrate de que esté accesible)
    def on_add(self, a, b):
        return a + b

    # Definir las funciones que el cliente puede llamar
    def on_message(self, message):
        print(f"Recibido mensaje: {message}")

    # Expone los métodos a través del diccionario 'exposed'
    exposed = {
        "on_add": on_add,
        "on_message": on_message
    }

if __name__ == "__main__":
    from rpyc import ThreadedServer
    server = ThreadedServer(MyService, port=18812)
    print("Servidor en espera de clientes...")
    server.start()



