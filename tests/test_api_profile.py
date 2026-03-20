
def auth_header(token="fake_token"):
    return {"Authorization": f"Bearer {token}"}


def test_get_profile_no_auth(client):
    assert client.get("/api/profile").status_code == 401


def test_get_profile_bad_token_format(client):
    assert client.get("/api/profile", headers={"Authorization": "fake_token"}).status_code == 401


def test_get_profile_invalid_token(client):
    assert client.get("/api/profile", headers=auth_header()).status_code == 401


def test_get_profile_successful(client, mock_firebase_auth, mock_firestore):
    mock_firestore["snapshot"].exists = True

    response = client.get("/api/profile", headers=auth_header())

    assert response.status_code == 200
    data = response.get_json()

    assert data["uid"] == "test_user_123"
    assert data["profile"] == {"first_name": "Test", "last_name": "User", "student_id": "12345678"}


def test_create_profile_missing_fields(client, mock_firebase_auth):
    assert client.post("/api/profile", headers=auth_header(), json={"first_name": "Ronald"}).status_code == 400


def test_create_profile_success(client, mock_firebase_auth, mock_firestore):
    assert client.post("/api/profile", headers=auth_header(), json={"first_name": "Ronald", "last_name": "Ho", "student_id": "A01180478"}).status_code == 200


def test_update_profile_invalid_field(client, mock_firebase_auth):
    response = client.put("/api/profile", headers=auth_header(), json={"age": 25})

    assert response.status_code == 400
    data = response.get_json()
    assert data is not None
    assert "errors" in data