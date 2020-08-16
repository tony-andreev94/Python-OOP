class Hotel:

    def __init__(self, name, ):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room_number == room.number][0]

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        self.guests += people
        if result:
            return result

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_to_remove

    def print_status(self):
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)
        free_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)

        status = f"Hotel {self.name} has {self.guests} total guests\n"  # TODO wrong calculation of guests, take_room takes rooms even if they are occupied
        status += f"Free rooms: {free_rooms}\n"
        status += f"Taken rooms: {taken_rooms}"
        print(status)
