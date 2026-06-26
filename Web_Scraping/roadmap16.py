from playwright.async_api import async_playwright
import asyncio

async def extrair_dados_livro(page, threshold):
    try:
        titulo = await page.locator("div > h1").inner_text()
        preco = await page.locator(".price_color").first.inner_text()
        preco_num = float(preco.replace("£",""))
        
        dados_livro = {
            "title": titulo,
            "price": preco_num,
            "cheap": preco_num < threshold
        }
        return dados_livro
    except Exception as e:
            print(f"Erro durante a extração: {e}")
            return []
async def main():
    async with async_playwright() as p:
        lista_livros = [
            "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
            "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
            "https://books.toscrape.com/catalogue/soumission_998/index.html"
        ]
        threshold =  50.5
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        for url in lista_livros:
            await page.goto(url)
            print("A extrair dados")

            esta_barato = await extrair_dados_livro(page,threshold)
            if esta_barato["cheap"] == True:
                print(f"Dentro da margem: Livro {esta_barato['title']}")
                print(f"Preço atual: £{esta_barato['price']} (O limite era £{threshold})")
            else:
                print(f"Demasiado caro: Livro {esta_barato['title']}")
                print(f"Preço atual: £{esta_barato['price']} (Ultrapassa o limite de £{threshold})")
            await asyncio.sleep(3)
asyncio.run(main())