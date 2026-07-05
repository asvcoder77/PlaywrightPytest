import time

from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from utils.apiBase import APIUtils


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=5a47ccbfcd73adf7e59088ad")

def test_Network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest)
    page.get_by_placeholder("email@example.com").fill("asvishnukaruvannur7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vi@12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="  ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    text=page.locator(".blink_me").text_content()
    print(text)

#Bypassing login page
def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    get_token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
#script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
