from playwright.sync_api import sync_playwright, expect
from time import sleep
import re

def test_main_page() :
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.3o3.co.kr/login", timeout=60_000)
        expect(page).to_have_url("https://app.3o3.co.kr/login")


if __name__ == "__main__":
    test_main_page()