import pytest


@pytest.fixture(scope="function")
def preSecondWork():
    print("this is the initial Setup")
    yield
    print("this is the teardown")
def test_ThirdCheck(preSetUpWork,preSecondWork):
    print("this is the testing steps")