from generate_numbers import generate_private_key

class Device:
    def __init__(self):
        self.__key = generate_private_key()
        self.__finalkey = None
        self.keyg = None

    def calc_keyg(self, g, n):
        self.keyg = g ** self.__key % n
        return self.keyg

    def calc_final_key(self, keyg, n):
        self.__finalkey = keyg ** self.__key % n
        print(f"final key: {self.__finalkey}")
