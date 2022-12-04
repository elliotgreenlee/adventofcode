with open("day1.input", "r") as f:
    max_elves = [0, 0, 0]
    counting_elf = 0
    for line in f:
        if line == '\n':
            for elf_rank, elf in enumerate(max_elves):
                if counting_elf > elf:
                    if elf_rank == 0:
                        max_elves[2] = max_elves[1]
                        max_elves[1] = max_elves[0]
                        max_elves[0] = counting_elf
                    if elf_rank == 1:
                        max_elves[2] = max_elves[1]
                        max_elves[1] = counting_elf
                    if elf_rank == 2:
                        max_elves[2] = counting_elf
                    break
            counting_elf = 0
        else:
            counting_elf += int(line.rstrip())
    print("Part 1: ", max_elves[0])
    print("Part 2: ", sum(max_elves))

