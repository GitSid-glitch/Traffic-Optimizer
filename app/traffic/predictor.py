import time
def compute_current_multiplier(route):
    return route["traffic_duration"] / route["base_duration"]
def predict_future_multiplier(route):
    base = route["base_duration"]
    traffic = route["traffic_duration"]
    current_multiplier = compute_current_multiplier(route)
    travel_minutes = base / 60
    hour = time.localtime().tm_hour
    if 8 <= hour <= 10 or 17 <= hour <= 19:
        rush_factor = 0.2
    else:
        rush_factor = 0.05
    future_growth = rush_factor * (travel_minutes / 60)
    predicted_multiplier = current_multiplier + future_growth
    return predicted_multiplier