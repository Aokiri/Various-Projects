from ctypes import addressof
from multiprocessing import connection
import socket, sys, signal

# Variables globales
SRV_ADDR = input('Ingrese la IP del servidor: ')
SRV_PORT = int(input('Ingrese el puerto del servidor: '))

# Handler del Ctr+C
def def_handler(sig, frame):
    """Permite salir del programa al presionar Ctrl+C"""
    print('\n\n[!] Saliendo...')
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

print('Servidor establecido, esperando conexiones...')
connection, address = s.accept()
print(f'Cliente conectado con la dirección {address}')

# Bucle que mantiene la conexión establecida.
while 1:
    data = connection.recv(1024)
    if not data: 
        break
    connection.sendall(b'-- Mensaje recibido --\n')
    print(data.decode('utf-8'))
connection.close()