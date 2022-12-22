from aocd import get_data


class Directory:
    def __init__(self, parent):
        self.parent_dir = parent
        self.sub_dirs = {}
        self.files = {}
        self.total_dir_size = 0

    def parse_ls(self, contents):
        print(f'Received this LS output:\n{contents}')
        lines = contents.splitlines()
        for line in lines:
            if line.startswith('dir'):
                dir_name = line.split()[1]
                self.sub_dirs[dir_name] = Directory(parent=self)
            elif line[0].isnumeric():
                size, name = line.split()
                self.files[name] = int(size)
                print(f'Populating files dict with "{name}" size: {size}')
            else:
                raise ValueError(f'Unknown input type: {line}')

    def get_size_recursive(self):
        self.total_dir_size = sum(self.files.values())
        for key in self.sub_dirs.keys():
            my_sub_dir = self.sub_dirs.get(key)
            self.total_dir_size += my_sub_dir.get_size_recursive()
        return self.total_dir_size


if __name__ == '__main__':
    data = get_data(day=7, year=2022)
    test_data = data#[0:300]
    current_dir = None
    commands = test_data.split('$ ')
    size = 0
    for c in commands:
        print(f'for c Current dir {current_dir}')
        if c.startswith('ls'):
            print(f'c. starts with Current dir {current_dir}')
            current_dir.parse_ls(c[3:])
            if current_dir.get_size_recursive() <= 100_000:
                size += current_dir.get_size_recursive()
        elif c.startswith('cd ..'):
            current_dir = current_dir.parent_dir
        elif c.startswith('cd'):
            print(f'Entering change directory with line {c}')
            target_name = c.split()[1]
            if target_name == '/':
                current_dir = Directory(parent=None)
            else:
                current_dir = current_dir.sub_dirs.get(c.split()[1])
    print(size)