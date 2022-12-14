import pytest
from .day6 import part1, part2


def test_case1():
    assert part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19


def test_case2():
    assert part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23


def test_case3():
    assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part2("nppdvjthqldpwncqszvftbrmjlhg") == 23


def test_case4():
    assert part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29


def test_case5():
    assert part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    assert part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26