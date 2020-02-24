# ejercicio 3
saldo=eval(input("¿cual es su capital actual?:"))
if saldo < 0:
    print("su saldo es negativo\n se procederá a realizar un prestamo")
    nsaldo=10000-saldo
    print("se solicitará un prestamo de ",nsaldo)
    print("se destinará:")
    print("5000 para cómputo")
    print("2000 para mobiliario")
    print("1500 para insumos e incentivos para el personal")
    print("aún queda 1500")
else:
    if saldo>=0 and saldo<20000:
        nnsaldo=20000-saldo
        print("se solicitará un prestamo de ", nnsaldo)
        print("se destinará:")
        print("5000 para cómputo")
        print("2000 para mobiliario")
        print("6500 para insumos e incentivos para el personal")
        print("aún queda 6500")

    else:
        nnn=(saldo-7000)/2
        print("no se realizará prestamo al banco")
        print("se destinará:")
        print("5000 para cómputo")
        print("2000 para mobiliario")
        print(nnn, "para insumos e incentivos para el personal")
        print("aún queda ",nnn)