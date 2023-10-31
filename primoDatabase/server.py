import socket as sck 
import AlphaBot 
import time
import sqlite3

SEPARATOR = ";"


lista = [] #fare una select per beccare i vari comani nel db in atomatico 


def popolaLista():
    conn = sqlite3.connect("./tabella_movements.db")
    cur = conn.cursor()
    
    ris = cur.execute(f"SELECT Comando FROM Movements")
    ris1 = ris.fetchall()
    for tupla in ris1:
          lista.append(tupla[0])

    print(lista)
    #controlla che ci sia qualcosa in stringa    

        
    conn.close()



def carryOutQuery(cmd, robot ):
    conn = sqlite3.connect("./tabella_movements.db")
    cur = conn.cursor()
    
    ris = cur.execute(f"SELECT SeqComandi FROM Movements WHERE Comando ='{cmd}'")
    ris1 = ris.fetchall()
    stringa = ris1[0][0]
    #controlla che ci sia qualcosa in stringa    
    print(stringa)
    comandi = stringa.split(";")
    for c in comandi:
        comando =  c.split(",")
        char = comando[0]
        intero = int(comando[1])
        print(char, intero)
        commandtoRobot(char, robot, intero)

    conn.close()


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
    print("entro in lista")
    popolaLista()

    
    while True: 
        message = conn.recv(4096).decode()
        
        splitted_msg = message.split(SEPARATOR)
        if len(splitted_msg) != 2:
            print("error splitted message leght")
            continue
        
        command = splitted_msg[0]
        duration =  splitted_msg[1]

        #durata in secondi 
        if(command.lower() in lista):
            carryOutQuery(command.lower(), robot)
            pass
        elif(command.lower() == "e"):
            break 
        else:
            commandtoRobot(command, robot, int(duration)) 



    conn.close()
    soc.close()
        
            

        


if __name__ == "__main__":
    main()