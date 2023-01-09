

import pytest

from frameworks.exchange_services.exchange_services import ExchangeServices


@pytest.fixture()
def clean_up():
    pass


def test_init():
    result = ExchangeServices()
