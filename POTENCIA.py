
titulo= " GERADOR DE POTÊNCIA"
soma = 0
print("==" *40)# caracteres para decoração
print(titulo.center(70))#centraliza o titulo
print("==" *40)# caracteres para decoração



while True:
    
    potencia = int(input(" qual Base de potência quer saber o resultado? "))
    i = 1
    while i <= 20 :
        valor = potencia**i
        print( " %s elevado a %sº potência = %s " % (potencia , i , valor))
    
        i+= 1


