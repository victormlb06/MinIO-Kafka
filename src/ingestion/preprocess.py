import json
import config
import os

from config import DOWNLOAD_PATH

# Criação do diretório de processamento, caso não exista
os.makedirs(config.PROCESSED_PATH, exist_ok=True)

# Caminho completo para os arquivos JSON
DOWNLOAD_PATH_COMPLETE = f'{config.DOWNLOAD_PATH}/topics/articles/partition=0/'
print(DOWNLOAD_PATH_COMPLETE)


def extract_titles():
    """ Lê os artigos, extrai os títulos e salva um JSON separado para cada resultado """
    for file in os.listdir(DOWNLOAD_PATH_COMPLETE):
        file_path = os.path.join(DOWNLOAD_PATH_COMPLETE, file)

        if file.endswith(".json"):  # Suporte para JSON
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Para cada artigo dentro do arquivo JSON
                for index, article in enumerate(data.get('results', [])):
                    article_data = {
                        "uri": article.get("uri"),
                        "url": article.get("url"),
                        "source": article.get("source"),
                        "published_date": article.get("published_date"),
                        "section": article.get("section"),
                        "subsection": article.get("subsection"),
                        "nytdsection": article.get("nytdsection"),
                        "adx_keywords": article.get("adx_keywords"),
                        "byline": article.get("byline"),
                        "title": article.get("title"),
                        "abstract": article.get("abstract"),
                        "des_facet": article.get("des_facet")
                    }

                    # Definindo o nome do arquivo com base no número do arquivo e índice do artigo
                    output_filename = f"article_{file.split('/')[-1].replace('.json', '')}_index_{index}.json"
                    output_path = os.path.join(config.PROCESSED_PATH, output_filename)

                    # Salvando o artigo individualmente
                    with open(output_path, "w", encoding="utf-8") as out_file:
                        json.dump(article_data, out_file, ensure_ascii=False, indent=4)
                    print(f"Resultado salvo em: {output_path}")


# Iniciar o processo de extração e salvamento
extract_titles()
