import threading

import grpc
import proto.chat_pb2 as Chat
import proto.chat_pb2_grpc as RPC
from datetime import datetime
import uuid

direccion = 'localhost'
puerto = 12000

class Cliente:

    def __init__(self, ID):
        self.ID = ID
        canal = grpc.insecure_channel(direccion + ':' + str(puerto))
        self.conexion = RPC.ServidorChatStub(canal)
        threading.Thread(target=self.recibirMensajes, daemon=True).start()
        while True:
            print("Ingrese su mensaje: ")
            mensaje = input()
            tiempo = datetime.now()
            tiempo = tiempo.time().strftime("%H:%M:%S")
            if mensaje is not '':
                men = Chat.Mensaje()
                men.id = str(uuid.uuid1())
                men.ts = tiempo
                men.mensaje = mensaje
                self.conexion.EnviarMensaje(men)
    
    def recibirMensajes(self):
        for mensaje in self.conexion.FlujoMensajes(Chat.Nulo()):
            print("[{}] {} {}".format(mensaje.id,mensaje.ts,mensaje.mensaje))


if __name__ == "__main__":
    usuario = "Humberto"
    cliente = Cliente(usuario)