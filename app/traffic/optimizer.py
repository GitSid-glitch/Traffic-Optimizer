def compute_route_score(route):
    return route["traffic_duration"]
def choose_best_route(routes):
    best_route = None
    best_score = float("inf")
    for route in routes:
        score = compute_route_score(route)
        if score < best_score:
            best_score = score
            best_route = route
    return best_route