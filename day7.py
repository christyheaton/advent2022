from aocd import get_data


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        if self.parent:
            print(f'Constructor for new dir named: {name}, parent: {parent.name}')
        else:
            print(f'Constructor for new dir named: {name}, parent: None')
        self.sub_dirs = {}
        self.files = {}
        self.total_dir_size = 0

    def get_size_recursive(self):
        self.total_dir_size = sum(self.files.values())
        for key in self.sub_dirs.keys():
            self.total_dir_size += self.sub_dirs.get(key).get_size_recursive()
        return self.total_dir_size


class FileSystem:
    def __init__(self, input_commands):
        self.input = input_commands
        self.directories = []
        self.cwd = Directory(parent=None, name='/')
        self.directories.append(self.cwd)
        self.parse_input()

    def parse_input(self):
        # This will parse through data in Day7 format and construct a file system
        # tree based on all the cd and ls commands
        commands = self.input.split('$ ')
        size = 0
        for c in commands:
            print(f'cwd: {self.cwd.name}, command: {c}')
            if c.startswith('ls'):
                self.parse_ls(c[3:])
            elif c.startswith('cd ..'):
                self.cwd = self.cwd.parent
            elif c.startswith('cd'):
                print(f'Entering change directory with line {c}')
                target_name = c.split()[1]
                if '/' in target_name:
                    print('skipping / dir')
                    continue
                else:
                    self.cwd = self.cwd.sub_dirs.get(c.split()[1])
                    print(f'new cwd: {self.cwd.name}')

    def parse_ls(self, contents):
        print(f'parsing "ls" for cwd: {self.cwd.name}')
        lines = contents.splitlines()
        for line in lines:
            if line.startswith('dir'):
                dir_name = line.split()[1]
                print(f'Parsing line: "{line}": found new dir to create: {dir_name}')
                new_dir = Directory(parent=self.cwd, name=dir_name)
                self.directories.append(new_dir)
                self.cwd.sub_dirs[dir_name] = new_dir
            elif line[0].isnumeric():
                print(f'Parsing line: {line}')
                size, name = line.split()
                print(f'Found file with name {name}, size {size}...')
                self.cwd.files[name] = int(size)
                print(f'Populating files dict with "{name}" size: {size}')
            else:
                raise ValueError(f'Unknown input type: {line}')


if __name__ == '__main__':
    data = get_data(day=7, year=2022)
    f = FileSystem(data)
    print()
    
    # Part 1 Solution:
    final_list_pt1 = []
    for dir in f.directories:
        total_size = dir.get_size_recursive()
        if total_size <= 100_000:
            final_list_pt1.append(total_size)
        final_list_pt1.append(total_size)

    print('Part 1:')
    print(f'Sum of all directories under 100,000 units is: {sum(final_list_pt1)}.')

    # Part 2 Solution:
    need_to_delete = f.directories[0].get_size_recursive() - 70_000_000 + 30_000_000
    big_dirs = []
    for d in f.directories:
        if d.get_size_recursive() > need_to_delete:
            big_dirs.append(d.get_size_recursive())

    print('Part 2:')
    print(f'Need to delete the directory of size {min(big_dirs)} units.')
