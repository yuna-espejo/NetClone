from playwright.sync_api import sync_playwright
from app.network import get_gateway_ip

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto(f"http://{get_gateway_ip()}")
    page.wait_for_load_state("networkidle")
    page.fill("input[placeholder='Usuario']","admin")
    page.fill("input[placeholder='Contraseña']","admin")
    page.click("input[value='Iniciar la sesión']")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="router_login.png")
    page.screenshot(path="router.png")