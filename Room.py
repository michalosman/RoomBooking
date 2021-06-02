class Room:

    def __init__(self, room_number, capacity, price):
        self.check_args(room_number, capacity, price)
        self.room_number = room_number
        self.capacity = capacity
        self.price = price

    @staticmethod
    def check_args(room_number, capacity, price):
        if type(room_number) != int:
            raise ValueError('Room number must be of type int')
        if type(capacity) != int:
            raise ValueError('Capacity must be of type int')
        if type(price) != int:
            raise ValueError('Price must be of type int')

    def __str__(self):
        return f'Room number: {self.room_number}\t\tCapacity: {self.capacity}\t\tPrice: {self.price}'

    def str_raw(self):
        return f'{self.room_number}\t\t{self.capacity}\t\t{self.price}'
