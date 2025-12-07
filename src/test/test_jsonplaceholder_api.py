"""Json Placeholder API tests"""
import allure
import pytest

@allure.step("Get method by id")
@pytest.mark.parametrize("request_id", [1, 50, 100])
def test_get_post_by_id(json_placeholder_service, request_id):
    """Get method by id"""
    response = json_placeholder_service.get(f"posts/{request_id}")
    assert response["id"] == request_id

@allure.step("Post with different titles, bodies, and userIds")
@pytest.mark.parametrize(
    "title, body_text, user_id",
    [
        ("First title", "First body", 1),
        ("Second title", "Second body", 2),
        ("Third title", "Third body", 3),
    ]
)
def test_create_post(json_placeholder_service, title, body_text, user_id):
    """Post with different titles, bodies, and userIds"""
    body = {
        "title": title,
        "body": body_text,
        "userId": user_id
    }
    response = json_placeholder_service.post(path = "posts", body= body)

    assert response is not None
    assert response["title"] == title
    assert response["body"] == body_text
    assert response["userId"] == user_id

@allure.step("Update data using PUT request")
@pytest.mark.parametrize(
    "request_id, title, body_text, user_id",
    [
        (1, "First title", "First body", 1)
    ]
)
def test_update_post(json_placeholder_service, request_id, title, body_text, user_id):
    """Update data using PUT request"""
    body = {
        "id": request_id,
        "title": title,
        "body": body_text,
        "userId": user_id
    }
    headers = {"Content-Type": "application/json"}
    response = json_placeholder_service.put(path = "posts/1", body = body, headers = headers)

    assert response is not None
    assert response["id"] == request_id
    assert response["title"] == title
    assert response["body"] == body_text
    assert response["userId"] == user_id

@allure.step("Delete data")
@pytest.mark.parametrize("request_id", [1])
def test_delete_post(json_placeholder_service, request_id):
    """Delete data"""
    headers = {"Content-Type": "application/json"}
    response = json_placeholder_service.delete(path = f"posts/{request_id}", headers = headers)
    assert response == {}
