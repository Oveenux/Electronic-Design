from flask import Flask, render_template,request, Response
import socket
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PRUEBA.html')

def enviar_datos():
    
    host = "0.0.0.0"  # Standard loopback interface address (localhost)
    port = 9001 # Port to listen on (non-privileged ports are > 1023)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        
        data, address = server_socket.recvfrom(1024)
        IP , puerto = address
        print(f'Received from {address}')
        print("="*40)
        nuevo_dato = f'ip:{IP}: ' + str(data.decode())  # Datos nuevos simulados
        yield f'data: {nuevo_dato}\n\n'
        time.sleep(1)  # Controla la frecuencia de envío de datos
        
@app.route('/stream')
def stream():
    return Response(enviar_datos(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run()
