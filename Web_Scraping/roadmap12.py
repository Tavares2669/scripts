#Começar a usar o select invés do find e find_all, 
#O select é mais flexível e poderoso, permitindo usar seletores CSS para acessar elementos específicos. 
#Ele pode selecionar elementos com base em classes, IDs, atributos e hierarquia, tornando-o ideal para extrair dados de páginas web complexas. 
#O select retorna uma lista de elementos que correspondem ao seletor fornecido, facilitando a extração de informações específicas de uma página web.
#O find e find_all são métodos mais simples que permitem acessar elementos com base em tags e atributos, mas não oferecem a mesma flexibilidade que o select.
from bs4 import BeautifulSoup
import requests
import csv

url1 = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
}

csv_file = "Web_Scraping_Documents_CSV/books.csv"
def extract_product_titles(url1):
    response = requests.get(url1, headers=headers)
    try:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.select("article.product_pod > h3 > a")
        posicao_do_livro_especifico = None
        print("Products:")

        for idx, product in enumerate(products, start=1):
            print(f"{idx} - {product['title'].strip()}")
            titulo = product['title'].strip()
            if titulo == "Tipping the Velvet":
                posicao_do_livro_especifico = idx
        print(f"Specific Product:\n {posicao_do_livro_especifico}- {titulo}")

        livros = soup.select("article.product_pod")
        with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Price","URL"])
            for livro  in livros:
                link_tag = livro.select_one("h3 > a")
                preco_tag = livro.select_one("div.product_price > p.price_color")
                titulo = link_tag['title'].strip()
                preco = preco_tag.text.strip().replace("Â", "")
                url_livro = url1 + link_tag['href']

                writer.writerow([titulo, preco, url_livro])
        print("Ficheiro criado com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the page. Status code: {e}")
extract_product_titles(url1)