class Navegador:
    def __init__(self):
        self.anterior = []
        self.posterior = []
        self.atual = None

    def ir_para(self, pagina):
        if self.atual:
            self.anterior.append(self.atual)
        self.atual = pagina
        self.posterior = []

    def voltar(self):
        if not self.anterior:
            return False
        self.posterior.append(self.atual)
        self.atual = self.anterior.pop()
        return True

    def avancar(self):
        if not self.posterior:
            return False
        self.anterior.append(self.atual)
        self.atual = self.posterior.pop()
        return True

    def mostrar_estado(self):
        print("\n=== Estado do Navegador ===")
        print(f"Histórico anterior: {self.anterior}")
        print(f"Página atual: {self.atual}")
        print(f"Histórico posterior: {self.posterior}")
        print("=" * 25)


def mostrar_menu():
    print("\n=== Navegador Simulado ===")
    print("1 - Navegar para nova página")
    print("2 - Voltar")
    print("3 - Avançar")
    print("4 - Mostrar estado atual")
    print("5 - Sair")
    print("=" * 23)


def executar_navegador():
    nav = Navegador()
    nav.ir_para("github.com")

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção (1-5): ").strip()

        print()

        if opcao == "1":
            pagina = input("Digite o endereço da página: ").strip()
            nav.ir_para(pagina)
            print(f"Navegando para: {pagina}")

        elif opcao == "2":
            if nav.voltar():
                print(f"Voltando para: {nav.atual}")
            else:
                print("Impossível voltar - Início do histórico")

        elif opcao == "3":
            if nav.avancar():
                print(f"Avançando para: {nav.atual}")
            else:
                print("Impossível avançar - Fim do histórico")

        elif opcao == "4":
            nav.mostrar_estado()

        elif opcao == "5":
            print("Encerrando navegador...")
            break

        else:
            print("Opção inválida! Tente novamente.")

        input("\nPressione ENTER para continuar...")
        print("\n" * 2)


if __name__ == "__main__":
    print("Bem-vindo ao Navegador Simulado!")
    executar_navegador()