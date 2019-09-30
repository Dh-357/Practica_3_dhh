import threading
import time

pa=0
pb=0
pc=0
pd=0
e1=0
e2=0
pak1=0
pak2=0
velocidad=2


def productor_a():
    global pa
    hilo_actual = threading.current_thread().getName()
    while True:
        pa+=1
        print(hilo_actual,'creando objeto: ',pa,'A')
        time.sleep(velocidad)

def productor_b():
    global pb
    hilo_actual = threading.current_thread().getName()
    while True:
        pb+=1
        print(hilo_actual,'creando objeto: ',pb,'B')
        time.sleep(velocidad)    

def ensamblador_1():
    global e1
    hilo_actual = threading.current_thread().getName()
    while True:
        if 2%pa==0 and 2%pb==0:
            e1+=1
            print(hilo_actual,'armando paquete: ',e1,'E')
            time.sleep(velocidad)

def productor_c():
    global pc
    hilo_actual = threading.current_thread().getName()
    while True:
        pc+=1
        print(hilo_actual,'creando objeto: ',pc,'B')
        time.sleep(velocidad)    

def ensamblador_2():
    global e2
    hilo_actual = threading.current_thread().getName()
    while True:
        if pc%2==0 and e1%1==0:
            e2+=1
            print(hilo_actual,'armando paquete: ',e2,'E')
            time.sleep(velocidad)

def productor_d():
    global pd
    hilo_actual = threading.current_thread().getName()
    while True:
        pd+=1
        print(hilo_actual,'creando objeto: ',pd,'B')
        time.sleep(velocidad)    

def empaquetador_1():
    global pak1
    hilo_actual = threading.current_thread().getName()
    while True:
        if e2%2==0:
            pak1+=1
            print(hilo_actual,'armando paquete: ',pak1,'E')
            time.sleep(velocidad)

def empaquetador_2():
    global pak2
    hilo_actual = threading.current_thread().getName()
    while True:
        if pd%10==0:
            pak2+=1
            print(hilo_actual,'armando paquete: ',pak2,'E')
            time.sleep(velocidad)

hilo1= threading.Thread(name='PRODUCTOR A', target=productor_a)
hilo2= threading.Thread(name='PRODUCTOR B', target=productor_b)
hilo3= threading.Thread(name='-----ENSAMBLADOR 1', target=ensamblador_1)
hilo4= threading.Thread(name='PRODUCTOR C', target=productor_c)
hilo5= threading.Thread(name='-----ENSAMBLADOR 2', target=ensamblador_2)
hilo6= threading.Thread(name='PRODUCTOR D', target=productor_d)
hilo7= threading.Thread(name='#-#-#-#-#-EMPAQUETADOR 1', target=empaquetador_1)
hilo8= threading.Thread(name='#-#-#-#-#-EMPAQUETADOR 2', target=empaquetador_2)

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()
hilo8.start()

