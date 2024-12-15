contatos = [
    ("Maria Silva", "64992363507"),
    ("João Santos", "64988776655"),
    ("Ana Oliveira", "64999740377"),
    ("Pedro Costa", "6499010410"),
    ("Lucas Souza", "64999610810")
]


def buscar_contato(lista_contatos, nome_busca):
    for nome, telefone in lista_contatos:
        if nome.lower() == nome_busca.lower():
            return telefone

    return None

def mostrar_resultado (resultado_busca):
    if resultado_busca:
        print(f"Contato encontrado!")
        print(f"Nome: {nome_procurado}")
        print(f"Telefone: {resultado_busca}")
    else:
        print(f"Contato '{nome_procurado}' não encontrado.")

# Teste com um contato que existe
nome_procurado = "Ana Oliveira"
resultado = buscar_contato(contatos, nome_procurado)
mostrar_resultado(resultado)

# Teste com um contato que não existe
nome_procurado = "Roberto Alves"
resultado = buscar_contato(contatos, nome_procurado)
mostrar_resultado(resultado)