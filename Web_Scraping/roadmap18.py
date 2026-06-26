import json
from pathlib import Path
 
def atualizar_json(novo_dicionario):
    ficheiro = Path.cwd() / "data.json"
    dados_existentes = []

    if ficheiro.exists():
        try:
            with open(ficheiro, mode="r", encoding="utf-8") as file:
                dados_existentes = json.load(file)
        except json.JSONDecodeError:
            dados_existentes = [] 
    
    link_da_noticia_nova = novo_dicionario["link"]
    ja_existe = False 
    for noticia_antiga in dados_existentes:
        if noticia_antiga["link"] == link_da_noticia_nova:
            ja_existe = True
            break
            
    if ja_existe == False:
        dados_existentes.append(novo_dicionario)
        with open(ficheiro, mode="w", encoding="utf-8") as file:
            # json.dump() pega na nossa lista e cospe-a para dentro do ficheiro
            # O indent=4 serve apenas para o texto ficar com quebras de linha bonitas
            # O ensure_ascii=False garante que os acentos (ç, ã) não ficam estragados
            json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
        print(f"Guardado no disco!")
    else:
        print(f"O link '{link_da_noticia_nova}' já existe. Ignorado.")

def usar_dados_do_json():
    ficheiro = Path.cwd() / "data.json"

    if not ficheiro.exists():
        print("Erro: O ficheiro data.json não foi encontrado!")
        return

    with open(ficheiro, mode="r", encoding="utf-8") as file:
        lista_de_noticias = json.load(file)

    print(f"Foram encontradas {len(lista_de_noticias)} notícias no ficheiro.\n")
    print("-" * 40)

    for noticia in lista_de_noticias:
        titulo = noticia["headline"]
        link = noticia["link"]
        print(f"Título: {titulo}")
        print(f"Link: {link}")
        print("-" * 40)

dicionario_1 = {"headline": "Robôs dominam o mundo", "link": "site.com/1"}
dicionario_2 = {"headline": "Mas humanos aprendem Python", "link": "site.com/2"}

atualizar_json(dicionario_1)
atualizar_json(dicionario_2)

usar_dados_do_json()