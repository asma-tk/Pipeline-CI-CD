

import requests

def test_prediction():
    url='http://127.0.0.1:8000'
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = requests.post(f"{url}/predict", json=payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert "prediction" in data, "Response JSON should contain 'prediction'"
    assert "species_name" in data, "Response JSON should contain 'species_name'"
    assert data["prediction"] == 0, f"Expected prediction 0 for setosa, got {data['prediction']}"
    assert data["species_name"] == "setosa", f"Expected species_name 'setosa', got {data['species_name']}"

if __name__ == "__main__":
    test_prediction()
    print("All tests passed!")
