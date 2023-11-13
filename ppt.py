print("Escribe una de las letras correspondientes para jugar piedra, papel, tijera, lagarto o spock contra la máquina")
print("a) piedra")
print("b) papel")
print("c) tijera")
print("d) lagarto")
print( "e) spock")
import random
opciones = ("piedra" , "papel" , "tijera" , "lagarto" , "spock")
c = input ()
if c == ("a") : print("Eligió piedra, la máquina jugará con: ") 
if c == ("b") : print("Eligió papel, la máquina jugará con: ")
if c == ("c") : print("Eligió tijera, la máquina jugará con: ")
if c == ("d") : print("Eligió lagarto, la máquina jugará con:") 
if c == ("e") : print("Eligió spock, la máquina jugará con:") 
seleccion = random.choice(opciones) 
print(seleccion)
if seleccion == "piedra": 
    if c == "a":
        print("Empate")
    elif c == "b": 
        print("La máquina ganó") 
    elif c == "c":
        print("Usted ganó")   
    elif c == "d":
        print ("La piedra aplastó al lagarto, ganó")
    elif c == "e" :
        print("la piedra fue destruida por spock, perdió")
        
elif seleccion == "papel":
    if c == "a" :
        print("La máquina ganó")
    elif c == "b":
       print("Empate ")
    elif c == "c":
        print("Usted ganó")
    elif c == "d":
        print ("El lagartó se comió el papel, perdió")
    elif c == "e" :
        print("El papel desaprueba a Spock, ganó")

elif seleccion == "tijera":
    if c == "a":
       print("usted ganó")
    elif c == "b":
        print("ganó la máquina")
    elif c == "c":
        print ("Empate")
    elif c == "d":
        print ("Las tijeras decapitaron al lagarto, ganó")
    elif c == "e":
        print("Spock destruyó las tijeras, perdió")

elif seleccion == "lagarto":
    if c == "a":
       print("El lagarto fue aplastado por la piedra, ganó")
    elif c == "b":
        print("El lagaro se comió el papel, perdió")
    elif c == "c":
        print ("Las tijeras decapitaron al lagarto, ganó")
    elif c == "d":
        print ("Empate")
    elif c == "e" :
        print("El lagarto envenenó a spock, perdió")

elif seleccion == "spock":
    if c == "a":
       print("La piedra fue destruida por Spock, perdió ")
    elif c == "b":
        print("El papel desaprueba a Spock, ganó")
    elif c == "c":
        print ("Spock destruyó las tijeras, perdió")
    elif c == "d":
        print ("Spock fue envenenado, ganó")
    elif c == "e" :
        print("Empate")