class FilaAtendimento:
    def __init__(self):
        self.chamados = []

    def adicionar_chamado(self, chamado):
        self.chamados.append(chamado)
        return f"Chamado '{chamado}' adicionado à fila. Posição: {len(self.chamados)}"

    def atender_proximo(self):
        if len(self.chamados) == 0:
            return "Não há chamados na fila"
        return f"Atendendo chamado: {self.chamados.pop(0)}"

    def ver_proximo(self):
        if len(self.chamados) == 0:
            return "Não há chamados na fila"
        return f"Próximo chamado: {self.chamados[0]}"

    def tamanho_fila(self):
        return len(self.chamados)


fila = FilaAtendimento()


print(fila.adicionar_chamado("Problema com login"))
print(fila.adicionar_chamado("Sistema lento"))
print(fila.adicionar_chamado("Erro ao salvar"))

print(f"\nTamanho da fila: {fila.tamanho_fila()}")
print(f"Próximo a ser atendido: {fila.ver_proximo()}")

print("\nIniciando atendimentos:")
print(fila.atender_proximo())
print(fila.atender_proximo())
print(fila.atender_proximo())
print(fila.atender_proximo())