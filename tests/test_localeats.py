
from playwright.sync_api import sync_playwright, expect

# Murilo Rodrigues

def test_abrir_formulario_cadastro():

    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()

        # Acessar o LocalEats
        pagina.goto("https://local-eats-unisenac.vercel.app/")

        # Clicar em Criar Conta
        pagina.get_by_role(
            "button", name="Criar Conta"
        ).click()

        # Primeira assertion: verificar campo de nome
        expect(
            pagina.locator("#regName")
        ).to_be_visible()

        # Segunda assertion: verificar campo de e-mail
        expect(
            pagina.locator("#regEmail")
        ).to_be_visible()

        navegador.close()
