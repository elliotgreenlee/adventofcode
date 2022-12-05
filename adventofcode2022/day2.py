from enum import Enum


class OutcomeScore(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


class ShapeScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Scoring matrix for part 1
# - A (rock) B (paper) C (scissors)
# X (rock)
# Y (paper)
# Z (scissors)
score_matrix1 = [
    [ShapeScore.ROCK.value + OutcomeScore.DRAW.value, ShapeScore.ROCK.value + OutcomeScore.LOSE.value, ShapeScore.ROCK.value + OutcomeScore.WIN.value],
    [ShapeScore.PAPER.value + OutcomeScore.WIN.value, ShapeScore.PAPER.value + OutcomeScore.DRAW.value, ShapeScore.PAPER.value + OutcomeScore.LOSE.value],
    [ShapeScore.SCISSORS.value + OutcomeScore.LOSE.value, ShapeScore.SCISSORS.value + OutcomeScore.WIN.value, ShapeScore.SCISSORS.value + OutcomeScore.DRAW.value]
]

# Scoring matrix for part 2
# - A (rock) B (paper) C (scissors)
# X (lose)
# Y (draw)
# Z (win)
score_matrix2 = [
    [OutcomeScore.LOSE.value + ShapeScore.SCISSORS.value, OutcomeScore.LOSE.value + ShapeScore.ROCK.value, OutcomeScore.LOSE.value + ShapeScore.PAPER.value],
    [OutcomeScore.DRAW.value + ShapeScore.ROCK.value, OutcomeScore.DRAW.value + ShapeScore.PAPER.value, OutcomeScore.DRAW.value + ShapeScore.SCISSORS.value],
    [OutcomeScore.WIN.value + ShapeScore.PAPER.value, OutcomeScore.WIN.value + ShapeScore.SCISSORS.value, OutcomeScore.WIN.value + ShapeScore.ROCK.value]
]


with open("day2.input") as f:
    total_score = 0
    for line in f:

        elf_play, my_play = line.rstrip().split(' ')
        elf_play = int(ord(elf_play[0]) - ord('A'))
        my_play = int(ord(my_play[0]) - ord('X'))
        total_score += score_matrix2[my_play][elf_play]
    print(total_score)
