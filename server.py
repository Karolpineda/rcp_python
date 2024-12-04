import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("Cliente conectado")

    def on_disconnect(self, conn):
        print("Cliente desconectado")

    # Método de adición
    def on_add(self, a, b):
        return a + b

    # Expone los métodos que se pueden invocar de forma remota
    def exposed_on_add(self, a, b):
        return self.on_add(a, b)

if __name__ == "__main__":
    from rpyc import ThreadedServer
    server = ThreadedServer(MyService, port=18812)
    print("Servidor en espera de clientes...")
    server.start()
