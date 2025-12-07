"""Brewery API tests"""
import allure
import pytest

@allure.step("Filter breweries by city")
@pytest.mark.parametrize("city,expected", [
    ("san_diego", "San Diego"),
    ("portland", "Portland")
])
def test_breweries_by_city(brewery_api_service, city, expected):
    """Filter breweries by city"""
    response = brewery_api_service.get(f"/v1/breweries?by_city={city}")
    assert all("city" in brewery for brewery in response)
    # Проверка, что ожидаемая подстрока входит в значение поля city,
    # так как API по запросу иногда возвращает "city": "South Portland",
    for brewery in response:
        actual = brewery["city"]
        assert expected in actual, f"Expected substring '{expected}' in '{actual}'"

@allure.step("Filter breweries by type")
@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(brewery_api_service, brewery_type):
    """Filter breweries by type"""
    response = brewery_api_service.get(f"/v1/breweries?by_type={brewery_type}")
    assert all("brewery_type" in brewery for brewery in response)
    for brewery in response:
        actual = brewery["brewery_type"]
        assert brewery_type == actual,  f"Expected substring '{brewery_type}' in '{actual}'"

@allure.step("Returns a list of breweries")
def test_get_all_breweries(brewery_api_service):
    """Returns a list of breweries"""
    response = brewery_api_service.get("/v1/breweries")

    assert isinstance(response, list)

@allure.step("Get a single brewery")
@pytest.mark.parametrize("brewery_uuid", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"])
def test_single_brewery(brewery_api_service, brewery_uuid):
    """Get a single brewery"""
    response = brewery_api_service.get(f"/v1/breweries/{brewery_uuid}")
    assert brewery_uuid == response["id"]

@allure.step("Search breweries by name")
@pytest.mark.parametrize("query_param", ["dog"])
def test_search_brewery_by_name(brewery_api_service, query_param):
    """Search breweries by name"""
    response = brewery_api_service.get(f"/v1/breweries/search?query={query_param}")

    assert isinstance(response, list)
    assert any("dog" in brewery["name"].lower() for brewery in response if "name" in brewery)
