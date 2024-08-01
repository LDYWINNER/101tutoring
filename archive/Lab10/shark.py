
class Shark:
    animal_type = "fish"
    location = "ocean"

    def __init__(self, name, age):
        #print("This is the constructor method.")
        self.name = name
        #self.x = 5
        self.age = age

    def set_followers(self, followers):
        print("This user has " + str(followers) + "followers")
        self.number_of_followers = followers

    def swim(self):
        #print("The shark is swimming.")
        print(self.name + " is swimming.")
        #print(self.x)
        print("Age: ", self.age)

    def be_awesome(self):
        #print("The shark is being awesome.")
        print(self.name + " is being awesome.")


def main():
    s = Shark('Alice', 10)
    s.swim()
    s.be_awesome()

    otherShark = Shark("Stevie", 7)
    otherShark.swim()

    print(otherShark.animal_type)
    print(s.location)

    print("Age: ", s.age)
    print("Age: ", otherShark.age)

    s.set_followers(12)
    print( s.number_of_followers )

if  __name__ == "__main__":
    main()