from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
def dynamic_reroute(current_position, destination, current_route):
    routes = get_routes(current_position, destination)
    if not routes:
        return current_route
    new_best = choose_best_route(routes)
    if not current_route:
        return new_best

    current_score = current_route["predicted_duration"]
    new_score = new_best["predicted_duration"]
    if new_score < current_score * 0.95:
        print("Switching route due to better prediction.")
        return new_best
    return current_route