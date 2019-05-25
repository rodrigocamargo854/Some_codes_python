n=int(input(" digite um número"))
k = 1
a = 1
b = 1
lista = []
while b <= n: # while b less than n
    a,b = b,a+b # make a and b equal a b and a+b
    
    lista.append(b)# add in lista [ ]
    
fibo1 = lista[-3]# made a variable to input index of lista -3
fibo2 = lista[-4]# made a variable to input index of lista -4    

if n not in lista: 
    
    print(" this number dont be included in fibonacci sequence ")
else:
    print (" the fibonatti  numbers wich build this number are %s and %s "%(fibo1,fibo2))




    
    
    
    
    
