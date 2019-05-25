titulo= "FORMAÇÃO DE UMA EQUAÇÃO DO 2º GRAU"
soma = 0
print("==" *40)
print(titulo.center(70))
print("==" *40)
	


while True:
    
    print(" Digite os coeficientes a,b e c com respectivos\n sinais para formar uma equação do 2º grau\n\n")

    a = input(" coeficiente a :")
    b = input(" coeficiente b :")
    c = input(" coeficiente c :")



    if a != "0":

        
        
        if a == "0" and b == "0" and c == "0":
            print("==" *40)
            print (f" Isto não é uma equação do 2º grau, favor digitar corretamente!")
            print("==" *40)
            
        elif b == "0":
            print("==" *40)
            print (f" A equação do 2º grau formada com estes coeficiente é:  {a}x²{c} \n EQUAÇÃO INCOMPLETA")
            print("==" *40)
            
        elif c == "0":
            print("==" *40)
            print (f" A equação do 2º grau formada com estes coeficiente é:  {a}x²{b}x \n EQUAÇÃO INCOMPLETA")
            print("==" *40)

        

        else:    
            print("==" *40)    
            print (f" A equação do 2º grau formada com estes coeficiente é: {a}x²{b}x{c} \n " )
            print("==" *40)

            
    else:

        print("==" *40)
        print ( f" A equação  formada com estes coeficiente é:  {b}x{c} \n É UMA EQUAÇÃO DO 1º GRAU") 
        print("==" *40)
