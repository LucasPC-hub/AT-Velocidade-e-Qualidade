def selection_sort_jogadores(jogadores):
    n = len(jogadores)
    # Percorre a lista n-1 vezes
    for i in range(n - 1):
        # Encontra o índice do maior valor no restante da lista
        indice_maior = i
        for j in range(i + 1, n):
            # Compara pontuações
            if jogadores[j]['pontos'] > jogadores[indice_maior]['pontos']:
                indice_maior = j
        # Troca os elementos se necessário
        if indice_maior != i:
            jogadores[i], jogadores[indice_maior] = jogadores[indice_maior], jogadores[i]

    return jogadores

jogadores = [
    {'nome': 'João', 'pontos': 85},
    {'nome': 'Maria', 'pontos': 92},
    {'nome': 'Pedro', 'pontos': 78},
    {'nome': 'Ana', 'pontos': 95}
]

print("Lista original:")
for j in jogadores:
    print(f"{j['nome']}: {j['pontos']} pontos")

jogadores_ordenados = selection_sort_jogadores(jogadores)

print("\nLista ordenada:")
for j in jogadores_ordenados:
    print(f"{j['nome']}: {j['pontos']} pontos")