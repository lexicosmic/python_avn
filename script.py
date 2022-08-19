# Visualização de dados em Python

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Título
plt.title("Meu primeiro grafico com Python")

# Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()
