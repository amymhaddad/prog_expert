class Temperature:
    min_temperature = 0
    max_temperature = 1000 

    def __init__(self, kelvin):
        self.kelvin = self.is_valid(kelvin)

    def is_valid(self, kelvin):
        if kelvin < Temperature.min_temperature or kelvin > Temperature.max_temperature:
            raise ValueError("Invalid temperature")
        else:
           # import pdb; pdb.set_trace()
            return 

    @classmethod
    def update_min_temperature(cls, kelvin):
        try:
            cls.min_temperature += kelvin
        except ValueError as e:

        cls.min_temperature += kelvin
        if cls.min_temperature > cls.max_temperature or cls.min_temperature <= 0:
            raise ValueError("Invalid temperature")
        else:
            return cls.min_temperature

    @classmethod
    def update_max_temperature(cls, kelvin):
        cls.max_temperature += kelvin
        if cls.max_temperature < cls.min_temperature or cls.max_temperature >= 1000:
            raise ValueError("Invalid temperature")
        else:
            return cls.max_temperature

temperature = Temperature(60)
Temperature.update_max_temperature(100)
print(temperature.max_temperature, temperature.min_temperature)
