from app.services.google_service import get_routes
from app.traffic.optimizer import choose_best_route
def plan_route(origin, destination):
    routes = get_routes(origin, destination)
    if not routes:
        return None
    best_route = choose_best_route(routes)
    return best_route