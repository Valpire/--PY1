from random import choice
from string import ascii_letters, digits


def get_random_password() -> str:
    n = 8
    password_elements = ascii_letters + digits
    password = ''.join(choice(password_elements) for _ in range(n))
    return password


print(get_random_password())
