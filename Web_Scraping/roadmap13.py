# https://playwright.dev/python/docs/input
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
'''def playwright_Wait():
    headline_list = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://news.ycombinator.com")
        page.wait_for_load_state("networkidle")

        headlines = page.locator("span.titleline").all()
        for headline in headlines[:10]:
            texto = headline.inner_text().strip()
            headline_list.append(texto)
            print(texto)

        print("First 10 Headlines")
        for idx,headline_text in enumerate(headline_list, start=1):
            print(f"{idx} - {headline_text}")
        browser.close()
playwright_Wait()
'''
async def automate_duckduckgo():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://duckduckgo.com")

        caixa_pesquisa = page.locator('[name="q"]')
        await caixa_pesquisa.fill("Python Playwright Web Scraping")

        await caixa_pesquisa.press('Enter')

        # Mandamos o Playwright esperar especificamente até esta "caixa" nascer no ecrã.
        seletor_resultados = '[data-testid="result-title-a"]'
        await page.wait_for_selector(seletor_resultados)

        # Localizamos o radar nos resultados, mas dizemos .first para apanhar só o número 1
        primeiro_resultado = page.locator(seletor_resultados).first
        
        titulo = await primeiro_resultado.inner_text()
        link = await primeiro_resultado.get_attribute("href")
        
        print(f"Título: {titulo}")
        print(f"Link: {link}")

        await page.wait_for_timeout(3000)
        
        await browser.close()

# O motor de arranque
asyncio.run(automate_duckduckgo())

'''
Apontar Localizadores
page.locator(".classe" ou "#id") -> A forma tradicional. Procura pelo código HTML (igual ao BeautifulSoup).
page.get_by_placeholder("texto") -> Procura pela marca de água dentro de uma caixa de texto.
page.get_by_role("button", name="Submeter") -> Procura pela função do elemento (ex: botão, link, título).

Agir Ações do Rato e Teclado
await elemento.click() -> Clica com o rato.
await elemento.fill("texto") -> Escreve texto dentro de uma caixa.
await elemento.press("Enter") -> Carrega numa tecla específica do teclado.

Extrair (Ler os dados)
await elemento.inner_text() -> Puxa o texto limpo e visível no ecrã.
await elemento.get_attribute("href") -> Puxa um link ou atributo escondido no HTML.

1- Vai ao site.
2- Aponta para a barra de pesquisa.
3- Age: Escreve "Python" e carrega no Enter.
4-(O cérebro espera que a página nova carregue.
5- Aponta para o título principal da página.
6- Extrai o texto desse título para a sua memória.

'''