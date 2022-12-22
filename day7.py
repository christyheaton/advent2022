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

    def get_total_size(self):
        self.total_dir_size = sum(self.files.values())
        return self.total_dir_size


if __name__ == '__main__':
    data = get_data(day=7, year=2022)
    count_size = 0
    test_data = data#[0:300]
    current_dir = None
    commands = test_data.split('$ ')
    for c in commands:
        print(f'for c Current dir {current_dir}')
        if c.startswith('ls'):
            print(f'c. starts with Current dir {current_dir}')
            current_dir.parse_ls(c[3:])
            total_dir_size = current_dir.get_total_size()
            if total_dir_size < 100_000:
                print(f'Total size is less than 100,000, adding to total.')
                count_size += total_dir_size
        elif c.startswith('cd ..'):
            current_dir = current_dir.parent_dir
        elif c.startswith('cd'):
            print(f'Entering change directory with line {c}')
            target_name = c.split()[1]
            if target_name == '/':
                current_dir = Directory(parent=None)
            else:
                current_dir = current_dir.sub_dirs.get(c.split()[1])
    print(f'Total count is {count_size}')
