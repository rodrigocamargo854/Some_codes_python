
lista=[]
num1=int(input( " digite um numero"))
lista.append(num1)
num2=int(input(" digite outro numero"))
lista.append(num2)
a= max(lista)
b= min(lista)
c = a%b
lista.append(c)


while lista[len(lista)-1] != 0:
    d = lista[len(lista)-2] % lista[len(lista)-1]
    lista.append(d)
print (" O Mdc entre %s e %s é %s " %(a,b,lista[len(lista)-2]))
    
    
    
    


