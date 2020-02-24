#pregunta 1b
nu=int(input("ingrese el número codificado (4 cifas):"))

a=int((nu-(nu%1000))/1000)
b=int((nu%1000)/100)
c=int((nu%100)/10)
d=nu%10


if a>=0 and a<=6:
    a1=a+3
else:
        a1=a-7


if b >= 0 and b <= 6:
    b1 = b + 3
else:
    b1=b-7


if c >= 0 and c <= 6:
    c1 = c + 3
else:
    c1=c-7


if d >= 0 and d <= 6:
    d1 = d + 3
else:
    d1=d-7


mm=c1*1000+d1*100+a1*10+b1
print("el número decodificado es", mm)