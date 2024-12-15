class No:
    def __init__(self, preco):
        self.preco = preco
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, preco):
        if self.raiz is None:
            self.raiz = No(preco)
        else:
            self._inserir_recursivo(self.raiz, preco)

    def _inserir_recursivo(self, no_atual, preco):
        if preco < no_atual.preco:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(preco)
            else:
                self._inserir_recursivo(no_atual.esquerda, preco)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(preco)
            else:
                self._inserir_recursivo(no_atual.direita, preco)

    def buscar(self, preco):
        return self._buscar_recursivo(self.raiz, preco)

    def _buscar_recursivo(self, no_atual, preco):
        if no_atual is None or no_atual.preco == preco:
            return no_atual

        if preco < no_atual.preco:
            return self._buscar_recursivo(no_atual.esquerda, preco)
        return self._buscar_recursivo(no_atual.direita, preco)



arvore = ArvoreBinaria()
precos = [100, 50, 150, 30, 70, 130, 170]

print("Inserindo os preços:", precos)
for preco in precos:
    arvore.inserir(preco)


preco_busca = 70
resultado = arvore.buscar(preco_busca)
print(f"\nBuscando o preço R$ {preco_busca}:")
if resultado:
    print(f"Preço R$ {preco_busca} encontrado!")
else:
    print(f"Preço R$ {preco_busca} não encontrado.")