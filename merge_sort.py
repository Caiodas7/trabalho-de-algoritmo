'''📌 Ideia principal:
O Merge Sort é um algoritmo dividir para conquistar:
Divide a lista no meio várias vezes até restarem listas com apenas 1 elemento.
Intercala (junta) essas pequenas listas em ordem, formando uma lista maior já ordenada.

✅ Vantagens:
Muito rápido: tempo garantido de O(n log n).
Estável (mantém a ordem de valores iguais).
Funciona bem com listas grandes.

❌ Desvantagens:
Usa mais memória (cria muitas listas novas durante o processo).
Mais difícil de entender e implementar para iniciantes.'''

def merge_sort(lista):
    # Caso base: se a lista tiver 1 ou nenhum elemento, já está ordenada
    if len(lista) <= 1:
        return lista

    # Encontra o meio da lista
    meio = len(lista) // 2

    # Divide a lista em duas metades
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Chama recursivamente o merge_sort para as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Junta (intercala) as duas metades ordenadas
    return intercalar(esquerda, direita)


def intercalar(esq, dir):
    resultado = []
    i = j = 0

    # Enquanto houver elementos nas duas listas:
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # Se ainda sobrar elementos em uma das listas, adiciona ao final
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    return resultado



valores = [8, 3, 5, 1]

# Divide em [8, 3] e [5, 1]
# Divide [8, 3] em [8] e [3] → intercala: [3, 8]
# Divide [5, 1] em [5] e [1] → intercala: [1, 5]
# Agora intercala [3, 8] com [1, 5] → resultado final: [1, 3, 5, 8]

ordenado = merge_sort(valores)
print(ordenado)  # Saída: [1, 3, 5, 8]
