import os
from colorama import init, Back, Style, Fore

# Inicializa o Colorama
init(autoreset=True)

def listar_itens(caminho, recursivo):
    itens_listados = []
    try:
        if recursivo:
            for raiz, dirs, arquivos in os.walk(caminho, topdown=False):
                for nome in dirs + arquivos:
                    itens_listados.append(os.path.join(raiz, nome))
        else:
            for nome in os.listdir(caminho):
                if os.path.isfile(os.path.join(caminho, nome)):  # Listar apenas arquivos na raiz
                    itens_listados.append(os.path.join(caminho, nome))
        return itens_listados
    except FileNotFoundError:
        print("Caminho não encontrado.")
        return []

def cortar_nome_arquivo(itens, substring):
    itens_para_renomear = []
    for item in itens:
        nome_original = os.path.basename(item)
        extensao = os.path.splitext(nome_original)[1]  # Extrair a extensão do arquivo
        nome_base = os.path.splitext(nome_original)[0]  # Extrair o nome base do arquivo

        index = nome_base.find(substring)
        if index != -1:
            nome_modificado = nome_base[:index] + extensao  # Adicionar a extensão ao nome modificado
            itens_para_renomear.append((item, os.path.join(os.path.dirname(item), nome_modificado)))

            # Exibição com o trecho removido destacado
            print(f"{nome_base[:index]}{Back.YELLOW}{nome_base[index:]}{Back.RESET}{extensao} → {nome_modificado}")
        else:
            print(f"{nome_original} (sem alteração)")
    print()
    return itens_para_renomear

def confirmar_renomeacao(itens_para_renomear):
    print(f"\nNúmero de itens a serem renomeados: {len(itens_para_renomear)}")
    resposta = input("\nDeseja confirmar as mudanças nos nomes dos itens? (s/n): ").strip().lower()
    return resposta == 's'

def renomear_itens(itens_para_renomear):
    for original, modificado in itens_para_renomear:
        os.rename(original, modificado)
        print(f"{Fore.RED}{os.path.basename(original)}{Style.RESET_ALL} → {Fore.GREEN}{os.path.basename(modificado)}{Style.RESET_ALL}")

def main():
    caminho = input("Digite o caminho dos itens: ").strip()
    recursivo = input("Deseja aplicar de forma recursiva? (s/n): ").strip().lower() == 's'
    substring = input("Digite o caractere ou substring a partir do qual deseja cortar o nome: ")

    itens = listar_itens(caminho, recursivo)
    itens_para_renomear = cortar_nome_arquivo(itens, substring)

    if itens_para_renomear:
        if confirmar_renomeacao(itens_para_renomear):
            renomear_itens(itens_para_renomear)
            print("Itens renomeados com sucesso!")
        else:
            print("Renomeação cancelada.")
    else:
        print("Nenhum item encontrado que necessite renomeação ou já formatado corretamente.")

if __name__ == "__main__":
    main()
