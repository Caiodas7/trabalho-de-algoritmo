'''📌 Ideia principal:
Pensa como se você estivesse organizando cartas na mão: você pega uma por uma e coloca na posição correta, comparando com as anteriores.
A parte da lista à esquerda vai ficando ordenada.
A cada passo, pegamos um novo número e o inserimos no lugar certo na parte já ordenada.

✅ Vantagens:
Muito eficiente para listas pequenas ou quase ordenadas.
Estável (mantém a ordem de elementos iguais).
Simples de entender e programar.

❌ Desvantagens:
Fica lento com listas grandes (tempo médio O(n²)). '''


def insertion_sort(lista):
    # Começamos do segundo elemento (índice 1), pois o primeiro já está "ordenado"
    for i in range(1, len(lista)):
        chave = lista[i]  # Este é o valor que queremos posicionar corretamente
        j = i - 1

        # Move todos os valores maiores que a chave uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]  # Move o valor maior para frente
            j -= 1  # Vai olhando o próximo valor à esquerda

        # Agora que achamos o lugar certo, colocamos a chave ali
        lista[j + 1] = chave

    return lista



valores = [5, 2, 4, 1]

# Primeira passada (i = 1): chave = 2
# Compara com 5 → 2 < 5 → move 5 pra frente → [5, 5, 4, 1]
# Insere 2 → [2, 5, 4, 1]

# Segunda passada (i = 2): chave = 4
# Compara com 5 → 4 < 5 → move 5 pra frente → [2, 5, 5, 1]
# Compara com 2 → 4 > 2 → insere 4 ali → [2, 4, 5, 1]

# Terceira passada (i = 3): chave = 1
# Move 5, depois 4, depois 2 → insere 1 no começo → [1, 2, 4, 5]

ordenado = insertion_sort(valores)
print(ordenado)  # Saída: [1, 2, 4, 5]