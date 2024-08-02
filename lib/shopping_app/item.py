from ownable import Owner


class Item(Owner):
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        return Item.instances
