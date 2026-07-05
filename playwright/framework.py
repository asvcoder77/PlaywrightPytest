import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import context

from pageObjects import login_page

from pageObjects.login_page import LoginPage
from pageObjects import dashboard_page

from pageObjects.dashboard_page import DashboardPage
from utils.apiBase import APIUtils

#JSON File>Util>Access into Test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright,browserInstance, user_credentials):
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # Create order,order ID
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, user_credentials)

    login_page = LoginPage(browserInstance)
    login_page.navigate()
    dashboard_page=login_page.login(username,password)
    orders_history_page=dashboard_page.select_orders_nav_link()
    order_details_page=orders_history_page.select_order(orderID)
    order_details_page.verify_order_message()





