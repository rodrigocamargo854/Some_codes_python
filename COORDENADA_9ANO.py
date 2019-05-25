

titulo= "GERADOR DO GRÁFICO DE UMA FUNÇÃO"
soma = 0
print("=" *80)
print(titulo.center(70))
print("=" *80)


import matplotlib.pyplot as grafico

x = []
y =[]

num = int(input(" Digite numero de coordenadas para x e para y\n"))
for i in range (0,num):
  coodx = int(input(" digite a coordenada para x\n"))
  x.append (coodx)
  coody = int(input(" digite a coordenads para y\n"))
  y.append (coody)
  

grafico.plot(x,y)

grafico.title(" Coordenadas Cartesianas Interativas")

grafico.show()
