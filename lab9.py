import matplotlib.pyplot as plt
import random
import landscape


class Sled:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.position = random.randint(-10, 10)

    def move(self):
        new_position = self.position - self.speed * landscape.slope(self.position)
        return new_position

    def found_treasure(self, treasure_position, threshold):
        if abs(treasure_position - self.move()) < threshold:
            return True
        else:
            return False


def main():
    x = [i / 10 for i in range(-100, 100)]
    y = [landscape.elevation(i) for i in x]
    plt.plot(x, y, label='Landscape')
    plt.xlabel("position")
    plt.ylabel("elevation")

    Joe = Sled("Joe", 0.05)
    Jack = Sled("Jack", 0.1)
    John = Sled("John", 0.08)

    thresh_treas = 0.05
    treasure_position = -1.3

    winner = "nobody"
    for _ in range(60):
        plt.plot(Joe.position, landscape.elevation(Joe.position), "og")
        plt.plot(Jack.position, landscape.elevation(Jack.position), "ob")
        plt.plot(John.position, landscape.elevation(John.position), "or")

        if Joe.found_treasure(treasure_position, thresh_treas):
            winner = Joe.name
            break
        elif Jack.found_treasure(treasure_position, thresh_treas):
            winner = Jack.name
            break
        elif John.found_treasure(treasure_position, thresh_treas):
            winner = John.name
            break

        Joe.position = Joe.move()
        Jack.position = Jack.move()
        John.position = John.move()

    print(winner, "is winning")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
