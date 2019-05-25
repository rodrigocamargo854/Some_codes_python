from random import randint
import time
import os

    
mult = 0
count = 0

def tempo():

    i = 60
    while i > 0:
        i -= 1
        t = time.sleep(1)
        print (i)
        



        

titulo= "DESAFIO TABUADA"
print("=" *80)
print(titulo.center(70))
print("=" *80)


while True:

    tabuada = int(input(" DIGITE 0 PARA COMEÇAR OU QUALQUER OUTRO NÚMERO PARA SAIR: "))

    if tabuada == 0 :
        
        for i in range (10):
            
            num = randint(0,100)
            num2 = randint(0,100)
            mult = num * num2

            resp = int (input(" Valor de %d x %d : " %(num,num2)))
            tempo()#arrumar

            if resp == mult:
                count += count +1

    print (" Você fez %d pontos!!\n"%(count))



    if tabuada == 1:
        print ("FIM DO PROGRAMA")




    


    
    
            

    

    
