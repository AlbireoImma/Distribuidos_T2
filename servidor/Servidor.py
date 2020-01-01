from concurrent import futures

import grpc
import proto.chat_pb2 as Chat
import proto.chat_pb2_grpc as RPC
import time
from datetime import datetime

def ts():
        tiempo = datetime.now()
        tiempo = tiempo.time().strftime("%H:%M:%S")
        return tiempo

class ServidorChat(RPC.ServidorChatServicer):
    
    def __init__(self):
        self.chats = []
        self.clientes = []
    
    def FlujoMensajes(self, request_iterator, context):
        indice = 0
        men = Chat.Mensaje()
        while True:
            while len(self.chats) > indice:
                men = self.chats[indice]
                indice += 1
                yield men
    
    def EnviarMensaje(self, request: Chat.Mensaje, context):
        print("mensaje de {} para {}".format(request.sender,request.destino))
        archivo = open("log.txt","a+")
        log = "[{}] ({}) {} --> {} {}\n".format(request.ts,request.id,request.sender,request.destino,request.mensaje)
        archivo.write(log)
        self.chats.append(request)
        return Chat.Nulo()
    
    def Registrar(self, request: Chat.Registro, context):
        self.clientes.append(request.user)
        archivo = open("log.txt","a+")
        time = ts()
        time = "[" + time + "]"
        archivo.write(time + " Usuario " + request.user + " conectado\n")
        print("Usuario [{}] registrado".format(request.user))
        return Chat.Nulo()

    def ObtenerLista(self, request, context):
        lista = Chat.Listado()
        aux = ""
        for user in self.clientes:
            user += " "
            aux += user
        lista.lista = aux
        return lista

    def Desconectar(self, request: Chat.Registro, context):
        user = request.user
        archivo = open("log.txt","a+")
        self.clientes.append(request.user)
        time = ts()
        time = "[" + time + "]"
        archivo.write(time + " Usuario " + request.user + " desconectado\n")
        print("Usuario [{}] Desconectado".format(user))
        if user in self.clientes:
            self.clientes.remove(user)
        return Chat.Nulo()
    
    

if __name__ == "__main__":
    puerto = 12000 # Puerto del servidor
    # Creamos un servidor grpc con maximo 10 conexiones
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    RPC.add_ServidorChatServicer_to_server(ServidorChat(), server) # Agregamos los servicios al servidor grpc
    print("Servidor en marcha...")
    server.add_insecure_port('[::]:' + str(puerto))
    server.start() # Servidor corriendo en segundo plano
    while True:
        time.sleep(100000)
