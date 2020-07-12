import random
import string

no_chars = int(input("Podaj min liczbe znakow w hasle: "))


def get_random_lower_letters():
    lower_letters = random.sample((list(string.ascii_lowercase)), round(no_chars / 2))
    return lower_letters


def get_random_upper_letters():
    upper_letters = random.sample((list(string.ascii_uppercase)), round(no_chars / 2))
    return upper_letters


def get_random_digits():
    digits = random.sample(range(10), round(no_chars / 2))
    return digits


def get_random_special():
    special = random.sample(list(string.punctuation), round(no_chars / 2))
    return special


def create_password():
    characters_used = get_random_lower_letters() + get_random_upper_letters() + get_random_digits() + get_random_special()
    pass_list = random.sample(characters_used, no_chars)
    password = "".join(str(element) for element in pass_list)
    return password


print(create_password())
