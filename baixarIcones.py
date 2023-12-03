import os, shutil, requests, zipfile, time
from tqdm import tqdm

def baixar_e_extrair_icones():
    # URL do repositório
    url = "https://github.com/lhrp/iconesBase/archive/refs/heads/main.zip"
    
    # Nome do arquivo compactado
    nome_arquivo = "iconesBase.zip"
    
    # Nome da pasta de destino
    pasta_destino = "imagens"
    
    # Realiza o download do arquivo compactado
    response = requests.get(url)
    with open(nome_arquivo, "wb") as file:
        file.write(response.content)
    
    # Extrai os arquivos do arquivo compactado
    with zipfile.ZipFile(nome_arquivo, "r") as zip_ref:
        zip_ref.extractall(pasta_destino)
    
    # Remove o arquivo compactado
    os.remove(nome_arquivo)
    
    # Remove os arquivos README.md e .gitattributes da pasta extraída
    readme_path = os.path.join(pasta_destino, "iconesBase-main", "README.md")
    gitattributes_path = os.path.join(pasta_destino, "iconesBase-main", ".gitattributes")
    os.remove(readme_path)
    os.remove(gitattributes_path)
    
    # Copia os arquivos da pasta extraída para a primeira pasta imagens
    imagens_path = os.path.join(pasta_destino, "iconesBase-main", "imagens")
    for file_name in tqdm(os.listdir(imagens_path)):
        time.sleep(0.02)
        file_path = os.path.join(imagens_path, file_name)
        shutil.copy(file_path, pasta_destino)
    
    # Remove as demais pastas
    shutil.rmtree(os.path.join(pasta_destino, "iconesBase-main"))
  
    print("Download, extração e organização concluídos com sucesso!")

# Chamada da função
baixar_e_extrair_icones()
