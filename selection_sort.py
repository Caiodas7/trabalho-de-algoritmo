# Algoritmos de Ordenação em Python

# 1. Selection Sort
#✅ Vantagens:
#Fácil de entender e implementar.
#Não precisa de memória extra (funciona no próprio array).
#❌ Desvantagens:
#Muito lento para listas grandes (demora em média O(n²)).

def selection_sort(lista):
    # Percorre cada posição da lista, de 0 até o último índice
    for i in range(len(lista)):
        # Assume que o menor valor está na posição i
        indice_menor = i

        # Compara esse valor com os outros valores à frente
        for j in range(i + 1, len(lista)):
            # Se encontrar um valor menor, atualiza o índice do menor
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        # Troca o valor atual (posição i) com o menor valor encontrado
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    # Retorna a lista já ordenada
    return lista

valores = [5, 3, 8, 1, 2]
ordenado = selection_sort(valores)
print(ordenado)