from collections import deque
import string


class Crates:
    def __init__(self, number_of_stacks):
        self.data = [deque() for i in range(number_of_stacks)]   # list of stacks

    def add(self, index, crate):
        self.data[index].append(crate)

    # Write function to move one crate top to top
    def move(self, count, start, finish):
        tmp_stack = deque()
        for i in range(count):
            tmp_stack.append(self.data[start].pop())
        for i in range(count):
            self.data[finish].append(tmp_stack.pop())
        pass

    # Print the top of each stack
    def print_tops(self):
        for stack in self.data:
            print(stack.pop(), end='')

    def print_stacks(self):
        for stack in self.data:
            print(stack)


with open("day5.input") as f:
    # Store each line into a queue, until I hit the blank space
    crates_input_queue = deque()
    line = f.readline()
    while line != '\n':
        crates_input_queue.append(line)
        line = f.readline()

    number_of_stacks = int(crates_input_queue.pop()[-2])
    crates = Crates(number_of_stacks)
    while crates_input_queue:
        line = crates_input_queue.pop()
        i = 1
        crate_index = 0
        for stack in range(number_of_stacks):
            if i < len(line):
                print(line[i], end='')
                if line[i] != ' ':
                    crates.add(crate_index, line[i])
            else:
                print(' ', end='')
            i += 4
            crate_index += 1
        print()

    for line in f:
        # for each line parse in the crate_moves, start, and finish
        _, crate_moves, _, start, _, finish = line.rstrip().split(' ')
        print(crate_moves, start, finish)
        # Part 1 call the move function crate_moves times for start and finish
        # for crate_move in range(int(crate_moves)):
            # crates.move(int(start)-1, int(finish)-1)
        # Part 2 call the move function
        crates.move(int(crate_moves), int(start)-1, int(finish)-1)

    crates.print_tops()
