from Room import Room


class RoomsData:

    def __init__(self):
        self.rooms = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open('data/rooms.txt') as file:
                for line in file:
                    words = line.split()
                    if len(words) == 3:
                        room_number = words[0]
                        capacity = words[1]
                        price = words[2]
                        try:
                            room_number = int(room_number)
                            capacity = int(capacity)
                            price = int(price)
                            room = Room(room_number, capacity, price)
                        except ValueError:
                            pass
                        else:
                            self.rooms.append(room)
        except FileNotFoundError as e:
            raise FileNotFoundError(f'{e.filename} does not exist')

    def get_sorted(self, order, argument):
        order = order.lower()
        if order != 'ascending' and order != 'descending':
            raise ValueError('Sort order must be either "ascending" or "descending"')
        if order == 'ascending':
            return self.get_sorted_ascending(argument)
        if order == 'descending':
            return self.get_sorted_descending(argument)

    def get_sorted_ascending(self, argument):
        argument = argument.lower()
        if argument != 'room number' and argument != 'capacity' and argument != 'price':
            raise ValueError('Sort argument must be either "room number", "capacity" or "price"')
        if argument == 'room number':
            return sorted(self.rooms, key=lambda room: room.room_number)
        if argument == 'capacity':
            return sorted(self.rooms, key=lambda room: room.capacity)
        if argument == 'price':
            return sorted(self.rooms, key=lambda room: room.price)

    def get_sorted_descending(self, argument):
        argument = argument.lower()
        if argument != 'room number' and argument != 'capacity' and argument != 'price':
            raise ValueError('Sort argument must be either "room number", "capacity" or "price"')
        if argument == 'room number':
            return reversed(sorted(self.rooms, key=lambda room: room.room_number))
        if argument == 'capacity':
            return reversed(sorted(self.rooms, key=lambda room: room.capacity))
        if argument == 'price':
            return reversed(sorted(self.rooms, key=lambda room: room.price))

    def __str__(self):
        result = ''
        for room in self.rooms:
            result += f'{str(room)}\n'
        return result
