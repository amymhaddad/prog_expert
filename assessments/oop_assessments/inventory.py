class Inventory:
    def __init__(self, max_capacity):
        #max number of ittems that can be stored in inentory
        self.max_capacity = max_capacity 
        self.total_items = {}
        
    def add_item(self, name, price, quantity):

        inventory_quantity = sum([item[0] for item in self.total_items])
        if name in self.total_items or inventory_quantity + quantity > self.max_capacity:
            return False
        else:
            self.total_items[name] = [price, quantity]
            return True
        

    def delete_item(self, name):
        # Write your code here.
        pass

    def get_items_in_price_range(self, min_price, max_price):
        # Write your code here.
        pass

    def get_most_stocked_item(self):
        # Write your code here.
        pass


i1 = Inventory(3)
print(i1.add_item("t", 5, 5))