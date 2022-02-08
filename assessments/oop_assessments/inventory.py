class Inventory:
    def __init__(self, max_capacity):
        #max number of ittems that can be stored in inentory
        self.max_capacity = max_capacity 
        self.total_items = {}
        self.curr_capacity = 0
        
    def add_item(self, name, price, quantity):

      # inventory_quantity = sum([item[0] for item in self.total_items])
        if name in self.total_items or self.curr_capacity + quantity > self.max_capacity:
            return False
        else:
            self.total_items[name] = [price, quantity]
            self.curr_capacity += quantity
            return True    

    def delete_item(self, name):
        if name not in self.total_items:
            return False
        del self.total_items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        # Write your code here.
        pass

    def get_most_stocked_item(self):
        
        max_stocked_item = max(quantity[1]    for quantity in self.total_items.values())


item1 = Inventory(50)
item1.add_item("item1", 5, 2)
item1.add_item("item2", 5, 3)
print(item1.get_most_stocked_item())
# item1.add_item("item3", 5, 2)


