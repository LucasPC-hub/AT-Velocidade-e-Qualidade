import random
import time
from typing import List

def bubble_sort(arr: List[float]) -> List[float]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

precos_1k = [random.uniform(1.0, 1000.0) for _ in range(1000)]
precos_10k = [random.uniform(1.0, 1000.0) for _ in range(10000)]

# Teste com 1000 elementos
inicio = time.time()
bubble_sort(precos_1k.copy())
tempo_1k = time.time() - inicio
print(f"Tempo para 1000 elementos: {tempo_1k:.2f} segundos")

# Teste com 10000 elementos
inicio = time.time()
bubble_sort(precos_10k.copy())
tempo_10k = time.time() - inicio
print(f"Tempo para 10000 elementos: {tempo_10k:.2f} segundos")

print(f"\nRazão entre os tempos (10k/1k): {tempo_10k/tempo_1k:.2f}x")