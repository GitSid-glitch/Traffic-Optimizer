from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
MIN_REMAINING_TIME = 180
MIN_TIME_SAVED = 120
EMERGENCY_TIME_SAVED = 300
def intelligent_reroute(simulator, destination):
    current_position = simulator.get_current_position()
    routes = get_routes(current_position, destination)
    if not routes:
        return simulator.route, False
    best_new_route = choose_best_route(routes)
    current_route_time = simulator.route.get("traffic_duration")
    if not current_route_time:
        return simulator.route, False
    remaining_fraction = max(0, min(1, simulator.get_remaining_distance_fraction()))
    current_remaining_time = current_route_time * remaining_fraction
    if current_remaining_time <= MIN_REMAINING_TIME:
        print("Near destination. No rerouting.")
        return simulator.route, False
    new_route_time = best_new_route.get("traffic_duration")
    if not new_route_time:
        return simulator.route, False
    time_saved = current_remaining_time - new_route_time
    print("\n---- Reroute Evaluation ----")
    print("Current Remaining Time:", round(current_remaining_time))
    print("New Route Time:", new_route_time)
    print("Time Saved:", round(time_saved))
    if time_saved > EMERGENCY_TIME_SAVED:
        print(">>> EMERGENCY REROUTE TRIGGERED <<<")
        return best_new_route, True
    if time_saved > MIN_TIME_SAVED:
        print(">>> REROUTING TRIGGERED <<<")
        return best_new_route, True
    print("No reroute. Not enough time saved.")
    return simulator.route, False