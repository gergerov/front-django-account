from accounts.exceptions import *

lat_chars_and_nums = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'


def is_correct_request_data(request_data):

    if "username" not in request_data:
        raise IncorrectRequestData

    if "password" not in request_data:
        raise IncorrectRequestData

    if "email" not in request_data:
        raise IncorrectRequestData

