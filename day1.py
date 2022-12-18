def get_intput_data(file):
    """Takes in a file, returns the data as a list"""
    with open(file) as f:
        lines = f.readlines()
        cal_str = '|'.join(lines)
    return cal_str


def get_total_per_elf(cal_str):
    """Takes in a string of calories, returns a list of total calories per elf"""
    sum_cals_elf = []
    count = 0

    for i in cal_str.split('|'):
        if i.replace('\n', ''):
            count += int(i)
        else:
            sum_cals_elf.append(count)
            count = 0
    sum_cals_elf.append(count)
    return sum_cals_elf


def get_max(cals_list):
    """Takes in a list of total calories per elf, returns the maximum value"""
    return max(cals_list)


def get_total_top_3(cals_list):
    """Takes in a list of total calories per elf, returns the sum of the top 3"""
    cals_list.sort()
    top_3 = cals_list[-3:]
    sum_top_3 = 0
    for n in top_3:
        sum_top_3 += n
    return sum_top_3


if __name__ == '__main__':
    data = get_intput_data('data/day1_input.txt')
    total_p_elf = get_total_per_elf(data)
    max_cals = get_max(total_p_elf)
    total_top_3 = get_total_top_3(total_p_elf)
    print(f'The elf with the most calories has {max_cals} calories.')
    print(f'The 3 elves with the most calories together have {total_top_3} calories.')
