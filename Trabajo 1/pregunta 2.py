#pregunta 2
print("usted tiene 500000 de saldo")
saldo=eval(input("¿cual es el valor de la compra?:"))



if saldo>500000:
    inv=0.55*saldo
    pres=0.3*saldo
    cre=500000-inv+pres
    inte=cre*0.2

    print("Se invertirá: ",inv)
    print("Se prestará: ",pres)
    print("El credito es: ",cre)
    print("El interes perdido es:", inte)

else:
    inv = 0.75 * saldo
    pres = 0.25 * saldo
    cre = 500000 - inv + pres
    inte = cre * 0.2

    print("Se invertirá: ", inv)
    print("Se prestará: ", pres)
    print("El credito es: ", cre)
    print("El interes perdido es:", inte)