import string
import random


class RandomFactory:
    DEFAULT_STRING_LENGTH = 10

    @staticmethod
    def get_random_string(string_length: int = DEFAULT_STRING_LENGTH):
        return "".join(random.choice(string.ascii_letters) for _ in range(RandomFactory.DEFAULT_STRING_LENGTH))
