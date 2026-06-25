from pathlib import Path
import shutil
def read_Numbers():
    current_file = Path.cwd() /"list_Numbers.txt"
    target_Folder = Path.cwd() / "Web_Scraping_Documents/"
    with open(current_file,'r', encoding= 'utf-8') as file:
        
        for linha in file:
            try:
                if linha.strip().isdigit():
                    print(f"{linha.strip()}")
                        
                else: 
                    int(linha)
                    continue
            #OU
            #
            #    numero = int(linha)
            #    print(numero)
            except ValueError:
                print("Não é dígito")
    try:
        caminho_destino = target_Folder / current_file.name

        if current_file.exists() and not caminho_destino.exists():
            shutil.copy(current_file, target_Folder)
            print(f"Ficheiro copiado para {target_Folder}")
        else:
            print("ficheiro já existe")
    except PermissionError:
        print("Sem permissão! Necssário privilégios administrativos")
if __name__ == "__main__":
    read_Numbers()