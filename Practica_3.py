import os
import itertools
def mas_repetido(): #recibe matriz
    print("probando funcion uno")
    pass

def condensa(): #recibe cadena
    limpia_pantalla()
    cadena=input("Introduce la cadena entre comillas:  ")
    lista_palabras=list(cadena)
    frecuencia_palabras=[]
    for x in lista_palabras:
        frecuencia_palabras.append(lista_palabras.count(x))
    lista_repetida=list(zip(lista_palabras, frecuencia_palabras))
    lista_nueva=[]
    for y in lista_repetida:
        if y not in lista_nueva:
            lista_nueva.append(y)
    print("Las parejas ordenadas con la letra y el numero de repeticiones es:\n")
    print(lista_nueva)
    pass

def triangulo_pascal(): #recibe niveles
    print("probando funcion tres")
    pass

def subcadenas(): #recibe cadena
    limpia_pantalla()
    listax=[]
    listay=[]
    cadena=input("Introduce la cadena (entre comillas):    ")
    listax=list(cadena)
    for L in range(0, len(listax)+1):
        for elqsige in itertools.combinations(listax, L):
            listay.append(elqsige)
    print(listay)    
    pass

def limpia_pantalla():
    if os.name == "posix":
        os.system("clear")        
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    pass
    

def default():
    print("Escoje un numero del 1 al 4 (unicamente)")
    pass

if __name__=="__main__":
    menu=True
    while menu:
        eleccion=int(input("introduce el numero de funcion\n\n"+
            "1.......Funcion(mas repetido)\n"+
            "2.......Funcion(condensa)\n"+
            "3.......Funcion(triangulo pascal)\n"+
            "4.......Funcion(subcadenas)\n"+
            "5.......SALIR DEL PROGRAMA\n\n"+
            "input:  "))
        if eleccion == 5:
            menu=False
            
        elif eleccion == 1:
            limpia_pantalla()
            mas_repetido()
            raw_input("Funcion completada.....(press ENTER)")
            limpia_pantalla()
    
                
        elif eleccion == 2:
            limpia_pantalla()
            condensa() 
            raw_input("Funcion completada.....(press ENTER)")            
            limpia_pantalla()
        elif eleccion == 3:
            limpia_pantalla()
            triangulo_pascal()
            raw_input("Funcion completada.....(press ENTER)")            
            limpia_pantalla()
        elif eleccion == 4:
            limpia_pantalla()
            subcadenas()
            raw_input("Funcion completada.....(press ENTER)")            
            limpia_pantalla()
        else:
            limpia_pantalla()
            default()
            raw_input("Funcion completada.....(press ENTER)")            
            limpia_pantalla()
            
        
    
