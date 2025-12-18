import string
import random


class RandomFactory:
    STRING_LENGTH = 10

    def get_random_string(self):
        return "".join(random.choice(string.ascii_letters) for i in range(self.STRING_LENGTH))
