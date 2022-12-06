def find_common(rucksacks):
    for item in rucksacks[0]:
        in_all = True
        for rucksack in rucksacks[1:]:
            if item not in rucksack:
                in_all = False
                break
        if in_all:
            return item


def priority(letter):
    if letter.islower():  # (a-z)
        return int(ord(letter[0]) - ord('a')) + 1
    if letter.isupper():  # (A-Z)
        return int(ord(letter[0]) - ord('A')) + 27


with open("day3.input") as f:
    total_priority = 0
    for line in f:
        rucksack1 = line.rstrip()[len(line)//2:]
        rucksack2 = line.rstrip()[:len(line)//2]
        common_item = find_common([set(rucksack1), set(rucksack2)])
        total_priority += priority(common_item)
    print(total_priority)

with open("day3.input") as f:
    total_priority = 0
    lines = list(f)
    for i in range(len(lines)//3):
        # Normally you should check in case it's not a multiple of 3
        rucksacks = [
            set(lines[i*3].rstrip()),
            set(lines[i*3+1].rstrip()),
            set(lines[i*3+2].rstrip())
        ]
        common_item = find_common(rucksacks)
        total_priority += priority(common_item)
    print(total_priority)
