class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RopeGrid:
    def __init__(self):
        self.visited_positions = set()
        self.head = Position(0, 0)
        self.tail = Position(0, 0)

    def simulate(self, direction, steps):
        if direction == 'U':
            self.step_up(steps)
        elif direction == 'D':
            self.step_down(steps)
        elif direction == 'L':
            self.step_left(steps)
        elif direction == 'R':
            self.step_right(steps)
        else:
            print("Error: Unknown Direction command")
            exit(1)

    def decorator(head_movement):
        def step(self, steps):
            for _ in range(steps):
                head_movement(self, steps)
                self.fix_tail()
                self.visited_positions.add((self.tail.x, self.tail.y))  # Set understands tuples but not Positions
        return step

    @decorator
    def step_up(self, steps):
        self.head.y += 1

    @decorator
    def step_down(self, steps):
        self.head.y -= 1

    @decorator
    def step_left(self, steps):
        self.head.x -= 1

    @decorator
    def step_right(self, steps):
        self.head.x += 1

    def fix_tail(self):
        # If the head is ever two steps up, down, left, or right from the tail
        if abs(self.head.y - self.tail.y) > 1 and self.head.y > self.tail.y:  # two steps up
            # If the head is left of tail
            if self.head.x < self.tail.x:
                self.tail.x -= 1  # Move tail left
            # If the head is right of tail
            elif self.tail.x < self.head.x:
                self.tail.x += 1  # Move tail right
            self.tail.y += 1  # Move tail up
        elif abs(self.head.y - self.tail.y) > 1 and self.head.y < self.tail.y:  # two steps down
            # If the head is left of tail
            if self.head.x < self.tail.x:
                self.tail.x -= 1  # Move tail left
            # If the head is right of tail
            elif self.tail.x < self.head.x:
                self.tail.x += 1  # Move tail right
            self.tail.y -= 1  # Move tail down
        elif abs(self.head.x - self.tail.x) > 1 and self.head.x > self.tail.x:  # two steps right
            # If the head is up of tail
            if self.tail.y < self.head.y:
                self.tail.y += 1  # Move tail up
            # If the head is down of tail
            elif self.head.y < self.tail.y:
                self.tail.y -= 1  # Move tail down
            self.tail.x += 1  # Move tail right
        elif abs(self.head.x - self.tail.x) > 1 and self.head.x < self.tail.x:  # two steps left
            # If the head is up of tail
            if self.tail.y < self.head.y:
                self.tail.y += 1  # Move tail up
            # If the head is down of tail
            elif self.head.y < self.tail.y:
                self.tail.y -= 1  # Move tail down
            self.tail.x -= 1  # Move tail left


def part1():
    with open("day9.input") as f:
        rope_grid = RopeGrid()
        for line in f:
            line = line.rstrip().split(' ')
            direction = line[0]
            steps = int(line[1])
            rope_grid.simulate(direction, steps)

        return len(rope_grid.visited_positions)


def part2():
    with open("day9.test") as f:
        for line in f:
            pass


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()