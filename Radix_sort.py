'''📌 Ideia principal:
O Radix Sort ordena os números dígito por dígito, começando do dígito menos significativo (das unidades para a esquerda). Ele usa um algoritmo de ordenação estável, como o Counting Sort, para cada posição decimal.

✅ Vantagens:
Muito eficiente para números inteiros grandes com dígitos pequenos.

Complexidade: O(d × (n + k)), onde:
d é o número de dígitos do maior número,
n é o número de elementos,
k é a base (geralmente 10 para números decimais).
Não faz comparações diretas entre os números.

❌ Desvantagens:
Só funciona bem com números inteiros e positivos.
Precisa de memória extra para cada dígito.
Pode ser mais lento que o QuickSort ou HeapSort em casos gerais.

'''

def counting_sort_por_digito(lista, casa_decimal):
    """
    Counting Sort modificado para ordenar com base em uma casa decimal específica.
    """
    n = len(lista)
    output = [0] * n          # Lista de saída (ordenada por esse dígito)
    contagem = [0] * 10       # Dez contadores (para dígitos de 0 a 9)

    # 1. Conta as ocorrências dos dígitos naquela casa (unidade, dezena, etc.)
    for numero in lista:
        digito = (numero // casa_decimal) % 10
        contagem[digito] += 1

    # 2. Soma acumulada para manter a ordem (estabilidade)
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    # 3. Constrói a saída de forma estável (de trás pra frente)
    for i in range(n - 1, -1, -1):
        digito = (lista[i] // casa_decimal) % 10
        output[contagem[digito] - 1] = lista[i]
        contagem[digito] -= 1

    # 4. Copia para a lista original
    for i in range(n):
        lista[i] = output[i]


def radix_sort(lista):
    """
    Ordena a lista usando o Radix Sort (base 10).
    """
    if not lista:
        return lista

    # Encontra o maior número para saber quantos dígitos há
    max_valor = max(lista)

    # Aplica o counting sort para cada casa decimal (unidade, dezena, centena, etc.)
    casa = 1
    while max_valor // casa > 0:
        counting_sort_por_digito(lista, casa)
        casa *= 10

    return lista


valores = [170, 45, 75, 90, 802, 24, 2, 66]

# 1ª rodada: casa = 1 (unidades) → ordena por: ..., 0, 2, 4, 5, 5, 6, 0, 2
# Resultado após unidades: [170, 90, 802, 2, 24, 45, 75, 66]

# 2ª rodada: casa = 10 (dezenas)
# Resultado: [802, 2, 24, 45, 66, 170, 75, 90]

# 3ª rodada: casa = 100 (centenas)
# Resultado final: [2, 24, 45, 66, 75, 90, 170, 802]

ordenado = radix_sort(valores)
print(ordenado)  # Saída: [2, 24, 45, 66, 75, 90, 170, 802]
