"""Dog API tests"""

import pytest

def test_list_all_breeds(service, dog_api_url):
    """List all breeds"""
    url = f"{dog_api_url}/breeds/list/all"
    response = service.get(url)
    assert "bulldog" in response["message"]

@pytest.mark.parametrize("breed", ["retriever", "bulldog", "poodle"])
def test_get_random_image_by_breed(service, dog_api_url, breed):
    """Single random image from a breed collection"""
    url = f"{dog_api_url}/breed/{breed}/images/random"
    response = service.get(url)
    assert response is not None
    assert isinstance(response["message"], str)
    assert response["status"] == "success"

@pytest.mark.parametrize("sub_breed", ["english", "french"])
def test_sub_breed_images(service, dog_api_url, sub_breed):
    """Single random image from a sub breed collection"""
    url = f"{dog_api_url}/breed/bulldog/{sub_breed}/images"
    response = service.get(url)
    assert response is not None
    assert isinstance(response["message"], list)
    assert response["status"] == "success"
    assert all(img_url.startswith("https://") for img_url in response["message"])

@pytest.mark.parametrize("breed", ["retriever"])
def test_get_images_by_breed(service, dog_api_url, breed):
    """Get all images of a specific breed"""
    url = f"{dog_api_url}/breed/{breed}/images"
    response = service.get(url)

    assert response is not None
    assert response["status"] == "success"
    assert isinstance(response["message"], list)
    assert all(img_url.startswith("https://") for img_url in response["message"])

@pytest.mark.parametrize("breed,sub_breed", [
    ("bulldog", "english"),
    ("bulldog", "french"),
])
def test_random_image_by_sub_breed(service, dog_api_url, breed, sub_breed):
    """Get random image by sub-breed"""
    url = f"{dog_api_url}/breed/{breed}/{sub_breed}/images/random"
    response = service.get(url)

    assert response is not None
    assert response["status"] == "success"
    assert isinstance(response["message"], str)
    assert response["message"].startswith("https://")