import datetime


class Reservation:

    def __init__(self, client_id_number, room_number, start_date, end_date):
        self.check_args(client_id_number, room_number, start_date, end_date)
        self.client_id_number = client_id_number
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def check_args(client_id_number, room_number, start_date, end_date):
        if type(client_id_number) != str:
            raise ValueError('Client ID number must be of type str')
        if type(room_number) != int:
            raise ValueError('Room number must be of type int')
        if type(start_date) != datetime.date:
            raise ValueError('Start date must be of type datetime.date')
        if type(end_date) != datetime.date:
            raise ValueError('End date must be of type datetime.date')

    def __str__(self):
        return f'Client ID Number: {self.client_id_number}\t' \
               f'Room number: {self.room_number}\tStart date: {self.start_date}\t\tEnd date: {self.end_date}'

    def str_raw(self):
        return f'{self.client_id_number}\t\t{self.room_number}\t\t{self.start_date}\t\t' \
               f'{self.end_date}'
