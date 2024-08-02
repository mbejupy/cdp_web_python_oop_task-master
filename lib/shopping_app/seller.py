from user import User
from ownable import Owner


class Seller(User, Owner):
    def __init__(self, name):
        super().__init__(name)
