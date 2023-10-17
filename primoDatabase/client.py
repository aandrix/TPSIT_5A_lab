import socket as sck 

SEPARATOR = ";"
SERVER_ALPHABOT = ("192.168.1.138", 5000)

def main():
    soc = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    soc.connect(SERVER_ALPHABOT)

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