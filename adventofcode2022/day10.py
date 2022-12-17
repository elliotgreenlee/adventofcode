
class Register:
    def __init__(self):
        self.x = 1
        self.history_x = []
        self.history_x.append(0)
        self.history_x.append(1)
        self.cycle = 1

        self.crt = []
        if self.cycle % 40 == self.x-1 or self.cycle % 40 == self.x or self.cycle % 40 == self.x+1:
            self.crt.append('#')
        else:
            self.crt.append('.')

    def simulate(self, lines):
        for line in lines:
            instruction = line.rstrip().split(' ')
            if instruction[0] == "noop":

                self.history_x.append(self.x)

                if self.cycle % 40 == self.x-1 or self.cycle % 40 == self.x or self.cycle % 40 == self.x+1:
                    self.crt.append('#')
                else:
                    self.crt.append('.')

                self.cycle += 1

            elif instruction[0] == "addx":

                self.history_x.append(self.x)

                if self.cycle % 40 == self.x-1 or self.cycle % 40 == self.x or self.cycle % 40 == self.x+1:
                    self.crt.append('#')
                else:
                    self.crt.append('.')
                self.cycle += 1

                self.x += int(instruction[1])
                self.history_x.append(self.x)

                if self.cycle % 40 == self.x-1 or self.cycle % 40 == self.x or self.cycle % 40 == self.x+1:
                    self.crt.append('#')
                else:
                    self.crt.append('.')
                self.cycle += 1


def part1():
    with open("day10.input") as f:
        lines = list(f)
        register = Register()
        register.simulate(lines)

        sum = 0
        cycle = 20
        while cycle < len(register.history_x):

            next_sum = cycle * register.history_x[cycle]
            sum += next_sum
            cycle += 40

        return sum


def part2():
    with open("day10.input") as f:
        lines = list(f)
        register = Register()
        register.simulate(lines)

        cycle = 1
        for pixel in register.crt:
            print(pixel, end='')
            if cycle % 40 == 0:
                print()
            cycle += 1


def main():
    print(part1())
    part2()


if __name__ == "__main__":
    main()
