import polyline
class RouteSimulator:

    def __init__(self, route):
        self.route = route
        self.total_duration = route["traffic_duration"]
        self.coordinates = polyline.decode(route["polyline"])

        self.total_points = len(self.coordinates)
        self.current_index = 0

    def advance(self, seconds):
        progress_fraction = seconds / self.total_duration
        steps_to_move = int(progress_fraction * self.total_points)

        self.current_index += steps_to_move

        if self.current_index >= self.total_points:
            self.current_index = self.total_points - 1

    def get_current_position(self):
        return self.coordinates[self.current_index]

    def get_remaining_distance_fraction(self):
        return max(
            0,
            (self.total_points - self.current_index) / self.total_points
        )

    def is_finished(self):
        return self.current_index >= self.total_points - 1

    def update_route(self, new_route):
        self.route = new_route
        self.total_duration = new_route["traffic_duration"]
        self.coordinates = polyline.decode(new_route["polyline"])
        self.total_points = len(self.coordinates)
        self.current_index = 0