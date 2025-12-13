from playwright.sync_api import sync_playwright
from time import sleep
import re
import pytest

@pytest.mark.xfail(strict=True)
def test_hamburger_button() :
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://app.3o3.co.kr/login")
        page.get_by_role("button", name="카카오 계정으로 계속하기").click()
        # 수동 로그인, 자동화 시 보안 문제있을 수 있음, 로그인 제한 시간 5분, OAuth 문제인지 세션 유지가 안돼 매번 로그인 해야 함
        page.wait_for_url("https://app.3o3.co.kr/payment/not-target/normal",timeout=300_000)
        #햄버거 버튼 클릭
        page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
        page.locator("div").filter(has_text="소득 리포트").nth(3).click()
        page.get_by_text("세금", exact=True).click()
        page.get_by_role("button").first.click()
        page.locator("div").filter(has_text="신고 내역").nth(3).click()
        page.get_by_role("button", name="뒤로가기").click()
        page.locator("div").filter(has_text="환급금 지급 내역").nth(3).click()
        page.get_by_role("button", name="확인").click()

        #page.get_by_role("img").nth(4).click()
        #여기까지 확인 완료, 뒤로가기 x
        #page.get_by_role("button", name="button").click()

        #고객센터는 팝업으로 표시됨
        with page.expect_popup() as page1_info:
            page.get_by_role("img").nth(3).click()
        page1 = page1_info.value
        page1.close()
        page.get_by_role("button", name="친구초대").click()
        page.locator("#root").click()

if __name__ == "__main__":
    test_hamburger_button()