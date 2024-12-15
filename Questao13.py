def knapsack_dp(valores, pesos, capacidade):
    n = len(valores)

    dp = [[0 for x in range(capacidade + 1)] for x in range(n + 1)]

    # Preenche a tabela dp[][] de baixo para cima
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                # Máximo entre incluir ou não o item atual
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Retorna o valor máximo possível
    return dp[n][capacidade]



valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidade = 50

resultado = knapsack_dp(valores, pesos, capacidade)
print(f"Valor máximo: {resultado}")