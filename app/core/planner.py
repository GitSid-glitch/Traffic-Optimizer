from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
from app.parking.parking_data import generate_parking_spots
from app.parking.parking_optimizer import choose_best_parking
def plan_route(origin, destination, use_parking=False):
    if not use_parking:
        routes = get_routes(origin, destination)
        if not routes:
            return None
        best_route = choose_best_route(routes)
        best_route["origin_coords"] = origin
        return best_route
    parking_spots = generate_parking_spots(destination)
    best_parking_option = choose_best_parking(origin, destination, parking_spots)
    if not best_parking_option:
        return None
    best_parking_option["route"]["origin_coords"] = origin

    return {
        "mode": "parking",
        "parking_id": best_parking_option["parking_id"],
        "route": best_parking_option["route"],
        "drive_time": best_parking_option["drive_time"],
        "walking_time": best_parking_option["walking_time"],
        "cost": best_parking_option["cost"],
        "available_spots": best_parking_option["available_spots"],
        "total_score": best_parking_option["total_score"],
    }