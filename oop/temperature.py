class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        import pdb

        pdb.set_trace()
        if kelvin < self.min_temperature or kelvin > self.max_temperature:
            raise Exception("Invalid temperature.")
        self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")
        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")
        cls.max_temperature = kelvin
