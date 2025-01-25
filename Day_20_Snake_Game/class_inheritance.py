class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(selfs):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()  #Initializes everything from the super class (Animal class) within the new object
    def breathe(self):
        super().breathe()
        print("doing this underwater") #modify the breathe it got from the animal class

    def swim(self):
        print("move in water")

nemo = Fish()
nemo.swim()
nemo.breathe()

#Take an exisitng class and edit it for our needs