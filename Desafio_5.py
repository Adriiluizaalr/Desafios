# Agora vamos dar uma relembrada na aula de funções, pegue o código do exercicio anterior e transfome numa função,
# essa função deve receber uma lista e dessa lista escolher algum nome e dar um print
# ou seja vocês vão precisar criar a função e depois "chamar" a mesma para que ela execute.

import random
def escolher_e_imprimir_nome(lista_de_nomes):
 nome_escolhido = random.choice(lista_de_nomes)
print(f"O nome escolhido foi: {nome_escolhido}")
nomes = ["Ana", "Bruno", "Carla", "Diogo", "Elena"]
escolher_e_imprimir_nome(nomes)
