import os
from colorama import Fore, Style, init, Back

# Inicializa o Colorama
init(autoreset=True)

def destacar_caracteres(nome, caracteres_para_substituir):
    """ Retorna uma versão do nome onde os caracteres a substituir são destacados em vermelho. """
    for caractere in caracteres_para_substituir:
        if caractere in nome:
            nome = nome.replace(caractere, f'{Style.BRIGHT}{Back.YELLOW}{Fore.RED}{caractere}{Style.RESET_ALL}')
    return nome

def renomear_recursivo(diretorio, caracteres_para_substituir, substitutos):
    total = 0
    # Exibe uma prévia dos arquivos e diretórios que serão renomeados
    mudancas = []
    for raiz, dirs, arquivos in os.walk(diretorio, topdown=False):
        for nome in arquivos + dirs:
            novo_nome = nome
            for original, substituto in zip(caracteres_para_substituir, substitutos):
                novo_nome = novo_nome.replace(original, substituto)
            if nome != novo_nome:  # Mostra apenas se o nome for alterado
                caminho_completo = os.path.join(raiz, nome)
                novo_caminho_completo = os.path.join(raiz, novo_nome)
                mudancas.append((caminho_completo, novo_caminho_completo))
                print(destacar_caracteres(caminho_completo, caracteres_para_substituir), f'{Fore.GREEN}->{Style.RESET_ALL}', novo_nome)
                total += 1

    print(f'Total a ser renomeado: {total}')

    # Pergunta ao usuário se deseja continuar com a renomeação
    resposta = input('Quer continuar? [sim, não]: ')
    if resposta.lower() == 'sim':
        # Processa as mudanças após confirmação
        for caminho_original, novo_caminho in mudancas:
            os.rename(caminho_original, novo_caminho)

# Exemplo de uso
diretorio_usuario = input("Digite o caminho do diretório: ")
caracteres_para_substituir = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç', 'Ã', 'Á', 'À', 'Â', 'Ä', 'Ê', 'É', 'È', 'Ë', 'Ì', 'Î', 'Ï', 'Í', 'Ú', 'Ù', 'Ü', 'Û', 'Õ', 'Ó', 'Ò', 'Ô', 'Ö']
substitutos =                ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'ã', 'á', 'à', 'â', 'ä', 'ê', 'é', 'è', 'ë', 'ì', 'î', 'ï', 'í', 'ú', 'ù', 'ü', 'û', 'õ', 'ó', 'ò', 'ô', 'ö']

renomear_recursivo(diretorio_usuario, caracteres_para_substituir, substitutos)


