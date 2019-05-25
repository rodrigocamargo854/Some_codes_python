import sys
from termcolor import colored, cprint
import time 
import random 

while True:
    
    print("="*40)
    print(" JOGO JUNKENPO - AUTOR -- dougras")
    print("="*40)


    a = int(input(" Digite \n\n 0 pedra \n 1 para  papel \n 2 para tesoura\n"))

    if a == 0 :
        a = "pedra"

    elif a == 1:
        a = "papel"
        
    elif a == 2 :
        a = "tesoura"
        
    print (" Você escolheu %s" %(a))
       
    b = random.randint(0,2)

    if b == 0 :
        b = "pedra"

    elif b == 1:
        b = "papel"
        
    elif b == 2 :
        b = "tesoura"
    print (" Eu escolhi %s" %(b))

    for i in range (0,5):
        print("-")
        time.sleep(0.1)

    if a == b:
        print( " Deu empate")
        
    elif a < b:
        print (" você venceu")

    elif a > b:
        print(" PERDEU!")

    
    



    






    
