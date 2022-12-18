def get_intput_data(file):
    """Takes in a file, returns the data as a list"""
    with open(file) as f:
        lines = f.readlines()
        cal_str = '|'.join(lines)
    return cal_str


def get_total_per_elf(cal_str):
    """Takes in a string of calories, returns a list of total calories per elf"""
    mylist = []
    count = 0

    for i in cal_str.split('|'):
        if i.replace('\n', ''):
            count += int(i)
        else:
            mylist.append(count)
            count = 0
    mylist.append(count)
    return mylist


def get_max(cals_list):
    """Takes in a list of total calories per elf, returns the maximum value"""
    return max(cals_list)


if __name__ == '__main__':
    data = get_intput_data('data/day1_input.txt')
    total_p_elf = get_total_per_elf(data)
    max_cals = get_max(total_p_elf)
    print(max_cals)
