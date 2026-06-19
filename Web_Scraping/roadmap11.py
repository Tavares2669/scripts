from bs4 import BeautifulSoup

html_content = "<html><body><h1>Welcome</h1><p class='intro'>Data extraction is fun. <h1 class='title' >aaa</h1></p></body></html>"

# Initialize the parser
soup = BeautifulSoup(html_content, 'html.parser')

# Accessing a tag directly
h1_class = soup.find("h1",class_="title")

print(soup.h1.text) # Search by tag name finds the first occurrence of the tag
print(h1_class.text) # Search by class and tag name

print("="*50)

html = """
<html>
    <head>
        <title>Roadmap 11</title>
    </head>
    <body>
        <h1>Roadmap 11</h1>
        <p>MEU primeiro Web Scaper</p>
        <p>clicar com o botão direito do mouse em um elemento da página e selecionar Inspecionar para abrir as ferramentas de desenvolvimento do navegador. Isso permite ver o código 
            a e identificar as tags e classes que contêm as informações que desejamos.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </body>
</html>
"""
print("Achar as palavras dentro de uma ul e li")
soup = BeautifulSoup(html, 'html.parser')
find_text_ul = soup.find_all("li")
for li in find_text_ul:
    print(li.text)

print("="*50)
print("Colocar o src dentro de uma lista")

src_list = []

html1 = """
<html>
    <head>
        <title>Roadmap 11 - Imagens</title>
    </head>
    <body>
        <h1>Roadmap 11</h1>
        <p>MEU primeiro Web Scraper</p>
        
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>

        <h2>Galeria de Projetos</h2>
        <div class="galeria">
            <img src="https://site.com/foto1.jpg" alt="Gato a programar em Python">
            <img src="https://site.com/grafico.png" alt="Gráfico de Web Scraping">
            <img src="https://site.com/meme.gif" alt="Meme de erro 404">
        </div>
    </body>
</html>
"""
soup_src = BeautifulSoup(html1, 'html.parser')
imagens = soup_src.find_all('img', src=True)
for img in imagens:
    src_list.append(img['src'])
print(",\n".join(src_list))

print("="*50)
print("Pesquisar usando tags aninhadas")
html_aninhado = """
<html>
    <body>
        <h2>Estrutura Complexa</h2>
        
        <div class="caixa-principal">
            <p>Texto normal ignorado</p>
            <span class="foco">
                <a href="https://link-secreto.com" id="alvo">O Tesouro Escondido!</a>
            </span>
        </div>
        
    </body>
</html>
"""
chained_Soup = BeautifulSoup(html_aninhado, 'html.parser')
chained_Result = chained_Soup.find("div", class_="caixa-principal").find("span", class_= "foco").find("a", id = "alvo")
texto_link = chained_Result.text
print(f"O texto do link é: {texto_link}")

