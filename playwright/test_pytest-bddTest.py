import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from conftest import user_credentials
from pageObjects import login_page
from pageObjects.login_page import LoginPage
from utils.apiBase import APIUtils

scenarios("features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, user_credentials)
    shared_data['orderID'] = orderID


@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    shared_data['login_page'] = login_page


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    orders_history_page = dashboard_page.select_orders_nav_link()
    shared_data['orders_history_page'] = orders_history_page


@when('select orderID')
def select_orderID(shared_data):
    orders_history_page = shared_data['orders_history_page']
    orderID = shared_data['orderID']
    order_details_page = orders_history_page.select_order(orderID)
    shared_data['order_details_page'] = order_details_page


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    order_details_page = shared_data['order_details_page']
    order_details_page.verify_order_message()
