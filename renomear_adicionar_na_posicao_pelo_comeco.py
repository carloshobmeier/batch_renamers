import os
from colorama import init, Back, Style, Fore

# Inicializa o Colorama
init(autoreset=True)

def listar_arquivos(caminho):
    try:
        arquivos = os.listdir(caminho)
        return arquivos
    except FileNotFoundError:
        print("Caminho não encontrado.")
        return []

def inserir_texto_em_arquivos(caminho, texto, posicao):
    arquivos = listar_arquivos(caminho)
    posicao -= 1  # Ajustar para zero-based index
    arquivos_para_modificar = []

    print("\nPreview da modificação dos nomes dos arquivos:")
    for arquivo in arquivos:
        nome_completo = os.path.join(caminho, arquivo)
        nome_sem_caminho = os.path.basename(nome_completo)
        parte_inicial = nome_sem_caminho[:posicao]
        parte_final = nome_sem_caminho[posicao:]
        nome_modificado = parte_inicial + texto + parte_final
        arquivos_para_modificar.append((nome_sem_caminho, nome_modificado))

        # Exibição com a parte inserida destacada
        print(f"{parte_inicial}{Back.YELLOW}{texto}{Back.RESET}{parte_final}")
    print()
    return arquivos_para_modificar

def confirmar_modificacao(arquivos_para_modificar):
    print(f"\nNúmero de arquivos a serem modificados: {len(arquivos_para_modificar)}")
    resposta = input("\nDeseja confirmar as mudanças nos nomes dos arquivos? (s/n): ").strip().lower()
    return resposta == 's'

def modificar_nomes_no_diretorio(caminho, arquivos_para_modificar):
    for original, modificado in arquivos_para_modificar:
        caminho_original = os.path.join(caminho, original)
        caminho_modificado = os.path.join(caminho, modificado)
        os.rename(caminho_original, caminho_modificado)
        print(f"{Fore.RED}{original}\n{Fore.GREEN}{modificado}\n")

def main():
    caminho = input("Digite o caminho dos arquivos: ").strip()
    posicao = int(input("Em qual posição deseja inserir o texto? "))
    texto = input("Digite o texto que deseja adicionar: ")

    arquivos_para_modificar = inserir_texto_em_arquivos(caminho, texto, posicao)

    if arquivos_para_modificar:
        if confirmar_modificacao(arquivos_para_modificar):
            modificar_nomes_no_diretorio(caminho, arquivos_para_modificar)
            print("Nomes dos arquivos modificados com sucesso!")
        else:
            print("Modificação cancelada.")
    else:
        print("Nenhum arquivo encontrado para modificar.")

if __name__ == "__main__":
    main()
