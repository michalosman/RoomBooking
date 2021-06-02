from Reservation import Reservation
import datetime


class ReservationsData:

    def __init__(self):
        self.reservations = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open('data/reservations.txt') as file:
                for line in file:
                    words = line.split()
                    if len(words) == 4:
                        client_id_number = words[0]
                        room_number = words[1]
                        start_date = words[2]
                        end_date = words[3]
                        try:
                            room_number = int(room_number)
                            start_date = datetime.datetime.strptime(start_date, f'%Y-%m-%d').date()
                            end_date = datetime.datetime.strptime(end_date, f'%Y-%m-%d').date()
                            reservation = Reservation(client_id_number, room_number, start_date,
                                                      end_date)
                        except ValueError:
                            pass
                        else:
                            self.reservations.append(reservation)
        except FileNotFoundError as e:
            raise FileNotFoundError(f'{e.filename} does not exist')

    def save_to_file(self):
        result = ''
        for reservation in self.reservations:
            result += f'{reservation.str_raw()}\n'
        with open('data/reservations.txt', 'w') as file:
            file.write(result)

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
        if argument != 'client id number' and argument != 'room number' and argument != 'start date':
            raise ValueError('Sort argument must be either "client id number", "room number" or "start date"')
        if argument == 'client id number':
            return sorted(self.reservations, key=lambda reservation: reservation.client_id_number)
        if argument == 'room number':
            return sorted(self.reservations, key=lambda reservation: reservation.room_number)
        if argument == 'start date':
            return sorted(self.reservations, key=lambda reservation: reservation.start_date)

    def get_sorted_descending(self, argument):
        argument = argument.lower()
        if argument != 'client id number' and argument != 'room number' and argument != 'start date':
            raise ValueError('Sort argument must be either "client id number", "room number" or "start date"')
        if argument == 'client id number':
            return reversed(sorted(self.reservations, key=lambda reservation: reservation.client_id_number))
        if argument == 'room number':
            return reversed(sorted(self.reservations, key=lambda reservation: reservation.room_number))
        if argument == 'start date':
            return reversed(sorted(self.reservations, key=lambda reservation: reservation.start_date))

    def add_reservation(self, client_id_number, room_number, start_date, end_date):
        try:
            room_number = int(room_number)
            start_date = datetime.datetime.strptime(start_date, f'%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, f'%Y-%m-%d').date()
            new_reservation = Reservation(client_id_number, room_number, start_date, end_date)
        except ValueError:
            raise ValueError('Wrong reservation arguments')
        else:
            self.reservations.append(new_reservation)
            self.save_to_file()

    def remove_reservation(self, room_number, start_date, end_date):
        try:
            room_number = int(room_number)
            start_date = datetime.datetime.strptime(start_date, f'%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, f'%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Wrong reservation arguments')
        else:
            self.reservations = list(filter(lambda reservation:
                                            not (reservation.room_number == room_number and
                                                 reservation.start_date == start_date and
                                                 reservation.end_date == end_date)
                                            , self.reservations))
            self.save_to_file()

    def get_client_reservations(self, client_id_number):
        return list(filter(lambda reservation: reservation.client_id_number == client_id_number, self.reservations))

    def get_vacant_rooms(self, rooms, start_date, end_date):
        try:
            start_date = datetime.datetime.strptime(start_date, f'%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date, f'%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Invalid date format, must be YYYY-MM-DD')

        given_date_reservations = list(filter(
            lambda reservation: not (
                    reservation.start_date < start_date and reservation.end_date < start_date or
                    reservation.start_date > end_date and reservation.end_date > end_date),
            self.reservations))

        reserved_room_numbers = []
        for reservation in given_date_reservations:
            reserved_room_numbers.append(reservation.room_number)

        vacant_rooms = list(filter(lambda room: room.room_number not in reserved_room_numbers, rooms))
        return vacant_rooms

    def __str__(self):
        result = ''
        for reservation in self.reservations:
            result += f'{str(reservation)}\n'
        return result
