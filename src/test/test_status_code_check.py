"""Status code test, second part of the homework #5"""
import allure
import requests

@allure.step("Check if response status code matches expected")
def test_status_code(url, status_code):
    """Check if response status code matches expected"""
    response = requests.get(url = url, timeout = 10)
    assert response.status_code == status_code, \
        (f"Expected status code {status_code}, got {response.status_code}")
