import random
from datetime import datetime
def get_time_multiplier():
    hour = datetime.now().hour
    if 8 <= hour <= 10:
        return random.uniform(1.4, 1.8)
    elif 17 <= hour <= 20:
        return random.uniform(1.5, 2.0)
    elif 12 <= hour <= 14:
        return random.uniform(1.2, 1.4)
    else:
        return random.uniform(0.9, 1.1)
def apply_traffic(route):
    base_time = route["duration"]
    multiplier = get_time_multiplier()
    predicted_time = base_time * multiplier
    return predicted_time