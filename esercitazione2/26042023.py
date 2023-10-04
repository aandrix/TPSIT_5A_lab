# 1 - faccio girare il programma senza il MUTEX (riga 14, 28, 35)
# devo importare Lock

######################################
# ho un contatore diviso tra 5 thread. Ogni thread prenderà il valore inziale
# del contatore e andrà a sommare il tempo proprio tempo di lavoro

#####################################
'''

Un processo produttore genera in modo casuale (anche con ripetizioni) numeri da 1 a 10 (inclusi) e
 li memorizza in un buffer condiviso che può contenere un solo numero alla volta. Due processi
 consumatori concorrenti tentano di acquisire tali numeri soltanto dopo la loro produzione.
 Uno dei due consumatori tenta di acquisire solo numeri da 1 a 5, l'altro solo numeri che vanno da 6 a 10.
Quando lo prendono settano il buffer (variabile) a 0 (zero)
'''

from time import sleep
from threading import Thread, Lock
import random

mutex = Lock()
counter = 0

'''
devo fare che ho una globale, data sta globale controllo 
'''

class produttore(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run



'''

from time import sleep
from threading import Thread, Lock
import random

mutex = Lock()  # creo il MUTEX
count = 1
'''

class ThreadContatore(Thread):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        # self.lock = threading.Lock()

    def run(self):
        global count

        # Inizio area MUTEX
        mutex.acquire()
        print(f"Thread {self.id}: count vale {count} inizio lavoro")
        x = random.randint(1, 5)
        print(f"Thread {self.id}: lavorerò per {x} secondi")
        sleep(x)
        count += x
        print(f"Thread {self.id}: count vale {count} fine lavoro incrementata di {x}")
        mutex.release()  # rilascio MUTEX


# creo 5 thread e li faccio partire

for i in range(5):
    thr = ThreadContatore(i)
    thr.start()

