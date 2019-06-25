import os
import random


class PasswordLengthTooShortException(Exception):
    pass


PASSWORD_LENGTH = 16
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`"
digits = "0123456789"
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"


def generate_password(n):
    ''' Randomly generate a strong password of n characters long. '''
    if n < 4:
        raise PasswordLengthTooShortException("Cannot generate a password of "
                                              "less than 4 characters.")
    seeds = list(os.urandom(n+1))
    password = [
        symbols[seeds[1] % len(symbols)],
        digits[seeds[2] % len(digits)],
        capitals[seeds[3] % len(capitals)],
        lowers[seeds[4] % len(lowers)]
    ]
    for i, seed in enumerate(seeds[5:]):
        switch = os.urandom(1)[0] % 4
        if switch == 0:
            password.append(symbols[seeds[i] % len(symbols)])
        elif switch == 1:
            password.append(digits[seeds[i] % len(digits)])
        elif switch == 2:
            password.append(capitals[seeds[i] % len(capitals)])
        elif switch == 3:
            password.append(lowers[seeds[i] % len(lowers)])
    random.Random(seeds[0]).shuffle(password)
    password = "".join(password)
    return password