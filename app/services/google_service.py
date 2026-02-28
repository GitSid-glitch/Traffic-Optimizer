import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

DIRECTIONS_URL = "https://maps.googleapis.com/maps/api/directions/json"
def get_routes(origin, destination):
    params = {
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "alternatives": "true",
        "departure_time": "now",
        "key": API_KEY
    }
    response = requests.get(DIRECTIONS_URL, params=params, timeout=5)
    if response.status_code != 200:
        print("Google API Error:", response.text)
        return []
    data = response.json()
    if data["status"] != "OK":
        print("Directions API status:", data["status"])
        return []
    routes = []
    for route in data["routes"]:
        leg = route["legs"][0]
        base_duration = leg["duration"]["value"] 
        if "duration_in_traffic" in leg:
            traffic_duration = leg["duration_in_traffic"]["value"]
        else:
            traffic_duration = base_duration

        routes.append({
            "base_duration": base_duration,
            "traffic_duration": traffic_duration,
            "distance": leg["distance"]["value"],
            "polyline": route["overview_polyline"]["points"]
        })

    return routes