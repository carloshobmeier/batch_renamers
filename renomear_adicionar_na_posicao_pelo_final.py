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

def inserir_texto_em_arquivos(caminho, texto, posicao_do_final):
    arquivos = listar_arquivos(caminho)
    arquivos_para_modificar = []

    print("\nPreview da modificação dos nomes dos arquivos:")
    for arquivo in arquivos:
        nome_completo = os.path.join(caminho, arquivo)
        nome_sem_caminho = os.path.basename(nome_completo)
        extensao = os.path.splitext(nome_sem_caminho)[1]
        nome_base = os.path.splitext(nome_sem_caminho)[0]

        # Ajustar a posição para base-1 e calcular a nova posição a partir do final do nome base
        posicao_insercao = len(nome_base) - posicao_do_final + 1
        parte_inicial = nome_base[:posicao_insercao]
        parte_final = nome_base[posicao_insercao:]

        nome_modificado = parte_inicial + texto + parte_final + extensao
        arquivos_para_modificar.append((nome_sem_caminho, nome_modificado))

        # Exibição com a parte inserida destacada
        print(f"{parte_inicial}{Back.YELLOW}{texto}{Back.RESET}{parte_final}{extensao}")
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
        print(f"{Fore.RED}{original}{Style.RESET_ALL} → {Fore.GREEN}{modificado}{Style.RESET_ALL}")

def main():
    caminho = input("Digite o caminho dos arquivos: ").strip()
    posicao = int(input("Em qual posição do final (sem considerar a extensão) deseja inserir o texto? "))
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
