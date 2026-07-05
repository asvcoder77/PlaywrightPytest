import pytest

@pytest.fixture(scope="function")
def preWork():
    print("I setup browser instance")
    return "PASS"

def test_InitialCheck(preWork):
    print("this is the initial check")
    assert preWork == "PASS"

def test_SecondCheck(preWork):
    print("this is the testing steps")