
def test_sensor_data_no_api_key(client):
    response = client.post("/api/sensor_data", json={"temperature": 21.0, "humidity": 50})
    assert response.status_code == 401


def test_sensor_data_wrong_key(client):
    response = client.post("/api/sensor_data", headers={"X-API-Key": "wrong-key"}, json={"temperature": 21.0, "humidity": 50})
    
    assert response.status_code == 401


def test_sensor_data_valid_key(client):
    response = client.post("/api/sensor_data", headers={"X-API-Key": "test-sensor-key"}, json={"temperature": 21.0, "humidity": 50})

    assert response.status_code == 201
    assert response.get_json() is not None
