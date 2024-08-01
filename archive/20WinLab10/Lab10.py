# Chap 34 ~ 37

# Chap 34 How to use *args and **kwargs
def multiply(x, y):
    print(x * y)

multiply(5, 4)
# multiply(5, 4, 3)

def multiplY(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiplY(5, 4, 3, 2)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwargs1 = 'Shark', kwargs2 = 4.5, kwargs3 = True)

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name = "Sammy", your_name = "Casey")
print()
print_values(
name_1="Alex",
name_2="Gray",
name_3="Harper",
name_4="Phoenix",
name_5="Remy",
name_6="Val"
)
print()
# argument's order
# --> 1. formal positional arguments
# --> 2. *args
# --> 3. keyword arguments
# --> 4. **kwargs
def example(arg_1, arg_2, *args, **kwargs):
    return

def example2(arg_1, arg_2, *args, kw_1 = 'shark', kw_2 = 'blobfish', **kwargs):
    return

def some_args(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)

args = ('Sammy', 'Casey', 'Alex')
some_args(*args)
print()

myList = [2, 3]
some_args(1, *myList)
print()

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {"kwarg_1": "Bal", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**kwargs)
print()

# Chap 35 How to construct classes and define objects
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print(self.name + ' is swimming.')

    def be_awesome(self):
        print(self.name + ' is being awesome.')

def main():
    sammy = Shark("Sammy", 5)
    sammy.be_awesome()
    stevie = Shark('Stevie', 7)
    stevie.swim()
if __name__ == '__main__':
    main()
print()

# Chap 36 Understanding class and instance variables
class Shark:
    animal_type = 'fish'
    location = 'ocean'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        print('This user has ' + str(followers) + " followers.")

new_shark = Shark('Sammy', 5)
print(new_shark.animal_type)
print(new_shark.location)
print()
print(new_shark.name)
print(new_shark.age)
print()
stevie = Shark('stevie', 8)
print(stevie.name)
print(stevie.age)
print()
stevie.set_followers(77)
print()

# Chap 37 Understanding inheritance
class Fish:
    def __init__(self, first_name, last_name = 'Fish', skeleton='bone',
                 eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print('The fish is swimming')

    def swim_backwards(self):
        print('The fish can swim backwards')

class Trout(Fish):
    pass

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
print()

class Clownfish(Fish):
    def live_with_anemone(self):
        print('The clownfish is coexisting with sea anemone.')

casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()
print()

class Shark(Fish):
    def __init__(self, first_name, last_name='Shark', skeleton='cartilage',
                 eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print('The shark cannot swim backwards, but can sink backwards.')

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
print()

class Trout(Fish):
    def __init__(self, water='freshwater'):
        self.water = water
        super().__init__(self)

terry = Trout()
# Initialize first name
terry.first_name = "Terry"
# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
# Use child __init__() override
print(terry.water)
# Use parent swim() method
terry.swim()
print()

class Coral:
    def community(self):
        print('Coral lives in a community')

class Anemone:
    def protect_clownfish(self):
        print('The anemone is protecting the clownfish')

class CoralReef(Coral, Anemone):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()