import threading
import time

def tarefa1():
    x = 0
    
    while x < 5:
        print("Tarefa 1")
        x += 1


def tarefa2():
    y = 0
    
    while y < 5: 
       print("Tarefa 2")
       y += 1
     
       
def tarefa3():
     z = 0
     
     while z < 5:
         print("Tarefa 3")
         z += 1
           

threading.Thread(target=tarefa1).start() #inicia com a tarefa 1       
tarefa2()
tarefa3()

'''
O resultado vai ser uma impressão sem padrão, 
pois ficará misturado de acordo com a necessidade do sistema.
'''