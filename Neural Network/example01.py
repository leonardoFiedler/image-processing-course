# Author: Leonardo Fiedler
# Cada habilidade de jogador/piloto e classe
# Habilidades: Ciencia, Fisica, Filosofia.
# Classes: 0 - Jogador
#          1 - Piloto

neymar = [1, 0, 0, 0]
messi = [1, 0, 1, 0]
barrichelo = [1, 1, 0, 1]
massa = [1, 1, 1, 1]

def funcao_ativacao(soma):
    if soma >= 1:
        return 1
    else:
        return 0

arr = [neymar, messi, barrichelo, massa]
# Vetor de peso para cada habilidade
peso = [0, 0, 0]
processados = []

while True:
    for player in arr:
        soma = 0
        for i in range(3):
            soma += player[i] * peso[i]

        if (funcao_ativacao(soma) == player[3]):
            print("Pertence a classe %i" % (player[3]))
        else:
            processados.append(player)
            # se a soma e 0, adiciona os pesos
            if soma == 0:
                for j in range(len(peso)):
                    peso[j] += player[j]
            else:
                # senao a soma deve subtrair os pesos
                for j in range(len(peso)):
                    peso[j] -= player[j]
            print("Não pertence a classe %i" % (player[3]))
    if len(processados) > 0:
        processados = []
        continue
    else:
        break

testes = [[0, 0, 0],[0, 0, 1],[0, 1, 0],[0, 1, 1]]

print("Testes")
for teste in testes:
    soma = 0
    for i in range(3):
        soma += teste[i] * peso[i]

    print("Pertence a classe %i" % (funcao_ativacao(soma)))
