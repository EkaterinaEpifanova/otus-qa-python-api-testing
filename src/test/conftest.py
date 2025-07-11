"""Test fixtures"""
import sys
import os
import pytest
# Добавляем src в sys.path вручную
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.client.service import BaseService


@pytest.fixture
def dog_api_client():
    """Dog URL"""
    return BaseService("https://dog.ceo/api")

@pytest.fixture
def brewery_api_service():
    """Brewery API URL"""
    return BaseService("https://api.openbrewerydb.org")

@pytest.fixture
def json_placeholder_service():
    """Placeholder URL"""
    return BaseService("https://jsonplaceholder.typicode.com")

def pytest_addoption(parser):
    """
    Register custom command-line options for pytest.
    This function adds additional options to pytest's CLI parser,
    such as --url and --status_code, which can be used in fixtures
    and test cases to customize the behavior of tests dynamically.
    Args:
        parser (Parser): Pytest's command line option parser.
    """
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL to test"
    )
    parser.addoption(
        "--status_code", action="store", default="200", help="Expected status code"
    )
@pytest.fixture
def url(request):
    """URL fixture"""
    return request.config.getoption("url")

@pytest.fixture
def status_code(request):
    """Status code fixture"""
    return int(request.config.getoption("status_code"))
