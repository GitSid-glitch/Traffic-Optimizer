from app.traffic.predictor import predict_future_multiplier
def compute_route_score(route):
    base = route["base_duration"]
    predicted_multiplier = predict_future_multiplier(route)
    predicted_duration = base * predicted_multiplier
    route["predicted_duration"] = predicted_duration
    return predicted_duration
def choose_best_route(routes):
    best_route = None
    best_score = float("inf")
    for route in routes:
        score = compute_route_score(route)
        if score < best_score:
            best_score = score
            best_route = route

    return best_route