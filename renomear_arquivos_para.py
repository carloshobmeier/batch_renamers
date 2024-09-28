import os
from colorama import init, Style, Fore

init(autoreset=True)

def listar_arquivos(diretorio):
    # Lista todos os arquivos no diretório fornecido
    arquivos = os.listdir(diretorio)
    arquivos_para_renomear = []

    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_completo):
            arquivos_para_renomear.append(arquivo)
    
    return arquivos_para_renomear

def renomear_arquivos(diretorio, novo_padrao, arquivos):
    cont = 1
    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        extensao = os.path.splitext(arquivo)[1]
        novo_nome = f"{novo_padrao}_{cont}{extensao}"
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(caminho_completo, novo_caminho)
        print(f"Renomeado: {Fore.RED}'{arquivo}'{Style.RESET_ALL} para {Fore.GREEN}'{novo_nome}'")
        cont += 1

# Solicita ao usuário o diretório
diretorio_usuario = input("\nDigite o caminho do diretório: ")
arquivos_para_renomear = listar_arquivos(diretorio_usuario)

# Lista os arquivos e mostra o total
print("\nArquivos a serem renomeados:")
for arquivo in arquivos_para_renomear:
    print(f"{Fore.YELLOW}{arquivo}")
print(f"\nTotal de arquivos a serem alterados: {Fore.BLUE}{len(arquivos_para_renomear)}\n")

# Solicita o novo padrão se houver arquivos para renomear
if arquivos_para_renomear:
    novo_padrao_usuario = input("Digite o novo padrão de nome para os arquivos: ")
    renomear_arquivos(diretorio_usuario, novo_padrao_usuario, arquivos_para_renomear)
else:
    print("Nenhum arquivo para renomear.")
