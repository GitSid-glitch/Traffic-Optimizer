from app.utils.geo import decode_route_polyline
class RouteSimulator:
    def __init__(self, route):
        self.route = route
        self.points = decode_route_polyline(route)
        self.current_index = 0
    def get_current_position(self):
        return self.points[self.current_index]
    def move_forward(self, step=5):
        self.current_index = min(self.current_index + step, len(self.points) - 1)
    def is_finished(self):
        return self.current_index >= len(self.points) - 1