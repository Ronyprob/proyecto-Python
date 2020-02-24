#pregunta 1
nu=eval(input("ingrese el número (4 cifas):"))
n1=nu//1000
n2=(nu-n1*1000)//100
n3=(nu-n1*1000-n2*100)//10
n4=nu-n1*1000-n2*100-n3*10

n11=(n1+7)%10
n22=(n2+7)%10
n33=(n3+7)%10
n44=(n4+7)%10
nn=n33*1000+n44*100+n11*10+n22
print("el número codificado es",nn)