import random


class Product:
    '''
    - `name` (string with no default)
    - `price` (integer with default value 10)
    - `weight` (integer with default value 20)
    - `flammability` (float with default value 0.5)
    - `identifier` (integer, automatically genererated as a random (uniform) number
    anywhere from 1000000 to 9999999, includisve)(inclusive).
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):

        self.identifier = identifier
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        '''
        `stealability(self)` - calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        '''
        ratio = self.price/self.weight

        if ratio < 0.5:
            print('Not so stealable...')
        elif ratio >= 0.5 and ratio < 1.0:
            print('Kinda steablable.')
        else:
            return 'Very stealable'

    def explode(self):
        '''`explode(self)` - calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.",if it is
        greater or equal to 10 but less than 50 return "...boom!", and otherwise
        return "...BABOOM!!"
        '''

        explosion = self.flammability * self.weight

        if explosion < 10:
            print('...fizzle.')
        elif explosion >= 10 and explosion < 50:
            print('...boom!')
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''
    - Change the default `weight` to 10 (but leave other defaults unchanged)
    - Override the `explode` method to always return "...it's a glove."
    - Add a `punch` method that returns "That tickles." if the weight is below 5,
    "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
    "OUCH!" otherwise
  '''

    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 0.5:
            print('That tickles.')
        elif self.weight >= 5 and self.weight < 15:
            print('Hey that hurt!')
        else:
            return 'OUCH!'
