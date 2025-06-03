'''📌 Ideia principal:
Também usa o método dividir para conquistar, como o Merge Sort, mas de um jeito diferente:
Escolhe um pivô (um valor qualquer da lista).
Coloca todos os menores que o pivô à esquerda, e os maiores à direita.
Repete esse processo nas duas partes separadamente (recursão).

✅ Vantagens:
Muito rápido na prática, com tempo médio O(n log n).
Funciona bem em listas grandes.
Usa pouca memória (mais eficiente que Merge Sort).

❌ Desvantagens:
No pior caso (lista já ordenada), pode ficar O(n²).
Não é estável (pode mudar a ordem de elementos iguais).
Usa recursão, que pode ser difícil para iniciantes.'''

def quick_sort(lista):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(lista) <= 1:
        return lista

    # Escolhe o pivô (aqui usamos o último elemento da lista)
    pivo = lista[-1]

    # Listas para separar os menores e maiores que o pivô
    menores = []
    maiores = []

    # Percorre todos os elementos menos o pivô
    for elemento in lista[:-1]:
        if elemento <= pivo:
            menores.append(elemento)
        else:
            maiores.append(elemento)

    # Chama o quick_sort nas partes e junta tudo
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


valores = [6, 2, 7, 3]

# Pivô = 3
# Menores = [2]
# Maiores = [6, 7]
# Chamada recursiva:

# quick_sort([2]) → [2]
# quick_sort([6, 7]):
#   Pivô = 7 → menores = [6] → maiores = []
#   → quick_sort([6]) + [7] + [] → [6, 7]

# Resultado final: [2] + [3] + [6, 7] → [2, 3, 6, 7]

ordenado = quick_sort(valores)
print(ordenado)  # Saída: [2, 3, 6, 7]
