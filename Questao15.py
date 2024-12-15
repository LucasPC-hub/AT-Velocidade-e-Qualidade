class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def nota_minima(self):
        if not self.raiz:
            return None
        return self._encontrar_minimo(self.raiz)

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual.valor

    def nota_maxima(self):
        if not self.raiz:
            return None
        return self._encontrar_maximo(self.raiz)

    def _encontrar_maximo(self, no):
        atual = no
        while atual.direita:
            atual = atual.direita
        return atual.valor


notas = [85, 70, 95, 60, 75, 90, 100]
arvore = ArvoreBinaria()


for nota in notas:
    arvore.inserir(nota)

print(f"Nota mínima: {arvore.nota_minima()}")
print(f"Nota máxima: {arvore.nota_maxima()}")