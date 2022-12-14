START_OF_PACKET_MARKER_LENGTH = 4
START_OF_MESSAGE_MARKER_LENGTH = 14


def validate_packet(packet):
    for letter in packet:
        if packet.count(letter) > 1:
            return False
    return True


def part1(stream):
    for i in range(len(stream) - START_OF_PACKET_MARKER_LENGTH):
        if validate_packet(stream[i:i+START_OF_PACKET_MARKER_LENGTH]):
            return i + START_OF_PACKET_MARKER_LENGTH


def part2(stream):
    for i in range(len(stream) - START_OF_MESSAGE_MARKER_LENGTH):
        if validate_packet(stream[i:i+START_OF_MESSAGE_MARKER_LENGTH]):
            return i + START_OF_MESSAGE_MARKER_LENGTH


def main():
    with open("day6.input") as f:
        line = f.readline().rstrip()
        print(part1(line))
        print(part2(line))


if __name__ == "__main__":
    main()
