titulo= "GERADOR DE TABUADA"
soma = 0
print("=" *80)
print(titulo.center(70))
print("=" *80)



tabuada = int(input(" qual tabuada quer responder? "))

pontos = 0
questao = 1
while questao < tabuada :
    valor = questao*tabuada
    resposta = input ( " %s  X %s = " % (questao , tabuada))
    
