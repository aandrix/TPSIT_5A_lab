import socket as sck 
from threading import Thread, Lock
mutex = Lock()


class Senzori(Thread):
    def __init__(self, con):
        Thread.__init__(self)
        self.con = con

    def run(self):
        while True:
         mutex.acquire()

         message = self.con.recv(4096)
         #sensore 1;sensore 2 (sono boleani)
         print(message.decode())
         mutex.release()
         

        


        pass




SEPARATOR = ";"
SERVER_ALPHABOT = ("192.168.1.121", 5000)

def main():
    soc = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    soc.connect(SERVER_ALPHABOT)

    senzori = Senzori(soc)
    senzori.start()
    while True:
        command = input("inserire il comando ")
        duration = input("inserire la dutata (sec) ")
        message = f"{command}{SEPARATOR}{duration}".encode()
        soc.sendall(message)
        if command.lower() == "e":
            break
    soc.close()


if __name__ == "__main__":
    main()