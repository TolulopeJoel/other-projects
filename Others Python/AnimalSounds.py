# inheritance
class Mammal:
    def __init__(self, mammal_first_name, mammal_last_name):
        self.mammal_first_name = mammal_first_name
        self.mammal_last_name = mammal_last_name

    def bark(self):
        bark_sound = input(f'Give me your best bark {self.mammal_first_name} {self.mammal_last_name}>> ')
        if len(bark_sound) < 10:
            print(f'{bark_sound} is a really good sound {self.mammal_first_name} {self.mammal_last_name}, but is that '
                  f'your best? ')
        else:
            print(f'woooow, nice one there {self.mammal_first_name} {self.mammal_last_name},'
                  f' never knew you were this good, neither did i underestimate you')

    def meow(self):
        long_meow = input('For how long can you Meow Catty> ')
        if len(long_meow) < 10:
            print(
                f'{long_meow} is how long you can go {self.mammal_first_name} {self.mammal_last_name}??, not IMPRESSIVE'
                f'at all🤧 ')
        else:
            print(f'niCE one {self.mammal_first_name} {self.mammal_last_name}😃')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


roddy = Dog(input('Dog\'s First Name>> '), input('Dog\'s Last Name>> '))
roddy.bark()

sofia = Cat(input('Cat\'s First Name>> '), input('Cat\'s Last Name>> '))
sofia.meow()
