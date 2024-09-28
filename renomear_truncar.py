import os

def truncar_nomes_arquivos(diretorio, limite_caracteres):
    # Lista todos os arquivos no diretório fornecido
    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        
        # Verifica se é um arquivo para evitar truncar diretórios
        if os.path.isfile(caminho_completo):
            # Extrai a extensão do arquivo para manter após a truncagem
            nome_base, extensao = os.path.splitext(arquivo)
            
            # Trunca o nome base se necessário
            if len(nome_base) > limite_caracteres:
                nome_base_truncado = nome_base[:limite_caracteres]
                novo_nome = nome_base_truncado + extensao
                novo_caminho = os.path.join(diretorio, novo_nome)
                
                # Verifica se o novo nome já existe e ajusta para evitar duplicação
                contador = 1
                while os.path.exists(novo_caminho):
                    novo_nome = f"{nome_base_truncado}_{contador}{extensao}"
                    novo_caminho = os.path.join(diretorio, novo_nome)
                    contador += 1

                # Renomeia o arquivo
                os.rename(caminho_completo, novo_caminho)
                print(f"Renomeado: '{arquivo}' para '{novo_nome}'")
            else:
                print(f"Nenhum nome truncado necessário para: {arquivo}")

# Solicita ao usuário o diretório e o limite de caracteres
diretorio_usuario = input("Digite o caminho do diretório: ")
limite_caracteres_usuario = int(input("Digite o limite de caracteres para os nomes dos arquivos: "))

# Chama a função de truncar nomes de arquivos
truncar_nomes_arquivos(diretorio_usuario, limite_caracteres_usuario)
