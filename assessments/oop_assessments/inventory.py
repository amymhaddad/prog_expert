class Inventory:
    def __init__(self, max_capacity):
        #max number of ittems that can be stored in inentory
        self.max_capacity = max_capacity 
        self.total_items = {}
        self.curr_capacity = 0
        
    def add_item(self, name, price, quantity):

      # inventory_quantity = sum([item[0] for item in self.total_items])
        #import pdb; pdb.set_trace()
        if name in self.total_items or self.curr_capacity + quantity > self.max_capacity:
            return False
        else:   
            self.total_items[name] = [price, quantity]
            self.curr_capacity += quantity
            return True    

    def delete_item(self, name):
        if name not in self.total_items:
            return False
        
        #import pdb; pdb.set_trace()
        self.curr_capacity -= self.total_items[name][1]
        del self.total_items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        items_in_price_range = []
        for key, val in self.total_items.items():
            if val[0] >= min_price and val[0] <= max_price:
                items_in_price_range.append(key)
        return items_in_price_range

    def get_most_stocked_item(self):

        #Check for none values and check if items have the same amount -- ie, quantities are both 2. In this case, I can't use max
        import pdb; pdb.set_trace()
        max_stocked_item = max([quantity[1]    for quantity in self.total_items.values()], default=0)

        for key, val in self.total_items.items():
            if val[1] == max_stocked_item:
                return key

inventory = Inventory(4)
inventory.add_item('Chocolate', 4.99, 4)
inventory.delete_item('Chocolate')
inventory.delete_item('Chocolate')
inventory.delete_item('Bread')
inventory.add_item('Chocolate', 4.99, 2)
inventory.add_item('Bread', 4.99, 2)

#print(inventory.total_items) 
print(inventory.get_most_stocked_item())
