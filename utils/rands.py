from string import ascii_lowercase, digits
from random import SystemRandom
from django.utils.text import slugify


def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        ascii_lowercase + digits,
        k=k,
    ))


def slugify_new(text):
    return slugify(text) + '-' + random_letters()