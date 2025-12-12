from playwright.sync_api import sync_playwright
from time import sleep

def create_session() :
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.3o3.co.kr/login")
        page.get_by_role("button", name="카카오 계정으로 계속하기").click()
        page.wait_for_url("https://app.3o3.co.kr/payment/not-target/normal", timeout=300_000)
        sleep(5)
        context.storage_state(path="session/session_state.json")
        sleep(5)
        browser.close()

if __name__ == "__main__":
    create_session()