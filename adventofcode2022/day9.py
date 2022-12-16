class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RopeGrid:
    def __init__(self, rope_length):
        self.rope_length = rope_length

        self.visited_positions = set()

        self.rope = [Position(0, 0) for i in range(self.rope_length)]
        self.HEAD_POSITION = 0
        self.TAIL_POSITION = self.rope_length - 1

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
                # Add tail position to visited positions set. Sets understand tuples but not Positions
                self.visited_positions.add((self.rope[self.rope_length-1].x, self.rope[self.rope_length-1].y))
        return step

    @decorator
    def step_up(self, steps):
        self.rope[self.HEAD_POSITION].y += 1

    @decorator
    def step_down(self, steps):
        self.rope[self.HEAD_POSITION].y -= 1

    @decorator
    def step_left(self, steps):
        self.rope[self.HEAD_POSITION].x -= 1

    @decorator
    def step_right(self, steps):
        self.rope[self.HEAD_POSITION].x += 1

    def fix_tail(self):
        # Iterate over each rope duo
        front = self.HEAD_POSITION
        for back in range(1, self.rope_length):
            # If the front is ever two steps up, down, left, or right from the back
            if abs(self.rope[front].y - self.rope[back].y) > 1\
                    and self.rope[front].y > self.rope[back].y:  # two steps up
                # If the front is left of back
                if self.rope[front].x < self.rope[back].x:
                    self.rope[back].x -= 1  # Move back left
                # If the front is right of back
                elif self.rope[back].x < self.rope[front].x:
                    self.rope[back].x += 1  # Move back right
                self.rope[back].y += 1  # Move back up
            elif abs(self.rope[front].y - self.rope[back].y) > 1\
                    and self.rope[front].y < self.rope[back].y:  # two steps down
                # If the front is left of tail
                if self.rope[front].x < self.rope[back].x:
                    self.rope[back].x -= 1  # Move back left
                # If the front is right of tail
                elif self.rope[back].x < self.rope[front].x:
                    self.rope[back].x += 1  # Move back right
                self.rope[back].y -= 1  # Move back down
            elif abs(self.rope[front].x - self.rope[back].x) > 1\
                    and self.rope[front].x > self.rope[back].x:  # two steps right
                # If the front is up of tail
                if self.rope[back].y < self.rope[front].y:
                    self.rope[back].y += 1  # Move back up
                # If the front is down of tail
                elif self.rope[front].y < self.rope[back].y:
                    self.rope[back].y -= 1  # Move back down
                self.rope[back].x += 1  # Move back right
            elif abs(self.rope[front].x - self.rope[back].x) > 1\
                    and self.rope[front].x < self.rope[back].x:  # two steps left
                # If the front is up of tail
                if self.rope[back].y < self.rope[front].y:
                    self.rope[back].y += 1  # Move back up
                # If the front is down of tail
                elif self.rope[front].y < self.rope[back].y:
                    self.rope[back].y -= 1  # Move back down
                self.rope[back].x -= 1  # Move back left

            # Move down the rope
            front = back


def part1():
    with open("day9.input") as f:
        rope_grid = RopeGrid(2)
        for line in f:
            line = line.rstrip().split(' ')
            direction = line[0]
            steps = int(line[1])
            rope_grid.simulate(direction, steps)

        return len(rope_grid.visited_positions)


def part2():
    with open("day9.input") as f:
        rope_grid = RopeGrid(10)
        for line in f:
            line = line.rstrip().split(' ')
            direction = line[0]
            steps = int(line[1])
            rope_grid.simulate(direction, steps)

        return len(rope_grid.visited_positions)


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()