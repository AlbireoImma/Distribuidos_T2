from concurrent import futures

import grpc
import proto.chat_pb2 as Chat
import proto.chat_pb2_grpc as RPC
import time

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
        print("[{}] {} {}".format(request.id,request.ts,request.mensaje))
        self.chats.append(request)
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
