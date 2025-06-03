'''📌 Ideia principal:
O Counting Sort conta quantas vezes cada número aparece e usa essa contagem para montar a lista ordenada.

✅ Vantagens:
Muito rápido para listas com números pequenos e inteiros positivos.
Complexidade de tempo: O(n + k), onde k é o maior número.
Não usa comparação.

❌ Desvantagens:
Não funciona com números negativos (sem adaptação).
Gasta muita memória se o maior número for muito alto.
Não é eficiente para dados muito dispersos (ex: [1, 10000]).
'''

def counting_sort(lista):
    if not lista:
        return lista  # Lista vazia já está ordenada

    # 1. Encontra o maior valor da lista
    max_valor = max(lista)

    # 2. Cria uma lista de contagem com zeros (índices de 0 até max_valor)
    contagem = [0] * (max_valor + 1)

    # 3. Conta quantas vezes cada número aparece
    for numero in lista:
        contagem[numero] += 1

    # 4. Reconstrói a lista ordenada com base nas contagens
    index = 0
    for numero, qtd in enumerate(contagem):
        for _ in range(qtd):
            lista[index] = numero
            index += 1

    return lista


valores = [4, 2, 2, 8, 3, 3, 1]

# max_valor = 8 → cria contagem de 9 posições (0 a 8)
# contagem: [0, 1, 2, 2, 1, 0, 0, 0, 1]
# → tem 1 vez o 1, 2 vezes o 2, 2 vezes o 3, etc.

# Reconstrói:
# lista = [1, 2, 2, 3, 3, 4, 8]

ordenado = counting_sort(valores)
print(ordenado)  # Saída: [1, 2, 2, 3, 3, 4, 8]
