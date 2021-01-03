

"""
Create the following classes using class inheretence
1: Animal
2: Fish
3: Tuna
4: Mammal
5: Dolphin

make sure the following will run: (>> CODE -> OUTPUT)

>> billy = Tuna()
>> billy.live -> "sea"
>> billiy.predator -> True
>> billy.cat -> "fish"
>> billiy.water_type() -> "freashwater"
>> billiy.reproduce() -> "laying eggs"

>> steve = Dolphin()
>> steve.live -> "sea"
>> steve.predator -> True
>> steve.cat -> "mamal"
>> steve.reproduce() -> "giving birth"
>> steve.talk() -> "squeak squeak!"


make sure following will fail /not run:
>> bob = fish()
>> steve.water_type()
>> billy.talk()

retrictions:

1) you should not be able to create an object that is only an animal or fish, it has to be a individual species (e.g. tuna)
2) you should fill in the variables and functions as soon as possible in the hierarchy, i.e. variable "cat" 
should not be defined in e.g. Dolphin
3) make sure that creation of a class without category functions are impossible, e.g. throws and error. I.e. you should not
be able to create a species of fish, e.g. salmon without specifying water_type()


"""


# Define classes.
class Animal:
    
    def __init__(self, cat, live, predator):
        self.cat = cat
        self.live = live
        self.predator = predator
    
    def __new__(cls, *args, **kwargs):
        if cls is __class__:
            raise TypeError(f'Base class {__class__} cannot be instantiated.')
        return object.__new__(cls, *args, **kwargs)

        
class Fish(Animal):
    
    __reproduce = 'laying eggs'
    __water_type = 'freshwater'

    def __init__(self, predator):
        super().__init__('fish', 'sea', predator)
    
    def __new__(cls, *args, **kwargs):
        if cls is __class__:
            raise TypeError(f'Base class {__class__} cannot be instantiated.')
        return object.__new__(cls, *args, **kwargs)
        
    def reproduce(self):
        return __class__.__reproduce

    def water_type(self):
        return __class__.__water_type

    
class Tuna(Fish):
    
    def __init__(self):
        super().__init__(True)

        
class Mammal(Animal):
    
    __reproduce = 'giving birth'
    __talk = 'squeak squeak!'
    
    def __init__(self, live, predator):
        super().__init__('mammal', live, predator)

    def __new__(cls, *args, **kwargs):
        if cls is __class__:
            raise TypeError(f'Base class {__class__} cannot be instantiated.')
        return object.__new__(cls, *args, **kwargs)
    
    def reproduce(self):
        return __class__.__reproduce
    
    def talk(self):
        return __class__.__talk

    
class Dolphin(Mammal):
    
    def __init__(self):
        super().__init__('sea', True)


# Instantiate object of Tuna.
billy = Tuna()


if __name__ == '__main__:

    # Print values.
    print(billy.live)
    print(billy.predator)
    print(billy.cat)
    print(billy.water_type())
    print(billy.reproduce())

    # Perform assertions.
    assert billy.live == 'sea'
    assert billy.predator == True
    assert billy.cat == 'fish'
    assert billy.water_type() == 'freshwater'
    assert billy.reproduce() == 'laying eggs'


    # Instantiate object of Dolphin.
    steve = Dolphin()

    # Print values.
    print(steve.live)
    print(steve.predator)
    print(steve.cat)
    print(steve.reproduce())
    print(steve.talk())

    # Perform assertions.
    assert steve.live == 'sea'
    assert steve.predator == True
    assert steve.cat == 'mammal'
    assert steve.reproduce() == 'giving birth'
    assert steve.talk() == 'squeak squeak!'


    # Expect TypeErrors.
    bob = Fish()
    a = Animal()

    # Expect AttributeError.
    steve.water_type()
    billy.talk()
