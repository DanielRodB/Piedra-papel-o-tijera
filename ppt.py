print("Escribe una de las letras correspondientes para jugar piedra, papel o tijera contra la máquina")
print("a) piedra")
print("b) papel")
print("c) tijera")
import random
opciones = ("piedra" , "papel" , "tijera")
c = input ()
if c == ("a") : print ("Eligió piedra, la máquina jugará con: ") 
if c == ("b") : print ("Eligió papel, la máquina jugará con: ")
if c == ("c") : print ("Eligió tijera, la máquina jugará con: ")
seleccion = random.choice(opciones) 
print(seleccion)
if seleccion== "piedra": 
    if c == "a":
        print("Empate")
    elif c == "b": 
        print("La máquina ganó") 
    elif c == "c" :
        print("Usted ganó")   
elif seleccion == "papel":
    if c == "a" :
        print("La máquina ganó")
    elif c == "b":
       print("Empate ")
    elif c == "c":
        print("Usted ganó")
elif seleccion == "tijera":
    if c == "a":
       print("usted ganó")
    elif c == "b":
        print("ganó la máquina")
    elif c == "c":
        print ("nadie ganó")

