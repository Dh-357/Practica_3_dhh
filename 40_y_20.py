import threading
import time
total_a=0
total_b=0
total_e=0
total_p=0
cont_a=0
cont_b=0
cont_e=True
cont_p=False
x=0
bloqueo=threading.Lock()   
def productor_a():
    global cont_a
    global total_a
    global cont_b
    cont_b=0
    hilo_actual = threading.current_thread().getName()
    while cont_a < 2:
        bloqueo.acquire()
        cont_a+=1
        total_a = total_a + 1
        print(hilo_actual,'creando objeto: ', total_a,'A')
        time.sleep(.8)
        bloqueo.release()
def productor_b():
    global cont_b
    global cont_a
    global cont_e
    global total_b
    hilo_actual = threading.current_thread().getName()
    while cont_b < 3:
        bloqueo.acquire()
        cont_b+=1
        total_b = total_b + 1
        print(hilo_actual,'creando objeto: ', total_b,'B')
        time.sleep(.8)    
        bloqueo.release()
    cont_a=0
    cont_e=True
def ensamblador():
    global x
    global cont_e
    global total_e
    global cont_p
    hilo_actual = threading.current_thread().getName()
    while cont_e ==True:
        bloqueo.acquire()
        total_e = total_e + 1
        x+=1
        print(hilo_actual,'ensamblando : ', total_e,'E')
        time.sleep(.8)
        cont_e=False
        bloqueo.release()
    

def empaquetador():
    global total_p
    global cont_p
    global x
    if (x % 5)==0:
        cont_p=True
    while cont_p==True:
        hilo_actual = threading.current_thread().getName()
        bloqueo.acquire()
        total_p = total_p + 1
        print(hilo_actual,'armando paquete: ', total_p,'P')
        time.sleep(.8)
        cont_p=False
        bloqueo.release()

def chambear():
    hilo1= threading.Thread(name='PRODUCTOR_A', target=productor_a)
    hilo2=threading.Thread(name='PRODUCTOR_B', target=productor_b)
    hilo3=threading.Thread(name='-------ENSAMBLADOR', target=ensamblador)
    hilo4=threading.Thread(name='#-#-#-#-#-#-EMPAQUETADOR', target=empaquetador)

    hilo1.start()
    hilo2.start()
    hilo2.join()
    hilo3.start()
    hilo4.start()
    hilo4.join()
    
for x in range(25):
    chambear()

print("\nListo....5 Paquetes armados")
