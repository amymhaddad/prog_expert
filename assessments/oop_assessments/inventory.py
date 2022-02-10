class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.total_items = {}
        self.curr_capacity = 0

    def add_item(self, name, price, quantity):
        if (
            name in self.total_items
            or self.curr_capacity + quantity > self.max_capacity
        ):
            return False

        self.total_items[name] = [price, quantity]
        self.curr_capacity += quantity
        return True

    def delete_item(self, name):
        if name not in self.total_items:
            return False
        self.curr_capacity -= self.total_items[name][1]
        del self.total_items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        return [
            key
            for key, val in self.total_items.items()
            if val[0] >= min_price and val[0] <= max_price
        ]

    def get_most_stocked_item(self):
        if self.total_items == {}:
            return None

        max_stocked_item = max(
            [quantity[1] for quantity in self.total_items.values()], default=0
        )

        for name, quantity in self.total_items.items():
            if quantity[1] == max_stocked_item:
                return name
