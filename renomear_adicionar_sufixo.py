import os
from colorama import init, Fore, Style

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)  # Para resetar a cor automaticamente após cada print

def list_directory_contents(directory):
    # Listar todos os arquivos e pastas no diretório
    print(f"Conteúdo da pasta em questão:")
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"{Fore.YELLOW}[Pasta]   {item}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}[Arquivo] {item}{Style.RESET_ALL}")

def add_suffix_to_files(directory, suffix):
    total_files = len(os.listdir(directory))
    total_renamed = 0

    # Navegar pelo diretório especificado
    for filename in os.listdir(directory):
        old_file = os.path.join(directory, filename)
        # Extrair a extensão do arquivo para adicionar o sufixo antes dela
        name, ext = os.path.splitext(filename)
        new_file = os.path.join(directory, name + suffix + ext)

        # Renomear o arquivo ou diretório
        os.rename(old_file, new_file)
        total_renamed += 1
        print(f"{Fore.GREEN}Renomeado:{Style.RESET_ALL} '{Fore.GREEN}{os.path.basename(old_file)}{Style.RESET_ALL}' para '{Fore.GREEN}{os.path.basename(new_file)}{Style.RESET_ALL}'")

    # Resultado final
    print("------------------------------------")
    print(f"Total de itens na pasta: {Fore.CYAN}{total_files}{Style.RESET_ALL}")
    print(f"Total de renomeados: {Fore.GREEN}{total_renamed}{Style.RESET_ALL}")
    print("------------------------------------")

def main():
    limpar()

    print(f"{Fore.MAGENTA}Bem-vindo ao Renomeador de Arquivos!{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Este script adiciona um sufixo especificado a todos os arquivos e diretórios em um caminho fornecido.{Style.RESET_ALL}\n")

    directory = input(f"Digite o caminho absoluto da pasta onde estão os arquivos: ")

    list_directory_contents(directory)

    if not os.path.isdir(directory):
        print(f"{Fore.RED}O diretório fornecido não existe. Por favor, verifique e tente novamente.{Style.RESET_ALL}")
        return

    # Solicitar ao usuário o sufixo a ser adicionado
    print()
    suffix = input(f"Digite o sufixo que deseja adicionar aos arquivos e diretórios: ")
    print("------------------------------------")
    print()

    add_suffix_to_files(directory, suffix)

if __name__ == "__main__":
    main()
