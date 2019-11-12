import threading
import time
from random import randint
palo=["corazon","Trebol","Diamante","Espada"]
numero={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}
turno=False
def server():
    global turno
    while True:
        n=randint(1,100)
        print(n)
        if(n>70):
            turno=not turno
        time.sleep(1)
server = threading.Thread(target=server)
server.start()
print(not turno)
count=0
while(True):
    while(not turno):
        print("dentro del loop")
        time.sleep(1)
    print("ya tengo turno")
    time.sleep(1)
