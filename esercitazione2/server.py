import socket as sck 
import AlphaBot 
import time
from threading import Thread, Lock
mutex = Lock()
class Task(Thread):
    def __init__(self, robot, conn):
        Thread.__init__(self)
        self.robot = robot
        self.conn = conn

    def run(self):

       while True:
            sensori = self.robot.getProssimitySensors()
            print(sensori)
            mutex.acquire()

            if sensori[0] == 0 or sensori[1] == 0:
             pass
             self.conn.sendall(f"senzori = {sensori}".encode())
            mutex.release()
            time.sleep(1)


SEPARATOR = ";"


def main():
    robot = AlphaBot.AlphaBot()
    soc = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    
    address = ("0.0.0.0", 5000)
    soc.bind(address)
    soc.listen()
    conn, client_address = soc.accept()
    print(f"sciao{client_address}")
    task = Task(robot, conn)
    task.start()
    while True: 
        message = conn.recv(4096).decode()
        '''
            f;int
        '''
        splitted_msg = message.split(SEPARATOR)
        if len(splitted_msg) != 2:
            print("error")
            continue
        
        command = splitted_msg[0]
        duration =  int(splitted_msg[1])

        #durata in secondi 
        if(command.lower() == "b"):
            robot.backward()
            time.sleep(duration/100)
            robot.stop()
        elif(command.lower() == "f"):
            robot.forward()
            time.sleep(duration/100)  
            robot.stop()
        elif(command.lower() == "l"):
            robot.left()
            time.sleep(duration/100)
            robot.stop()
        elif(command.lower() == "r"):
            robot.right()
            time.sleep(duration/100)
            robot.stop()
        elif(command.lower() == "e"):
            break 
        else:
            print("errore") 

    conn.close()
    soc.close()
        
            

        


if __name__ == "__main__":
    main()
