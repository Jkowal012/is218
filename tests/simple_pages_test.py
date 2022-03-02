def test_request_about(client):
    response= client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_about(client):
    response= client.get("/index")
    assert response.status_code == 200
    assert b"About Page" in response.data