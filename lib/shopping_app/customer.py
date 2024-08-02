from user import User
from cart import Cart
from ownable import Owner


class Customer(User, Owner):
    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)