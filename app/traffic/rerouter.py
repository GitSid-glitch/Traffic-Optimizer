from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
def intelligent_reroute(simulator, destination, threshold=0.08):
    current_position = simulator.get_current_position()
    routes = get_routes(current_position, destination)
    if not routes:
        return simulator.route, False
    best_new_route = choose_best_route(routes)
    total_points = len(simulator.points)
    remaining_points = total_points - simulator.current_index
    remaining_fraction = remaining_points / total_points
    current_remaining_time = (
        simulator.route["traffic_duration"] * remaining_fraction)
    new_route_time = best_new_route["traffic_duration"]
    improvement = (
        current_remaining_time - new_route_time) / current_remaining_time
    if improvement > threshold:
        return best_new_route, True
    return simulator.route, False