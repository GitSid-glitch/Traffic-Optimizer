from app.utils.geo import decode_route_polyline, compute_total_distance
class RouteSimulator:
    def __init__(self, route):
        self.route = route
        self.points = decode_route_polyline(route)
        self.current_index = 0

        self.total_distance = compute_total_distance(self.points)
    def get_current_position(self):
        return self.points[self.current_index]
    def move_forward(self, step=5):
        self.current_index = min(self.current_index + step, len(self.points) - 1)
    def get_remaining_distance_fraction(self):
        remaining_points = self.points[self.current_index:]
        remaining_distance = compute_total_distance(remaining_points)
        return remaining_distance / self.total_distance
    def is_finished(self):
        return self.current_index >= len(self.points) - 1