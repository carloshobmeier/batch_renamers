import os
from colorama import init, Back, Fore, Style

# Inicializa o Colorama
init(autoreset=True)

def listar_itens(caminho, recursivo=False):
    itens_listados = []
    try:
        if recursivo:
            for raiz, dirs, arquivos in os.walk(caminho, topdown=False):  # topdown=False para renomear de dentro para fora
                for nome in dirs:
                    itens_listados.append(os.path.join(raiz, nome))
                for nome in arquivos:
                    itens_listados.append(os.path.join(raiz, nome))
        else:
            for nome in os.listdir(caminho):
                caminho_completo = os.path.join(caminho, nome)
                if os.path.isfile(caminho_completo):
                    itens_listados.append(caminho_completo)
        return itens_listados
    except FileNotFoundError:
        print("Caminho não encontrado.")
        return []

def renomear_itens(caminho, caracteres, inicio, recursivo):
    itens = listar_itens(caminho, recursivo)
    itens_para_renomear = []

    print("\nItens encontrados:")
    for item in itens:
        nome_completo = os.path.basename(item)
        if os.path.isdir(item) and not recursivo:
            continue  # Pula diretórios se não estiver no modo recursivo
        extensao = os.path.splitext(nome_completo)[1] if os.path.isfile(item) else ''
        nome_base = os.path.splitext(nome_completo)[0]

        # Ajuste para índice baseado em zero
        inicio_ajustado = inicio - 1
        parte_para_excluir = nome_base[inicio_ajustado:inicio_ajustado + caracteres]
        nome_renomeado = nome_base[:inicio_ajustado] + nome_base[inicio_ajustado + caracteres:] + extensao
        novo_caminho = os.path.join(os.path.dirname(item), nome_renomeado)
        itens_para_renomear.append((item, novo_caminho))

        # Exibição destacando o trecho a ser excluído
        print(f"{nome_base[:inicio_ajustado]}{Back.YELLOW}{parte_para_excluir}{Back.RESET}{nome_base[inicio_ajustado + caracteres:]}{extensao}")

    return itens_para_renomear

def confirmar_renomeacao(itens_para_renomear):
    print(f"\nNúmero de itens a serem renomeados: {len(itens_para_renomear)}")
    resposta = input("Deseja confirmar a renomeação dos itens? (s/n): ").strip().lower()
    return resposta == 's'

def renomear_itens_no_diretorio(itens_para_renomear):
    for original, novo in itens_para_renomear:
        os.rename(original, novo)
        print(f"{Fore.RED}{os.path.basename(original)}{Style.RESET_ALL} → {Fore.GREEN}{os.path.basename(novo)}{Style.RESET_ALL}")

def main():
    caminho = input("Digite o caminho dos itens: ").strip()
    caracteres = int(input("Quantos caracteres deseja excluir? "))
    inicio = int(input("A partir de qual caracter deseja começar a contar? "))
    recursivo = input("Deseja aplicar de forma recursiva? (s/n): ").strip().lower() == 's'

    itens_para_renomear = renomear_itens(caminho, caracteres, inicio, recursivo)

    if itens_para_renomear:
        if confirmar_renomeacao(itens_para_renomear):
            renomear_itens_no_diretorio(itens_para_renomear)
            print("Itens renomeados com sucesso!")
        else:
            print("Renomeação cancelada.")
    else:
        print("Nenhum item encontrado para renomear.")

if __name__ == "__main__":
    main()
