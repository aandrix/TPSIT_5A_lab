import socket as sck 
import AlphaBot 
import time
import sqlite3

SEPARATOR = ";"


diz_query = {"quad":"quad"}


def carryOutQuery(cmd, robot ):
    conn = sqlite3.connect("./tabella_movements.db")
    cur = conn.cursor()
    
    ris = cur.execute(f"SELECT SecComandi FROM Movements WHERE Comando ={cmd}")
    
    comandi = ris.split(";")
    for c in comandi:
        comando=  c.split(",")
        char = comando[0]
        intero = int(comando[1])
        commandtoRobot(char, robot, intero)
    pass


def commandtoRobot(command, robot, duration):
    if(command.lower() == "b"):
            robot.backward()
            time.sleep(duration)
            robot.stop()
    elif(command.lower() == "f"):
            robot.forward()
            time.sleep(duration)  
            robot.stop()
    elif(command.lower() == "l"):
            robot.left()
            time.sleep(duration)
            robot.stop()
    elif(command.lower() == "r"):
            robot.right()
            time.sleep(duration)
            robot.stop()

def main():
    robot = AlphaBot.AlphaBot()
    soc = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    address = ("0.0.0.0", 5000)
    soc.bind(address)
    soc.listen()
    conn, client_address = soc.accept()
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
        if(command.lower() in diz_query):
            carryOutQuery(command.lower())
            pass
        elif(command.lower() == "e"):
            break 
        else:
            commandtoRobot(command, robot, duration) 

    conn.close()
    soc.close()
        
            

        


if __name__ == "__main__":
    main()