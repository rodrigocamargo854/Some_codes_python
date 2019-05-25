
titulo= " GERADOR DE TABUADA"
soma = 0
print("==" *40)# caracteres para decoração
print(titulo.center(70))#centraliza o titulo
print("==" *40)# caracteres para decoração



while True:
    
    tabuada = int(input(" qual tabuada quer responder? "))
    i = 1
    while i <=20 :
        valor = tabuada*i
        print( " %s  X %s = %s " % (tabuada , i , valor))
    
        i+= 1
    


