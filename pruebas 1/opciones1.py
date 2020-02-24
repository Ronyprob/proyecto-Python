# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:04:59 2020

@author: Admin-CTIC
"""

print("bienvenido")
print("figuras disponibles:")
print("a. cuadrado")
print("b. triangulo")
print("c. circulo")

k=input("elija alguna para el area: ")

if k=="a":
    lado=eval(input("ingrese el lado:"))
    res=lado**2
    print("la respuesta es: ", res)
else:
    if k=="b":
        altura=eval(input("ingrese la altura: "))
        base=eval(input("ingrese la base: "))
        res=base*altura/2
        print("la respuesta es: ", res)
    else:
        if k=="c":
            radio=eval(input("ingrese el radio: "))
            res=radio**2*3.14
            
            print("la respuesta es: ", res)
        else:
            print("las alternativas son (a,b,c)"












            if d >= 0 and d <= 6:
                d1 = d + 3
            else:
                d1 = d - 7
    
