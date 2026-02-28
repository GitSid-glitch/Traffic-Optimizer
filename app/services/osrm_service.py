import requests

BASE_URL = "http://router.project-osrm.org/route/v1/driving/"

def get_routes(origin, destination):
    """
    origin, destination: (lat, lon)
    Returns list of route dictionaries.
    """

    coordinates = f"{origin[1]},{origin[0]};{destination[1]},{destination[0]}"
    url = f"{BASE_URL}{coordinates}"

    params = {
        "alternatives": "true",
        "overview": "full",
        "geometries": "polyline"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("code") != "Ok":
        return []

    return data["routes"]