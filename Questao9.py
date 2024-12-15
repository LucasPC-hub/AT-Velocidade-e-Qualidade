class Perfil:
    def __init__(self, username, nome):
        self.username = username
        self.nome = nome


class HashTable:
    def __init__(self, tamanho=10):
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, key):
        return sum(ord(c) for c in key) % len(self.tabela)

    def inserir(self, perfil):
        indice = self.hash(perfil.username)
        self.tabela[indice].append(perfil)

    def buscar(self, username):
        indice = self.hash(username)
        for perfil in self.tabela[indice]:
            if perfil.username == username:
                return perfil
        return None


def testar_buscas():
    ht = HashTable()

    perfis = [
        Perfil("joao123", "João Silva"),
        Perfil("maria456", "Maria Santos"),
        Perfil("pedro789", "Pedro Souza"),
        Perfil("ana321", "Ana Oliveira")
    ]
    for perfil in perfis:
        ht.inserir(perfil)

    # Testes de busca
    testes = [
        "joao123",  # Existe
        "maria456",  # Existe
        "usuario404",  # Não existe
        "ana321",  # Existe
        ""  # Vazio
    ]

    for username in testes:
        resultado = ht.buscar(username)
        print(f"Busca '{username}': {resultado.nome if resultado else 'Não encontrado'}")


testar_buscas()