import os
from colorama import init, Back, Style, Fore

# Inicializa o Colorama
init(autoreset=True)

def listar_itens(caminho, recursivo):
    itens_listados = []
    try:
        if recursivo:
            for raiz, dirs, arquivos in os.walk(caminho, topdown=False):  # topdown=False para renomear de dentro para fora
                for nome in dirs + arquivos:
                    itens_listados.append(os.path.join(raiz, nome))
        else:
            for nome in os.listdir(caminho):
                itens_listados.append(os.path.join(caminho, nome))
        return itens_listados
    except FileNotFoundError:
        print("Caminho não encontrado.")
        return []

def remover_sublinhados_duplos(itens):
    itens_para_renomear = []
    for item in itens:
        nome_original = os.path.basename(item)
        nome_modificado = nome_original.replace('__', '_')  # Substitui sublinhados duplos por um único sublinhado
        while '__' in nome_modificado:  # Continua substituindo enquanto houver sublinhados duplos
            nome_modificado = nome_modificado.replace('__', '_')

        if nome_original != nome_modificado:
            itens_para_renomear.append((item, os.path.join(os.path.dirname(item), nome_modificado)))

            # Exibição com os sublinhados duplos destacados
            print(f"{nome_original.replace('__', Back.YELLOW + '__' + Back.RESET)} → {nome_modificado}")
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

    itens = listar_itens(caminho, recursivo)
    itens_para_renomear = remover_sublinhados_duplos(itens)

    if itens_para_renomear:
        if confirmar_renomeacao(itens_para_renomear):
            renomear_itens(itens_para_renomear)
            print("Itens renomeados com sucesso!")
        else:
            print("Renomeação cancelada.")
    else:
        print("Nenhum item encontrado para renomear ou já formatado corretamente.")

if __name__ == "__main__":
    main()
