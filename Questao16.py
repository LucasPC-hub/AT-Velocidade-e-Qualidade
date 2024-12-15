class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
            return
        atual = self.raiz
        while True:
            if valor < atual.valor:
                if not atual.esquerda:
                    atual.esquerda = No(valor)
                    break
                atual = atual.esquerda
            else:
                if not atual.direita:
                    atual.direita = No(valor)
                    break
                atual = atual.direita

    def remover(self, valor):
        def min_valor(no):
            atual = no
            while atual.esquerda:
                atual = atual.esquerda
            return atual.valor

        def remover_rec(no, valor):
            if not no: return None

            if valor < no.valor:
                no.esquerda = remover_rec(no.esquerda, valor)
            elif valor > no.valor:
                no.direita = remover_rec(no.direita, valor)
            else:
                if not no.esquerda: return no.direita
                if not no.direita: return no.esquerda
                no.valor = min_valor(no.direita)
                no.direita = remover_rec(no.direita, no.valor)
            return no

        self.raiz = remover_rec(self.raiz, valor)

    def em_ordem(self):
        def percorrer(no, nums):
            if no:
                percorrer(no.esquerda, nums)
                nums.append(no.valor)
                percorrer(no.direita, nums)
            return nums

        return percorrer(self.raiz, [])


# Teste
arvore = Arvore()
for num in [45, 25, 65, 20, 30, 60, 70]:
    arvore.inserir(num)

print(arvore.em_ordem())  # Original
arvore.remover(20)
print(arvore.em_ordem())
arvore.remover(25)
print(arvore.em_ordem())
arvore.remover(45)
print(arvore.em_ordem())