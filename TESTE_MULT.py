from random import randint
import time
import os

    
mult = 0
count = 0

def tempo():

    i = 30
    while i > 0:
        i -= 1
        t = time.sleep(1)
        print (i)
        



        

titulo= "DESAFIO MULTIPLICAÇÃO"
print("=" *80)
print(titulo.center(70))
print("=" *80)




while True:



    def tempo ():
        for a in range (10,-1,-1):
            print(a)
            time.sleep(1)
        


    tabuada = int(input(" DIGITE 0 PARA COMEÇAR OU QUALQUER OUTRO NÚMERO PARA SAIR: "))

    if tabuada == 0 :
        
        i = 1
        while i <= 10:
            
            num = randint(-10,+10)
            num2 = randint(-10,+10)
            mult = num+num2

            prep = print("Questão %d : Valor de (%d)+(%d) : " %(i,num,num2))
            tempo()
            resp = int(input(" resposta: "))
            
            if resp == mult:
                count = count +1
            
            i+=1
            
            
    

    print (" Você fez %d pontos!!\n\n"%(count))



    if tabuada == 1:
        print ("FIM DO PROGRAMA")




    


    
    
            

    

    
