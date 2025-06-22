"""Brewery API tests"""
import pytest

@pytest.mark.parametrize("city,expected", [
    ("san_diego", "San Diego"),
    ("portland", "Portland")
])
def test_breweries_by_city(service, brewery_api_url, city, expected):
    """Filter breweries by city"""
    url = f"{brewery_api_url}?by_city={city}"
    response = service.get(url)
    assert response is not None
    assert all("city" in brewery for brewery in response)
    # Проверка, что ожидаемая подстрока входит в значение поля city,
    # так как API по запросу иногда возвращает "city": "South Portland",
    for brewery in response:
        actual = brewery["city"]
        assert expected in actual, f"Expected substring '{expected}' in '{actual}'"

@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(service, brewery_api_url, brewery_type):
    """Filter breweries by type"""
    url = f"{brewery_api_url}?by_type={brewery_type}"
    response = service.get(url)

    assert response is not None
    assert all("brewery_type" in brewery for brewery in response)
    for brewery in response:
        actual = brewery["brewery_type"]
        assert brewery_type == actual,  f"Expected substring '{brewery_type}' in '{actual}'"

def test_get_all_breweries(service, brewery_api_url):
    """Returns a list of breweries"""
    response = service.get(brewery_api_url)
    assert response is not None
    assert isinstance(response, list)

@pytest.mark.parametrize("brewery_uuid", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"])
def test_single_brewery(service, brewery_api_url, brewery_uuid):
    """Get a single brewery"""
    url = f"{brewery_api_url}/{brewery_uuid}"
    response = service.get(url)
    assert response is not None
    assert brewery_uuid == response["id"]

@pytest.mark.parametrize("query_param", ["dog"])
def test_search_brewery_by_name(service, brewery_api_url, query_param):
    """Search breweries by name"""
    url = f"{brewery_api_url}/search?query={query_param}"
    response = service.get(url)

    assert response is not None
    assert isinstance(response, list)
    assert any("dog" in brewery["name"].lower() for brewery in response if "name" in brewery)