class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

        self.parent = None
        self.children = {}


class FileSystem:
    def __init__(self, lines):
        self.root = File(name='/', size=0)
        self.user_location = self.root

        self.lines = lines
        self.command_index = 0  # controlled by each command
        while self.command_index < len(self.lines) - 1:
            self.command_parse()

    def command_parse(self):
        line = self.lines[self.command_index].rstrip().split(' ')
        if line[1] == 'cd':
            self.cd_parse(line[2])
        elif line[1] == 'ls':
            self.ls_parse()

    def cd_parse(self, argument):
        self.command_index += 1
        if argument == '/':
            self.cd_home()
        elif argument == '..':
            self.cd_out()
        else:
            self.cd_in(argument)

    def cd_in(self, child_name):
        self.user_location = self.user_location.children[child_name]

    def cd_out(self):
        self.user_location = self.user_location.parent
        return

    def cd_home(self):
        self.user_location = self.root

    def ls_parse(self):
        self.command_index += 1
        line = self.lines[self.command_index].rstrip().split(' ')
        while line[0] != '$':
            if line[0] == 'dir':
                name = line[1]
                self.ls_add_dir(name)
            else:
                size = int(line[0])
                name = line[1]
                self.ls_add_file(size, name)
            self.command_index += 1
            line = self.lines[self.command_index].rstrip().split(' ')

    def ls_add_file(self, size, name):
        new_file = File(name=name, size=size)
        new_file.parent = self.user_location
        self.user_location.children[name] = new_file

    def ls_add_dir(self, name):
        new_dir = File(name=name, size=0)
        new_dir.parent = self.user_location
        self.user_location.children[name] = new_dir

    def operate_on_all_sub_dirs(self, dir, operation):
        """Return a result for running operation on every dir under this one"""
        dirs = []
        for name, file in dir.children.items():
            if file.size == 0:
                dirs.append((file.name, operation(file)))
                sub_dirs = self.operate_on_all_sub_dirs(file, operation)
                for sub_dir in sub_dirs:
                    dirs.append((sub_dir[0], sub_dir[1]))
        return dirs

    def directory_sum(self, dir):
        sum = 0
        for name, file in dir.children.items():
            if file.size == 0:
                sum += self.directory_sum(file)
            else:
                sum += file.size

        return sum


def part1(lines):
    file_system = FileSystem(lines)
    dirs = file_system.operate_on_all_sub_dirs(file_system.root, file_system.directory_sum)
    sum = 0
    for name, size in dirs:
        if size <= 100000:
            sum += size
    return sum


def part2(lines):
    file_system = FileSystem(lines)
    dirs = file_system.operate_on_all_sub_dirs(file_system.root, file_system.directory_sum)
    BIG_ENOUGH = 8381165
    LARGEST_DIRECTORY_SIZE = file_system.directory_sum(file_system.root)
    smallest = LARGEST_DIRECTORY_SIZE
    for _, size in dirs:
        if size >= 8381165 and size < smallest:
            smallest = size

    return smallest


def main():
    with open("day7.input") as f:
        lines = list(f)
        print(part1(lines))
        print(part2(lines))


if __name__ == "__main__":
    main()
