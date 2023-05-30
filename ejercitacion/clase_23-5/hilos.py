""" Ejercicios
1 - Escribir un programa que genere dos hilos utilizando threading.
Uno de los hilos debera leer desde stdin el texto ingresado por el usuario y deberá escribirlo en una cola de mensajes (queue).
El segundo hilo deberá leer desde la queue el contenido y encriptará dicho texto utilizando el algoritmo ROT13 y lo almacenará en una cola de mensajes (queue).
El primer hilo deberá leer dicho mensaje de la cola y lo mostrará por pantalla.
ROT13
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
gato (claro)->(rot13) tngb
2 - Analizar el comportamiento de el programa queue0.py y explicarlo. Usar Queue.join(), Thead.join(). Ejecutar el hilo deamon=True y deamon=False. """

import sys, threading, os, queue, sys, codecs

class Encrypter():
    def __init__(self):
        self.lifo_input = queue.LifoQueue()
        self.lifo_encrypt = queue.LifoQueue()

    def run(self):
        print("Ingrese el texto a encriptar (ingrese 'Exit' al finalizar)")
        th_rw = threading.Thread(target=self.th_rw, daemon=False)
        th_encrypt = threading.Thread(target=self.th_encrypt, daemon=True)
        th_rw.start()
        th_encrypt.start()

    def th_rw(self):
            line = sys.stdin.readline()
            self.lifo_input.put(line)
            self.lifo_input.join()
            try:
                while True:
                    print(self.lifo_encrypt.get(block=False), end="")
            except queue.Empty:
                print("Todo listo, adios!")

    def th_encrypt(self):
        while True:
            line = self.lifo_input.get(block=True)
            self.lifo_encrypt.put(codecs.encode(line, "rot_13"))
            self.lifo_input.task_done()


if __name__ == "__main__":
    app = Encrypter()
    app.run()