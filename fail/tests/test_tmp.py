import pytest
from playwright.sync_api import sync_playwright
import re
from time import sleep

def test_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="session/session_state.json")
        page = context.new_page()
        page.goto("https://app.3o3.co.kr/payment/not-target/normal")
        #page.wait_for_url("https://app.3o3.co.kr/payment/not-target/normal", timeout=300_000)
        page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
        page.locator("div").filter(has_text="신고 내역").nth(3).click()
        sleep(1)
        page.get_by_role("button", name="뒤로가기").click()
        sleep(1)
        page.get_by_text("환급금 지급 내역").click()
        sleep(1)
        page.get_by_role("button", name="확인").click()

        browser.close()