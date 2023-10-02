import pytest

from rest.lambdatest import LambdatestService


@pytest.fixture(scope="session")
def lambdatest_service():
    return LambdatestService()


@pytest.fixture
def context():
    return dict()
