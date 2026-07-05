from playwright.sync_api import Page

fakePayLoadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrderResponse
    )


def test_Network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.get_by_placeholder("email@example.com").fill("asvishnukaruvannur7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Vi@12345")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="  ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)