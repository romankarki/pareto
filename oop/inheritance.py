class Animal:

    def speak(self):
        print("sound")


class Cat(Animal):


    def __init__(self):
        super().__init__()

    def speak(self):
        '''
        Docstring for speak
        
        :param self: Description
        Description: this is overriding speak() method by default
        '''
        print("meow")

#example of polymorphism animals and cat are both animal type so 
animals = [Cat(), Animal()]

for a in animals:
    a.speak()