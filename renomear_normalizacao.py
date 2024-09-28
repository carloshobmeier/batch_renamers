import os
from colorama import Fore, Style, Back, init

init(autoreset=True)

def normalize_name(name, to_replace, replacements):
    original_name = name
    for old, new in zip(to_replace, replacements):
        name = name.replace(old, new)
    return name, original_name

def highlight_changes(original, new):
    highlighted = ""
    for o, n in zip(original, new):
        if o != n:
            highlighted += f"{Back.YELLOW}{o}{Style.RESET_ALL}"
        else:
            highlighted += o
    return highlighted

def collect_changes(path, to_replace, replacements, recursive):
    changes = []
    if recursive:
        for root, dirs, files in os.walk(path, topdown=False):  # Process directories after their contents
            for file_name in files:
                new_name, original_name = normalize_name(file_name, to_replace, replacements)
                if new_name != file_name:
                    highlighted_name = highlight_changes(original_name, new_name)
                    changes.append((os.path.join(root, file_name), os.path.join(root, new_name), highlighted_name))
            for dir_name in dirs:
                new_name, original_name = normalize_name(dir_name, to_replace, replacements)
                if new_name != dir_name:
                    highlighted_name = highlight_changes(original_name, new_name)
                    changes.append((os.path.join(root, dir_name), os.path.join(root, new_name), highlighted_name))
    else:
        # Handle only files in the given directory, ignore subdirectories
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                new_name, original_name = normalize_name(entry, to_replace, replacements)
                if new_name != entry:
                    highlighted_name = highlight_changes(original_name, new_name)
                    changes.append((full_path, os.path.join(path, new_name), highlighted_name))
    return changes

def main():
    path = input("Informe o caminho para normalização: ")
    recursive = input("Deseja fazer uma busca recursiva? (s/n): ").lower() == 's'
    to_replace = [" ", 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'À', 'È', 'Ì', 'Ò', 'Ù', 'à', 'è', 'ì', 'ò', 'ù', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'â', 'ê', 'î', 'ô', 'û', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'Ã', 'Õ', 'Ñ', 'ã', 'õ', 'ñ', 'Ç', 'ç', 'Ā', 'ē', 'ī', 'ō', 'ū']
    replacements = ["_", 'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'O', 'N', 'a', 'o', 'n', 'C', 'c', 'A', 'e', 'i', 'o', 'u']

    changes = collect_changes(path, to_replace, replacements, recursive)
    
    if changes:
        print("\nArquivos/diretórios a serem renomeados:")
        for original, new, highlighted in changes:
            print(f"{highlighted}")
        print(f"\nTotal de itens a serem renomeados: {len(changes)}\n")
        if input("Deseja proceder com a renomeação? (s/n): ").lower() == 's':
            for original, new, _ in changes:
                os.rename(original, new)
            print("\nRenomeação concluída.\n")
        else:
            print("\nRenomeação cancelada.\n")
    else:
        print("\nNenhum item precisa ser renomeado.\n")

if __name__ == "__main__":
    main()
