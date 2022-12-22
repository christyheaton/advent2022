from aocd import get_data


class Directory:
    def __init__(self, parent):
        self.parent_dir = parent
        self.sub_dirs = {}
        self.files = {}
        self.total_size = 0

    def parse_ls(self, contents):
        print(f"Received this LS output:\n{contents}")
        lines = contents.splitlines()
        for line in lines:
            if line.startswith('dir'):
                dir_name = line.split()[1]
                self.sub_dirs[dir_name] = Directory(parent=self)
            elif line[0].isnumeric():
                size, name = line.split()
                self.files[name] = size
                self.total_size += size
                print(f'total size: {self.total_size}')
                print(f"Populating files dict with '{name}' size: {size}")
            else:
                raise ValueError(f'Unknown input type: {line}')


if __name__ == '__main__':
    data = get_data(day=7, year=2022)

    test_data = data[0:300]
    currentDir = None
    commands = test_data.split('$ ')
    for c in commands:
        print(f'for c Current dir {currentDir}')
        if c.startswith('ls'):
            print(f'c. starts with Current dir {currentDir}')
            currentDir.parse_ls(c[3:])
        elif c.startswith('cd ..'):
            currentDir = currentDir.parent_dir
        elif c.startswith('cd'):
            print(f'Entering change directory with line {c}')
            target_name = c.split()[1]
            if target_name == '/':
                currentDir = Directory(parent=None)
            else:
                currentDir = currentDir.sub_dirs.get(c.split()[1])
