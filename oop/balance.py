class BankAccount:

    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def set_balance(self, amount):
        invalid_amount_type = type(amount) not in [int, float]:

        if invalid_amount_type or amount < 0 or amount > 100000:
            return 

        self._balance = amount

    def get_balance(self):
        return round(self._balance)
