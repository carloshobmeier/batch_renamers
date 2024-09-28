import os
from colorama import init, Back, Style, Fore

# Inicializa o Colorama
init(autoreset=True)

def listar_itens(caminho, recursivo):
    itens_listados = []
    try:
        if recursivo:
            for raiz, dirs, arquivos in os.walk(caminho, topdown=False):  # Usar topdown=False para processar de dentro para fora
                for nome in arquivos:
                    itens_listados.append(os.path.join(raiz, nome))
                for nome in dirs:
                    itens_listados.append(os.path.join(raiz, nome))
        else:
            for nome in os.listdir(caminho):
                item_completo = os.path.join(caminho, nome)
                itens_listados.append(item_completo)
        return itens_listados
    except FileNotFoundError:
        print("Caminho não encontrado.")
        return []

def remover_caracter_final(itens):
    caracteres_removidos = ' _-'
    itens_para_renomear = []
    for item in itens:
        nome_original = os.path.basename(item)
        extensao = os.path.splitext(nome_original)[1] if os.path.isfile(item) else ''
        nome_base = os.path.splitext(nome_original)[0]

        original_length = len(nome_base)
        while nome_base and nome_base[-1] in caracteres_removidos:
            nome_base = nome_base[:-1]

        nome_modificado = nome_base + extensao
        if nome_modificado != nome_original:
            itens_para_renomear.append((item, os.path.join(os.path.dirname(item), nome_modificado)))
            removed_part = nome_original[len(nome_base):original_length]
            print(f"{nome_base}{Back.YELLOW}{removed_part}{Back.RESET}{extensao}")
        else:
            print(f"{nome_original} (sem alteração)")
    print()
    return itens_para_renomear

def confirmar_renomeacao(itens_para_renomear):
    print(f"\nNúmero de itens a serem renomeados: {len(itens_para_renomear)}")
    resposta = input("Deseja confirmar as mudanças nos nomes dos itens? (s/n): ").strip().lower()
    return resposta == 's'

def renomear_itens(itens_para_renomear):
    for original, modificado in itens_para_renomear:
        os.rename(original, modificado)
        print(f"{Fore.RED}{os.path.basename(original)}{Style.RESET_ALL} → {Fore.GREEN}{os.path.basename(modificado)}{Style.RESET_ALL}")

def main():
    caminho = input("Digite o caminho dos itens: ").strip()
    recursivo = input("Deseja aplicar de forma recursiva? (s/n): ").strip().lower()

    itens = listar_itens(caminho, recursivo == 's')
    itens_para_renomear = remover_caracter_final(itens)

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
