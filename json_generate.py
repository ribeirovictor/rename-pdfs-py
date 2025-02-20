import os
import json

def gerar_json_arquivos(diretorio):
  """Gera um arquivo JSON com os nomes dos arquivos em um diretório.

  Args:
    diretorio: Caminho completo do diretório.
  """

  # Lista para armazenar os nomes dos arquivos
  lista_arquivos = []

  # Iterar sobre os arquivos no diretório
  for arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, arquivo)
    if os.path.isfile(caminho_completo):
      lista_arquivos.append(arquivo)

  # Criar o arquivo JSON
  with open('files.json', 'w') as arquivo_json:
    json.dump(lista_arquivos, arquivo_json, indent=4)

# Solicitar o caminho do diretório ao usuário
diretorio = input("Digite o caminho do diretório: ")

# Chamar a função para gerar o JSON
gerar_json_arquivos(diretorio)

print("JSON gerado com sucesso!")