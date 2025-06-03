'''📌 Ideia principal:
O Bucket Sort divide os elementos em "baldes" (buckets) com base em intervalos. Cada balde é ordenado separadamente (geralmente com Insertion Sort), e depois os baldes são reunidos em ordem.

✅ Vantagens:
Muito rápido para números com distribuição uniforme.
Ideal para números reais (decimais).
Complexidade média: O(n + k) (k = número de baldes).

❌ Desvantagens:
Precisa de conhecimento sobre a distribuição dos dados.
O desempenho piora se os dados não forem bem distribuídos.
Exige bastante memória (vários baldes).'''

def bucket_sort(lista):
    if not lista:
        return lista

    # 1. Cria baldes vazios (um para cada intervalo, ex: 0-0.1, 0.1-0.2, ...)
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # 2. Coloca cada elemento no balde correspondente
    for numero in lista:
        # Multiplica por 10 para saber em qual balde vai
        indice = int(numero * num_buckets)
        # Cuida do caso onde número == 1.0 (vai para o índice 10, que não existe)
        if indice == num_buckets:
            indice -= 1
        buckets[indice].append(numero)

    # 3. Ordena individualmente cada balde (com Insertion Sort, por exemplo)
    def insertion_sort(sublista):
        for i in range(1, len(sublista)):
            chave = sublista[i]
            j = i - 1
            while j >= 0 and sublista[j] > chave:
                sublista[j + 1] = sublista[j]
                j -= 1
            sublista[j + 1] = chave
        return sublista

    for i in range(num_buckets):
        buckets[i] = insertion_sort(buckets[i])

    # 4. Junta todos os baldes em uma única lista
    resultado = []
    for balde in buckets:
        resultado.extend(balde)

    return resultado


valores = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

# Cada número vai para um balde de 0.1 em 0.1:
# Exemplo: 0.23 → balde[2] (índice = int(0.23 * 10))

# Depois ordenamos cada balde e juntamos tudo:
# Resultado: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]

ordenado = bucket_sort(valores)
print(ordenado)  # Saída: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
