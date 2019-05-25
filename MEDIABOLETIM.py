while True:
    
    titulo= "CÁLCULO DA MÉDIA DE NOTAS"
    soma = 0
    print("==" *40)# caracteres para decoração
    print(titulo.center(70))#centraliza o titulo
    print("==" *40)# caracteres para decoração


    lista = [] #cria lista
    i = 0 # variavel para o contador
    soma = 0 # variavel de armazenamento
    num = float ( input (" Digite o número de notas para cálculo da média\n"))
                         
    while i < num:
                         
        valor = float(input(f"digite uma nota\n"))
        lista.append(valor)
        soma = float(soma + lista[i])
        i += 1
            
    print("A nota final no boletim é %6.2f" %(soma/i))

