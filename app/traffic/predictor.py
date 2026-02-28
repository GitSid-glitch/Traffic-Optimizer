import time
def compute_current_multiplier(route):
    return route["traffic_duration"] / route["base_duration"]
def predict_future_multiplier(route):
    base = route["base_duration"]
    distance_km = route["distance"] / 1000
    current_multiplier = compute_current_multiplier(route)
    congestion_level = max(0, current_multiplier - 1)
    hour = time.localtime().tm_hour
    if 8 <= hour <= 10 or 17 <= hour <= 19:
        demand_factor = 1.3
    elif 11 <= hour <= 16:
        demand_factor = 1.1
    else:
        demand_factor = 0.9
    congestion_growth = 1 + 0.5 * congestion_level
    exposure_factor = 1 + 0.03 * distance_km
    predicted_multiplier = (current_multiplier * congestion_growth * exposure_factor * demand_factor)
    return predicted_multiplier