import asyncio
from playwright.async_api import async_playwright
from roadmap18 import atualizar_json

async def scraping(tab1):
    try:
        pesquisa_title = tab1.locator(".titleline > a")
        primeiros_titulos = await pesquisa_title.all()
        headlines = primeiros_titulos[:5]
        lista = []
        contador_id=0
        for headline in headlines:
            titulo = await headline.inner_text()
            link = await headline.get_attribute("href")
            contador_id+=1
            if not titulo:
                titulo = "N/A"
            if not link:
                link = "N/A"
                
            dicionario = {
                "id":contador_id,
                "headline": titulo,
                "link" : link
            }
            lista.append(dicionario)
        return lista
    except Exception as e:
        print(f"Erro durante a extração: {e}")
        return []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        tab1 = await context.new_page()
        await tab1.goto("https://news.ycombinator.com/")
        
        ficheiro_json_extraido = await scraping(tab1)
        await browser.close()

        print("\nA processar os dados para o cofre JSON...")
        for noticia in ficheiro_json_extraido:
            atualizar_json(noticia)

if __name__ == "__main__":
    asyncio.run(main())