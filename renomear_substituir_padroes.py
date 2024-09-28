import os
from colorama import init, Fore, Style, Back

def limpar():
    os.system("cls")

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

def get_total_matching_files(directory, pattern):
    # Retorna o total de arquivos que combinam com o padrão
    return sum(1 for filename in os.listdir(directory) if pattern in filename)

def batch_rename(directory, old_text, new_text):
    placeholder = "_-_TEMP_-_" + old_text
    total_matching = get_total_matching_files(directory, old_text)
    total_renamed = 0
    total_failed = 0
    total_global = 0

    if old_text == "":
        print("Você não forneceu um padrão. O programa será encerrado.")
        return None
    
    # caso que vc tá só convertendo maiúsculas/minúsculas (mesma palavra)
    if old_text.lower() == new_text.lower():
    # Primeiro passo: renomear para o placeholder
        for filename in os.listdir(directory):
            if old_text in filename:
                old_file = os.path.join(directory, filename)
                temp_file = os.path.join(directory, filename.replace(old_text, placeholder))
                os.rename(old_file, temp_file)

        # Segundo passo: renomear do placeholder para o novo texto
        for filename in os.listdir(directory):
            if placeholder in filename:
                temp_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, filename.replace(placeholder, new_text))
                
                if os.path.exists(new_file):
                    total_failed += 1
                    total_global += 1
                    print(f"{total_global}.\t{Back.RED} FALHA {Style.RESET_ALL}:\n'{Fore.RED}{os.path.basename(old_file)}{Style.RESET_ALL}' para '{Fore.RED}{os.path.basename(new_file)}{Style.RESET_ALL}' (porque já existia um arquivo com este nome)")
                    print("Ambos foram mantidos como estavam")
                    print()
                    continue
                
                os.rename(temp_file, new_file)
                total_renamed += 1
                total_global += 1
                print(f"{total_global}.\t{Fore.GREEN}Renomeado{Style.RESET_ALL}:\n'{Fore.GREEN}{os.path.basename(old_file)}{Style.RESET_ALL}' para '{Fore.GREEN}{os.path.basename(new_file)}{Style.RESET_ALL}'")
                print()

    # caso em que haverá substituição de padrão
    elif old_text != new_text:
        # Navegar pelo diretório especificado
        for filename in os.listdir(directory):
            if old_text in filename:
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, filename.replace(old_text, new_text))

                if os.path.exists(new_file):
                    total_failed += 1
                    total_global += 1
                    print(f"{total_global}.\t{Back.RED} FALHA {Style.RESET_ALL}:\n'{Fore.RED}{os.path.basename(old_file)}{Style.RESET_ALL}' para '{Fore.RED}{os.path.basename(new_file)}{Style.RESET_ALL}' (porque já existia um arquivo com este nome)")
                    print("Ambos foram mantidos como estavam")
                    print()
                    continue

                os.rename(old_file, new_file)
                total_renamed += 1
                total_global += 1
                print(f"{total_global}.\t{Fore.GREEN}Renomeado{Style.RESET_ALL}:\n'{Fore.GREEN}{os.path.basename(old_file)}{Style.RESET_ALL}' para '{Fore.GREEN}{os.path.basename(new_file)}{Style.RESET_ALL}'")
                print()       


    # Resultado final
    print("------------------------------------")
    print(f"Total de ocorrências do padrão: {Fore.CYAN}{total_matching}{Style.RESET_ALL}")
    print(f"Total de renomeados: {Fore.GREEN}{total_renamed}{Style.RESET_ALL}")
    print(f"Total de falhas: {Fore.RED}{total_failed}{Style.RESET_ALL}")
    print("------------------------------------")

def main():
    limpar()

    print(f"{Fore.MAGENTA}Bem-vindo ao Renomeador de Arquivos!{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Este script substitui um padrão especificado (por outro padrão), atingindo todos os arquivos e diretórios em um caminho fornecido.{Style.RESET_ALL}\n")
    
    directory = input("Digite o caminho absoluto da pasta onde estão os arquivos: ")

    if not os.path.isdir(directory):
        print()
        print(f"{Fore.RED}O diretório fornecido não existe. Por favor, verifique e tente novamente.{Style.RESET_ALL}")
        print()
        return
    
    list_directory_contents(directory)

    # Definição do que será renomeado
    print()
    old_text = input("[OBRIGATÓRIO] Digite o padrão atual: ")
    total_files = len(os.listdir(directory))
    total_matching = get_total_matching_files(directory, old_text)
    if old_text == "":
        print()
        print(f"{Fore.RED}Você não forneceu um padrão. O programa será encerrado.{Style.RESET_ALL}")
        print()
        return None
    print(f"Total de itens na pasta: {Fore.CYAN}{total_files}{Style.RESET_ALL}")
    print(f"Total de ocorrências do padrão: {Fore.CYAN}{total_matching}{Style.RESET_ALL}")
    print()
    new_text = input("Digite o novo padrão: ")
    print("------------------------------------")
    print()

    batch_rename(directory, old_text, new_text)

if __name__ == "__main__":
    main()
