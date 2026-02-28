import random
def generate_parking_spots(destination, count=6):
    lat, lng = destination
    spots = []
    for i in range(count):
        spot = {
            "id": i,
            "lat": lat + random.uniform(-0.01, 0.01),
            "lng": lng + random.uniform(-0.01, 0.01),
            "cost_per_hour": random.randint(20, 80),
            "capacity": random.randint(20, 100),
            "available_spots": random.randint(0, 50),
        }
        spots.append(spot)
    return spots