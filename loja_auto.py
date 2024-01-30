#Importação do sync_playwright da biblioteca playwright
from playwright.sync_api import sync_playwright

#Importando a biblioteca time para visualizar a página melhor
import time

#Criando o navegador
with (sync_playwright() as p):
    navegador = p.chromium.launch(headless=False)

    #Criando uma nova página
    pagina = navegador.new_page()

    #Apontando para qual site o código deve ir
    pagina.goto("https://www.saucedemo.com")

    #Digitando o Login
    pagina.fill('xpath=//*[@id="user-name"]', 'standard_user')
    time.sleep(1)
    pagina.screenshot(path="login.png", full_page=True)

    #Digitando a senha
    pagina.fill('xpath=//*[@id="password"]', 'secret_sauce')
    time.sleep(1)
    pagina.screenshot(path="senha.png", full_page=True)

    #Clicando no botão de login
    pagina.locator('xpath=//*[@id="login-button"]').click()
    time.sleep(1)
    pagina.screenshot(path="login_button.png", full_page=True)

    #Filtrando os produtos do mais caro para o mais barato
    pagina.query_selector('xpath=//*[@id="header_container"]/div[2]/div/span/select').select_option(label='Price (high to low)')
    time.sleep(1)
    pagina.screenshot(path="filtro.png", full_page=True)

    #Adiciona a jaqueta ao carrinho
    pagina.locator('xpath=//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(1)
    pagina.screenshot(path="jaqueta.png", full_page=True)

    #Clica no carrinho
    pagina.locator('xpath=//*[@id="shopping_cart_container"]/a').click()
    time.sleep(1)
    pagina.screenshot(path="carrinho.png", full_page=True)

    #Clica no checkout
    pagina.locator('xpath=//*[@id="checkout"]').click()
    time.sleep(1)
    pagina.screenshot(path="checkout.png", full_page=True)
    
    #Preenche o first name
    pagina.fill('xpath=//*[@id="first-name"]', 'Teste')
    time.sleep(1)
    pagina.screenshot(path="first_name.png", full_page=True)

    #Preenche o last name
    pagina.fill('xpath=//*[@id="last-name"]', 'Playwright')
    time.sleep(1)
    pagina.screenshot(path="last_name.png", full_page=True)

    #Preenche o código postal
    pagina.fill('xpath=//*[@id="postal-code"]', '12345678')
    time.sleep(1)
    pagina.screenshot(path="zip.png", full_page=True)

    #Clica no botão para continuar a compra
    pagina.locator('xpath=//*[@id="continue"]').click()
    time.sleep(1)
    pagina.screenshot(path="continue.png", full_page=True)

    #Clica para finalizar a compra
    pagina.locator('xpath=//*[@id="finish"]').click()
    pagina.screenshot(path="finish.png", full_page=True)

    time.sleep(5)
