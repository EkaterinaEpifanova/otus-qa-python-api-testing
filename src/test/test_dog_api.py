"""Dog API tests"""
import allure
import pytest

@allure.step("List all breeds")
def test_list_all_breeds(dog_api_client):
    """List all breeds"""
    response = dog_api_client.get("breeds/list/all")
    assert response["status"] == "success"
    assert "message" in response
    assert "bulldog" in response["message"]

@allure.step("Single random image from a breed collection")
@pytest.mark.parametrize("breed", ["retriever", "bulldog", "poodle"])
def test_get_random_image_by_breed(dog_api_client, breed):
    """Single random image from a breed collection"""
    response = dog_api_client.get(f"breed/{breed}/images/random")
    image_url = response["message"]
    assert isinstance(image_url, str)
    assert response["status"] == "success"
    assert breed in image_url.lower(), f"Breed '{breed}' not found in image URL: {image_url}"

@allure.step("Single random image from a sub breed collection")
@pytest.mark.parametrize("sub_breed", ["english", "french"])
def test_sub_breed_images(dog_api_client, sub_breed):
    """Single random image from a sub breed collection"""
    response = dog_api_client.get(f"breed/bulldog/{sub_breed}/images")
    image_urls = response["message"]
    assert isinstance(image_urls, list)
    assert response["status"] == "success"
    assert all(img_url.startswith("https://") for img_url in image_urls)
    assert all(
        sub_breed in img_url.lower()
        for img_url in image_urls
    ), f"Not all image URLs contain sub-breed '{sub_breed}'"

@allure.step("Get all images of a specific breed")
@pytest.mark.parametrize("breed", ["retriever"])
def test_get_images_by_breed(dog_api_client, breed):
    """Get all images of a specific breed"""
    response = dog_api_client.get(f"breed/{breed}/images")
    image_urls = response["message"]
    assert response["status"] == "success"
    assert isinstance(response["message"], list)
    assert all(img_url.startswith("https://") for img_url in image_urls)
    assert all(
        breed in img_url.lower()
        for img_url in image_urls
    ), f"Not all image URLs contain sub-breed '{breed}'"

@allure.step("Get random image by sub-breed")
@pytest.mark.parametrize("breed,sub_breed", [
    ("bulldog", "english"),
    ("bulldog", "french"),
])
def test_random_image_by_sub_breed(dog_api_client, breed, sub_breed):
    """Get random image by sub-breed"""
    response = dog_api_client.get(f"breed/{breed}/{sub_breed}/images/random")
    image_url = response["message"]
    assert response["status"] == "success"
    assert isinstance(image_url, str)
    assert image_url.startswith("https://")
    assert breed in image_url
    assert sub_breed in image_url
