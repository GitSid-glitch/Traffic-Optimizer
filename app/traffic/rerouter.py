from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
def should_reroute(current_route, new_best_route, threshold=0.08):
    current_remaining = current_route["traffic_duration"]
    new_time = new_best_route["traffic_duration"]
    improvement = (current_remaining - new_time) / current_remaining
    return improvement > threshold

def intelligent_reroute(current_position, destination, current_route):
    routes = get_routes(current_position, destination)
    if not routes:
        return current_route, False
    best_route = choose_best_route(routes)
    if should_reroute(current_route, best_route):
        return best_route, True
    return current_route, False