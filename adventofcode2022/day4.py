def fully_overlapping(l1, r1, l2, r2):
    # if range2 within range1 or range1 within range2
    return (l1 <= l2 and r2 <= r1) or (l2 <= l1 and r1 <= r2)


def left_overlapping(l1, r1, l2, r2):
    # if r1 inside range2 or l2 inside range1 (should be same thing)
    return (l2 <= r1 <= r2) or (l1 <= l2 <= r1)


def right_overlapping(l1, r1, l2, r2):
    # if l1 inside range2 or r2 inside range1 (should be same thing)
    return (l2 <= l1 <= r2) or (l1 <= r2 <= r1)


def overlapping(l1, r1, l2, r2):
    return fully_overlapping(l1, r1, l2, r2) or left_overlapping(l1, r1, l2, r2) or right_overlapping(l1, r1, l2, r2)


with open("day4.input") as f:
    overlapping_pairs = 0
    for line in f:
        elf1, elf2 = line.split(',')
        elf1L, elf1R = elf1.split('-')
        elf1L = int(elf1L)
        elf1R = int(elf1R)
        elf2L, elf2R = elf2.split('-')
        elf2L = int(elf2L)
        elf2R = int(elf2R)

        if overlapping(elf1L, elf1R, elf2L, elf2R):
            overlapping_pairs += 1

    print(overlapping_pairs)

