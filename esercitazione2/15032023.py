from time import sleep
from threading import Thread

class Task(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

'''
class Task1(Thread):
    def __init__(self, id, temp):
        Thread.__init__(self)
        self.id = id\    
        self.temp = temp



    def run(self):
        print(f"start thread {self.id} ...")
        sleep(self.temp)
        print(f"stop thread {self.id}...")

'''



class Task2(Task): #questo conta
    def __init__(self, id, quanto):
        Task.__init__(self,id)
        self.quanto = quanto

    def run(self):
        print(f"start thread {self.id} ...")

        
        for k in range(0, self.quanto):
            sleep(1)
            print(f"thread 2 k={k}...")

        print(f"stop thread {self.id}...")


class Task1(Task):
    def __init__(self, id, temp):
        Task.__init__(self,id)
        self.temp = temp

    def run(self):
        print(f"start thread {self.id} ...")
        sleep(self.temp)
        print(f"stop thread {self.id}...")



            
    


t1 = Task1(1,30)
t1.start()

t2 = Task2(2,30)
t2.start()




print("ho finito")

