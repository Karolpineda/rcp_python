import rpyc

def main():
    # Conexión con el servidor en localhost en el puerto 18812
    conn = rpyc.connect("localhost", 18812)

    # Invoca el método remoto 'exposed_on_add' pasando dos números
    result = conn.root.exposed_on_add(5, 3)
    print(f"Resultado de la suma: {result}")

    # Cierra la conexión
    conn.close()

if __name__ == "__main__":
    main()
