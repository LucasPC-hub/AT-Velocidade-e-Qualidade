lista_livros = [f"ISBN-{i:06d}" for i in range(100000)]


def busca_binaria(lista, isbn_busca):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2

        if lista[meio] == isbn_busca:
            return iteracoes
        elif lista[meio] < isbn_busca:
            inicio = meio + 1
        else:
            fim = meio - 1

    return iteracoes


def busca_linear(lista, isbn_busca):
    iteracoes = 0
    for livro in lista:
        iteracoes += 1
        if livro == isbn_busca:
            return iteracoes
    return iteracoes



def comparar_buscas(isbn_procurado):
    iteracoes_binaria = busca_binaria(lista_livros, isbn_procurado)
    iteracoes_linear = busca_linear(lista_livros, isbn_procurado)

    print(f"Buscando o ISBN: {isbn_procurado}")
    print(f"Número de iterações na busca binária: {iteracoes_binaria}")
    print(f"Número de iterações na busca linear: {iteracoes_linear}")

# Teste com um ISBN que está no meio da lista
comparar_buscas("ISBN-050000")