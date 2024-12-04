import rpyc

def main():
    # Conexión con el servidor en localhost en el puerto 18812
    conn = rpyc.connect("localhost", 18812)

    # Invoca el método remoto 'on_add' pasando dos números
    result = conn.root.on_add(5, 3)
    print(f"Resultado de la suma: {result}")

    # Enviar un mensaje al servidor
    conn.root.on_message("¡Hola desde el cliente!")

    # Cierra la conexión
    conn.close()

if __name__ == "__main__":
    main()
