from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
from app.utils.geo import haversine
WALKING_SPEED_KMPH = 5
AVAILABILITY_WEIGHT = 500 
def compute_parking_score(origin, destination, parking_spot):
    routes = get_routes(origin, (parking_spot["lat"], parking_spot["lng"]))
    if not routes:
        return None
    best_route = choose_best_route(routes)
    drive_time = best_route["traffic_duration"]
    walking_distance = haversine((parking_spot["lat"], parking_spot["lng"]), destination)
    walking_time = (walking_distance / WALKING_SPEED_KMPH) * 3600
    cost_penalty = parking_spot["cost_per_hour"] * 20
    availability_penalty = 0
    if parking_spot["available_spots"] < 5:
        availability_penalty = AVAILABILITY_WEIGHT
    total_score = (drive_time + walking_time + cost_penalty + availability_penalty)
    return {
        "parking_id": parking_spot["id"],
        "total_score": total_score,
        "drive_time": drive_time,
        "walking_time": walking_time,
        "cost": parking_spot["cost_per_hour"],
        "available_spots": parking_spot["available_spots"],
        "route": best_route
    }

def choose_best_parking(origin, destination, parking_spots):
    best_option = None
    best_score = float("inf")
    for spot in parking_spots:
        result = compute_parking_score(origin, destination, spot)
        if not result:
            continue
        if result["total_score"] < best_score:
            best_score = result["total_score"]
            best_option = result
    return best_option