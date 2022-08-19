# Crescimento da população brasileira 1980-2016
# DataSUS

import matplotlib.pyplot as plt

dados = open("est_caso_01/populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

# Gráfico
titulo = "Crescimento da população brasileira 1980-2016"
eixox = "Ano"
eixoy = "População x100.000.000"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y, color="#E4E4E4")
plt.plot(x, y, color="k", linestyle="--")
# plt.scatter(x, y, color="k", s=20)
plt.show()
# plt.savefig("populacao_brasileira.png", dpi=300)
