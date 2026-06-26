import csv
import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

async def scraping(tab1):
    try:
        pesquisa_title = tab1.locator(".titleline > a")
        primeiros_titulos = await pesquisa_title.all()
        headlines = primeiros_titulos[:5]
        lista = []
        
        for headline in headlines:
            titulo = await headline.inner_text()
            link = await headline.get_attribute("href")

            if not titulo:
                print("Não há titulo")
                print("Título em falta, a inserir N/A.")
                titulo = "N/A"
            if not link:
                print("Link em falta, a inserir N/A.")
                link = "N/A"
            dicionario = {
                "headline": titulo,
                "link" : link
            }
            print(dicionario)
            lista.append(dicionario)
        return lista
    except Exception as e:
        print(f"Erro durante a extração: {e}")
        return []
async def main():
    ficheiro = Path.cwd() / "Web_Scraping_Documents_CSV"
    ficheiro.mkdir(parents=True, exist_ok=True)
    caminho_ficheiro = ficheiro / "scrapes.csv"

    headers = ["headline", "link"]
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        tab1 = await context.new_page()
        await tab1.goto("https://news.ycombinator.com/")
        
        ficheiro_csv = await scraping(tab1)
        await browser.close()

        precisa_cabecalho = not caminho_ficheiro.exists() or caminho_ficheiro.stat().st_size == 0
        with open(caminho_ficheiro, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers) 
            if precisa_cabecalho:
                writer.writeheader()   
            writer.writerows(ficheiro_csv)
            print("Criado")
asyncio.run(main())