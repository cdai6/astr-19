class animal:

    def print(self):
        print(f"length of the arms is {self.len_arm} cm")
        print(f"length of the legs is {self.len_leg} cm")
        print(f"number of eyes is {self.num_arm}")
        print(f"does it have a tail? {self.tail}")
        print(f"is it furry? {self.furry}")

    def __init__(self, a=50, b=50, c=2, d=True, e=True):
        self.len_arm = a
        self.len_leg = b
        self.num_arm = c
        self.tail = d
        self.furry = e


def main():
    animals = animal()
    animals.print()


if __name__ == '__main__':
    main()
