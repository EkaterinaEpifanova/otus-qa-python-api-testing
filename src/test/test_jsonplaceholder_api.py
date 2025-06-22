"""Json Placeholder API tests"""
import pytest

@pytest.mark.parametrize("request_id", [1, 50, 100])
def test_get_post_by_id(service, json_placeholder_url, request_id):
    """Post method by id"""
    url = f"{json_placeholder_url}/posts/{request_id}"
    response = service.get(url)
    assert response["id"] == request_id

@pytest.mark.parametrize(
    "title, body_text, user_id",
    [
        ("First title", "First body", 1),
        ("Second title", "Second body", 2),
        ("Third title", "Third body", 3),
    ]
)
def test_create_post(service, json_placeholder_url, title, body_text, user_id):
    """Post with different titles, bodies, and userIds"""
    url = f"{json_placeholder_url}/posts"
    body = {
        "title": title,
        "body": body_text,
        "userId": user_id
    }
    response = service.post(url, body)

    assert response is not None
    assert response["title"] == title
    assert response["body"] == body_text
    assert response["userId"] == user_id

@pytest.mark.parametrize(
    "request_id, title, body_text, user_id",
    [
        (1, "First title", "First body", 1)
    ]
)
def test_update_post(service, json_placeholder_url, request_id, title, body_text, user_id):
    """Update data using PUT request"""
    url = f"{json_placeholder_url}/posts/1"
    body = {
        "id": request_id,
        "title": title,
        "body": body_text,
        "userId": user_id
    }
    headers = {"Content-Type": "application/json"}
    response = service.put(url, body, headers)

    assert response is not None
    assert response["id"] == request_id
    assert response["title"] == title
    assert response["body"] == body_text
    assert response["userId"] == user_id

@pytest.mark.parametrize("request_id", [1])
def test_delete_post(service, json_placeholder_url, request_id):
    """Delete data"""
    url = f"{json_placeholder_url}/posts/{request_id}"
    headers = {"Content-Type": "application/json"}
    response = service.delete(url, headers)

    assert response == {}
