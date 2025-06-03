'''
✅ Vantagens:
# Muito fácil de entender.
# Estável (mantém a ordem de valores iguais).

❌ Desvantagens:
# Muito ineficiente para listas grandes (tempo de execução é O(n²)).'''

def bubble_sort(lista):
    n = len(lista)  # Guarda o tamanho da lista

    # Faz várias passagens pela lista
    for i in range(n):
        # A cada passagem, os maiores valores vão para o final

        # Este for percorre até n - i - 1, porque os últimos já estão ordenados
        for j in range(0, n - i - 1):
            # Compara dois elementos vizinhos
            if lista[j] > lista[j + 1]:
                # Se estão na ordem errada, troca de lugar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Retorna a lista ordenada
    return lista

valores = [4, 2, 7, 1]

# Primeira passada:
# [4, 2, 7, 1] → troca 4 e 2 → [2, 4, 7, 1]
# [2, 4, 7, 1] → troca 7 e 1 → [2, 4, 1, 7]

# Segunda passada:
# [2, 4, 1, 7] → troca 4 e 1 → [2, 1, 4, 7]

# Terceira passada:
# [2, 1, 4, 7] → troca 2 e 1 → [1, 2, 4, 7]

# Pronto!

ordenado = bubble_sort(valores)
print(ordenado)  # Saída: [1, 2, 4, 7]