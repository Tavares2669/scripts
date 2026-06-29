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
            json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
        print(f"NOVA ENTRADA: Guardado no disco!")
    else:
        print(f"DUPLICADO: O link '{link_da_noticia_nova}' já existe. Ignorado.")


if __name__ == "__main__":
    # Este código SÓ corre se executar python roadmap18.py diretamente.
    # Serve para testar se a máquina está boa, sem estragar o código principal.
    print("A testar o módulo de JSON isoladamente...")
    teste = {"headline": "Teste de Modulos", "link": "teste.com/1"}
    atualizar_json(teste)