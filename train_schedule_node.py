class train_schedule_node(object):
    '''
    trip_id = None
    last_known_stop = None
    last_known_time = None
    stop_number = None
    scheduled_stops = []
    route_id = None
    target_stop = None
    target_stop_time = None'''

    def __init__(self, trip_id, route_id, stop_number, current_status,
                 scheduled_stops):
        self.trip_id = trip_id
        self.stop_number = stop_number
        self.scheduled_stops = scheduled_stops
        self.route_id = route_id
        if (current_status <= 1):
            self.last_known_stop = scheduled_stops[0][0]
            self.last_known_time = scheduled_stops[0][1]
            if (len(scheduled_stops) > 1):
                self.target_stop = scheduled_stops[1][0]
                self.target_stop_time = scheduled_stops[1][1]
        else:
            self.target_stop = scheduled_stops[0][0]
            self.target_stop_time = scheduled_stops[0][1]
            self.last_known_stop = None
            self.last_known_time = None

    def update(self, stop_number, current_status, scheduled_stops):
        self.stop_number = stop_number
        self.scheduled_stops = scheduled_stops
        if current_status <= 1:
            self.last_known_stop = scheduled_stops[0][0]
            self.last_known_time = scheduled_stops[0][1]
            if len(scheduled_stops) > 1:
                self.target_stop = scheduled_stops[1][0]
                self.target_stop_time = scheduled_stops[1][1]
        else:
            self.target_stop = scheduled_stops[0][0]
            self.target_stop_time = scheduled_stops[0][1]

    def get_last_stop(self):
        return self.last_known_stop

    def get_last_stop_time(self):
        return self.last_known_time

    def get_next_stop(self):
        return self.target_stop

    def get_next_stop_time(self):
        return self.target_stop_time

    def time_between_stops(self):
        return self.target_stop_time - self.last_known_time

    def fraction_remaining(self, timestamp):
        return float(timestamp - self.last_known_time) / \
               float(self.time_between_stops())
