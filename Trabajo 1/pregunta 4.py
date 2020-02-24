# distancia minima

x0=eval(input("ingrese la abcisa inicial: "))
y0=eval(input("ingrese la ordenada inicial:"))

x1=eval(input("ingrese la segunda abcisa: "))
y1=eval(input("ingrese la segunda ordenada:"))

x2=eval(input("ingrese la tercera abcisa: "))
y2=eval(input("ingrese la tercera ordenada:"))

x3=eval(input("ingrese la cuarta abcisa: "))
y3=eval(input("ingrese la cuarta ordenada:"))

x4=eval(input("ingrese la quinta abcisa: "))
y4=eval(input("ingrese la quinta ordenada:"))

d1=(x0-x1)**2+(y0-y1)**2
d2=(x0-x2)**2+(y0-y2)**2
d3=(x0-x3)**2+(y0-y3)**2
d4=(x0-x4)**2+(y0-y4)**2

if d1<=d2 and d1<=d3 and d1<=d4:
    print("la mas cerca a la primera es la segunda: ")
else:
    if d2<=d1 and d2<=d3 and d2<=d4:
        print("la mas cerca a la primera es la tercera: ")
    else:
        if d3<=d1 and d3<=d2 and d3<=d4:
            print("la mas cercana a la primera es la cuarta: ")
        else:
            print("la mas cercana a la primera es la quinta: ")