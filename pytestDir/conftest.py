import pytest

@pytest.fixture(scope="function")
def preSetUpWork():
    print("Launch browser")