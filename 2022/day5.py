from aocd import get_data


def format_container_data(stacks_data: list) -> dict:
    """Takes in a list of lines from the input data
    outputs a dictionary where the key is the column,
    and value is a list of strings with the column info in order bottom to top"""
    stacks_dict = {key: [] for key in range(1, 10)}
    container_info = stacks_data[::-1]
    container_info_split = []
    for cont in container_info:
        cont = cont.replace('    ', ' ').split(' ')
        container_info_split.append(cont)
    count = 0
    while count < len(container_info_split):
        for k in stacks_dict.keys():
            for d in container_info_split:
                if not d[count]:
                    continue
                stacks_dict[k].append(d[count])
            count += 1
    return stacks_dict


def perform_instructions(instructions: str, stacks: dict) -> dict:
    """Given a set of instructions and a dictionary of stacks,
    perform the instructions and output the modified dictionary of stacks"""
    for i in instructions:
        sp = i.split(' ')
        count = int(sp[1])
        from_stack = int(sp[3])
        to_stack = int(sp[5])
        #part 1
        # for c in range(count):
        #     stacks[to_stack].append(stacks[from_stack].pop())
        #part2
        for item in stacks[from_stack][-count:]:
            stacks[to_stack].append(item)
        del stacks[from_stack][len(stacks[from_stack]) - count:]
    return stacks


if __name__ == '__main__':
    data = get_data(day=5, year=2022).splitlines()
    stack_data = data[0:9]
    instructions_data = data[10:]

    stacks_prelim = format_container_data(stack_data)
    print(f'Stacks before shuffling: {stacks_prelim}')
    stacks_shuffled = perform_instructions(instructions_data, stacks_prelim)
    print(f'Stacks after shuffling: {stacks_shuffled}')

    message = ''
    for order in stacks_shuffled.values():
        message += order[-1][1]
    print(f'Message: {message}')
