# -*- coding: utf-8 -*-


#graficos em linhas com titulos

import matplotlib.pyplot as plt

x = [0,1, 2, 3]
y = [0,5, 1, 10]
#legenda do grafico / titulo
plt.title("Primeiro Grafico em linhas 00")

#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#parametros x e y 
#grafico em linha
plt.plot(x, y)

#exibir o grafico
plt.show()