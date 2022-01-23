class Temperature:
    min_temperature = 0
    max_temperature = 1000 

    def __init__(self, kelvin):
        if kelvin < Temperature.min_temperature or kelvin >= Temperature.max_temperature:
            raise ValueError("Invalid temperature")
        self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.min_temperature:
            raise ValueError("Invalid temperature")
        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise ValueError("Invalid temperature")
        cls.max_temperature = kelvin