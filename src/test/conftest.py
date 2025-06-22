"""Test fixtures"""
import pytest
from src.main.client.service import BaseService

@pytest.fixture(scope="session")
def service():
    """Shared BaseService instance for API tests"""
    return BaseService()

@pytest.fixture
def dog_api_url():
    """Dog URL"""
    return "https://dog.ceo/api"

@pytest.fixture
def brewery_api_url():
    """Brewery API URL"""
    return "https://api.openbrewerydb.org/v1/breweries"

@pytest.fixture
def json_placeholder_url():
    """Placeholder URL"""
    return "https://jsonplaceholder.typicode.com"
