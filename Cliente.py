import threading

import grpc
import proto.chat_pb2 as Chat
import proto.chat_pb2_grpc as RPC
from datetime import datetime
import uuid

direccion = 'localhost'
puerto = 12000

class Cliente:

    def __init__(self):
        canal = grpc.insecure_channel(direccion + ':' + str(puerto))
        self.conexion = RPC.ServidorChatStub(canal)
        Usuarios = self.conexion.ObtenerLista(Chat.Nulo())
        Usuarios = Usuarios.lista.split(" ")
        print("Usuarios en el servidor:", Usuarios)
        self.ID = input("Ingrese su nombre de usuario: ")
        while self.ID in Usuarios or self.ID == "all":
            Usuarios = self.conexion.ObtenerLista(Chat.Nulo())
            Usuarios = Usuarios.lista.split(" ")
            print("Usuarios en el servidor:", Usuarios)
            self.ID = input("Ingrese un nombre no usado o prohibido (all): ")
        reg = Chat.Registro()
        reg.user = self.ID
        self.conexion.Registrar(reg)
        threading.Thread(target=self.recibirMensajes, daemon=True).start()
        print("Para obtener los datos de las personas en el servidor usar ?all")
        print("Los mensajes se envian de la forma: destino mensaje")
        print("Para enviar un mensaje global usar all como destino del mensaje")
        print("Usar ?close para desconectarse del servidor")
        while True:
            mensaje = input()
            if mensaje == "?all":
                Usuarios = self.conexion.ObtenerLista(Chat.Nulo())
                Usuarios = Usuarios.lista.split(" ")
                print("### Usuarios en el servidor ", Usuarios)
            elif mensaje == "?close":
                self.conexion.Desconectar(reg)
                return
            elif mensaje == "?list":
                Usuarios = self.conexion.ObtenerLista(Chat.Nulo())
                Usuarios = Usuarios.lista.split(" ")
                print("### Usuarios en el servidor ", Usuarios)
            else:
                if len(mensaje.split(" ")) > 1:
                    dest, mensaje  = mensaje.split(" ",1)
                    tiempo = datetime.now()
                    tiempo = tiempo.time().strftime("%H:%M:%S")
                    if mensaje is not '':
                        men = Chat.Mensaje()
                        men.id = str(uuid.uuid1())
                        men.ts = tiempo
                        men.mensaje = mensaje
                        men.destino = dest
                        men.sender = self.ID
                        self.conexion.EnviarMensaje(men)
                else:
                    print("Mensaje con formato incorrecto!")
    
    def recibirMensajes(self):
        for mensaje in self.conexion.FlujoMensajes(Chat.Nulo()):
            if mensaje.destino == self.ID or mensaje.destino == "all":
                print("[{}] {}: {}".format(mensaje.ts,mensaje.sender,mensaje.mensaje))


if __name__ == "__main__":
    cliente = Cliente()