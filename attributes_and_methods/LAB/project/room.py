class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.capacity >= people and not self.is_taken:
            self.guests += people
            self.is_taken = True
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"


# Testing
# room = Room(101, 5)
# room.take_room(4)
# print(room.guests)
# room.free_room()
# print(room.guests)
# print(room.free_room())
