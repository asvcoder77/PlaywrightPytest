from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import context

from pageObjects.login_page import LoginPage
from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
#Create order,order ID
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright)
    print(orderID)
#Login
    loginPage = LoginPage(page) #Object for login page

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("asvishnukaruvannur7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vi@12345")
    page.get_by_role("button",name="login").click()
    page.get_by_role("button",name="  ORDERS").click()
#Go to orderhistory page and check order ID present
    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button",name="view").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")