import os

def mas_repetido(): #recibe matriz
    print("probando funcion uno")
    pass

def condensa(): #recibe cadena
    print("probando funcion dos")
    pass

def triangulo_pascal(): #recibe niveles
    print("probando funcion tres")
    pass

def subcadenas(): #recibe cadena
    print("probando funcion cuatro")    
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
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            mas_repetido()
            raw_input("Funcion completada.....(press ENTER)")
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
    
                
        elif eleccion == 2:
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            condensa() 
            raw_input("Funcion completada.....(press ENTER)")            
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
        elif eleccion == 3:
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            triangulo_pascal()
            raw_input("Funcion completada.....(press ENTER)")            
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
        elif eleccion == 4:
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            subcadenas()
            raw_input("Funcion completada.....(press ENTER)")            
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
        else:
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            default()
            raw_input("Funcion completada.....(press ENTER)")            
            if os.name == "posix":
                os.system("clear")        
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
            
        
    