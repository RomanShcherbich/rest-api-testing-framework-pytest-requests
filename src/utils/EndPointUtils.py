BOOKING_PATH = "/booking"


class BookingEndpoint:

    def __init__(self):
        self.path = BOOKING_PATH

    def get_path(self):
        return self.path

    def get_path_with_id(self, booking_id):
        return "{}/{}".format(self.path, booking_id)
