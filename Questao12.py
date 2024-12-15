import os


def listar_arquivos(diretorio):
    try:
        conteudo = os.listdir(diretorio)

        for item in conteudo:
            caminho_completo = os.path.join(diretorio, item)

            if os.path.isdir(caminho_completo):
                listar_arquivos(caminho_completo)
            elif os.path.isfile(caminho_completo):
                print(f"Arquivo encontrado: {caminho_completo}")

    except PermissionError:
        print(f"Sem permissão para acessar: {diretorio}")
    except Exception as e:
        print(f"Erro ao acessar {diretorio}: {str(e)}")


# Caminho para pasta PS3
caminho_inicial = "/home/lc/Ps3"
listar_arquivos(caminho_inicial)