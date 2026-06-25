import asyncio
from playwright.async_api import async_playwright
import time

async def dynamic_wait():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        tab1 = await context.new_page()
        await tab1.goto("https://hn.algolia.com/")

        await tab1.locator("input[type='search']").fill("A story")

        pesquisa = tab1.locator(".SearchResults_container")
        await pesquisa.first.wait_for(state="visible")
        titulo = tab1.locator(".Story_title")
        await tab1.wait_for_timeout(500)

        primeiros_resultados = await titulo.all()

        cinco = primeiros_resultados[:5]
        for resultados in cinco:
            texto = await resultados.inner_text()
            link = await resultados.locator("a").first.get_attribute("href")
            print(f"{texto}\n{link}")

        tab2 = await context.new_page()
        inicio_idle = time.time()
        await tab2.goto("https://unsplash.com/")
        await tab1.close()
        print("="*50)
        await tab2.wait_for_load_state("networkidle")
        tempo_idle = time.time() - inicio_idle
        print(f"Tempo com Network Idle: {tempo_idle:.2f} segundos")

        tab3 = await context.new_page()
        await tab3.goto("https://the-internet.herokuapp.com/entry_ad")
        await tab2.close()

        modal = tab3.locator(".modal")
        fechar = await tab3.wait_for_selector(".modal-footer p")
        print("="*50)
        await modal.wait_for(state="visible")
        print("Modal apareceu")
        await fechar.click()
        await modal.wait_for(state="hidden")
        print("Apagado")
        await tab3.locator("#restart-ad").click()
        print("Ativado outra vez")
        await tab3.wait_for_timeout(3000)

asyncio.run(dynamic_wait())