from playwright.sync_api import sync_playwright
from app.network import get_gateway_ip

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto(f"http://{get_gateway_ip()}")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="router.png")