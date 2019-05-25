
while True:

    titulo= "VERIFICADOR DE NUMERO PRIMO"
    soma = 0
    print("=" *80)
    print(titulo.center(70))
    print("=" *80)
    num = int(input(" Digite um número "))
    
    i=1
    count = 0
    count2 = 0
    
    while i <= num:
        ver = num % i
        
        if ver == 0:
            print("divisor")
            count = count+i
            count2 += 1
            
            print(i)
            
        i+=1
       
    if count2 > 2:
        print(f"\n {num} não é um número primo")
    else:
        print(f"\n{num} é um número  primo")

    
