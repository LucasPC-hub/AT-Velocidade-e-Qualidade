import time
import random


class HashTable:
    def __init__(self, tamanho=1024):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, valor):
        return hash(valor) % self.tamanho

    def adicionar(self, valor):
        indice = self._hash(valor)
        if not self.contem(valor):
            self.tabela[indice].append(valor)

    def contem(self, valor):
        indice = self._hash(valor)
        return valor in self.tabela[indice]


def encontrar_duplicatas_original(lista):
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicatas:
                duplicatas.append(lista[i])
    return duplicatas


def encontrar_duplicatas_hashtable(lista):
    elementos_vistos = HashTable()
    duplicatas = []
    for elemento in lista:
        if elementos_vistos.contem(elemento):
            if elemento not in duplicatas:
                duplicatas.append(elemento)
        else:
            elementos_vistos.adicionar(elemento)
    return duplicatas


tamanho = 100000
lista_teste = [random.randint(1, 1000) for _ in range(tamanho)]

# Medir tempo - versão original
inicio = time.time()
encontrar_duplicatas_original(lista_teste)
tempo_original = time.time() - inicio

# Medir tempo - versão hashtable
inicio = time.time()
encontrar_duplicatas_hashtable(lista_teste)
tempo_hashtable = time.time() - inicio

print(f"Tempo de execução (Original): {tempo_original:.4f} segundos")
print(f"Tempo de execução (Otimizado): {tempo_hashtable:.4f} segundos")
print(f"Melhoria: {(tempo_original / tempo_hashtable):.2f}x mais rápido")