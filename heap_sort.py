'''📌 Ideia principal:
O Heap Sort usa uma estrutura chamada heap, que é uma árvore especial onde:
O maior (ou menor) valor está sempre no topo.
A árvore pode ser armazenada em uma lista, sem usar ponteiros.
No Heap Sort, a ideia é:
Transformar a lista em um max-heap (maior valor no topo).
Trocar o maior valor (no início) com o último da lista.
Reduzir o tamanho do heap e "reorganizar" (heapify).
Repetir até a lista estar ordenada.

✅ Vantagens:
Complexidade garantida: O(n log n) sempre.
Não precisa de muita memória extra (in-place).

❌ Desvantagens:
Não é estável (pode mudar a ordem de elementos iguais).
É um pouco mais difícil de implementar que os anteriores.

'''

def heapify(lista, n, i):
    """
    Transforma a subárvore com raiz em i em um heap (max-heap).
    """
    maior = i            # Assume que a raiz é o maior
    esquerda = 2 * i + 1 # Índice do filho da esquerda
    direita = 2 * i + 2  # Índice do filho da direita

    # Verifica se o filho da esquerda é maior que o atual maior
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica o filho da direita
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se o maior não é a raiz, troca e aplica o heapify na nova subárvore
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)


def heap_sort(lista):
    n = len(lista)

    # 1. Constrói um max-heap (começando do meio até o início)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # 2. Um por um, move o maior elemento para o fim da lista e reorganiza o heap
    for i in range(n - 1, 0, -1):
        # Troca o primeiro (maior) com o último
        lista[0], lista[i] = lista[i], lista[0]

        # Chama heapify para reorganizar o heap reduzido
        heapify(lista, i, 0)

    return lista



valores = [4, 10, 3, 5, 1]

# Cria max-heap → [10, 5, 3, 4, 1]
# Troca 10 com o último → [1, 5, 3, 4, 10]
# Reorganiza → [5, 4, 3, 1, 10]
# Troca 5 com o penúltimo → [1, 4, 3, 5, 10]
# Reorganiza → [4, 1, 3, 5, 10]
# Continua até lista ficar ordenada

ordenado = heap_sort(valores)
print(ordenado)  # Saída: [1, 3, 4, 5, 10]
