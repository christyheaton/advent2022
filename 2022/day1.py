from aocd import get_data


def get_total_per_elf(elf_calories: list) -> list:
    """Takes in a list of calories, returns a list of total calories per elf"""
    sum_cals_elf = []
    count = 0
    cal_str = '|'.join(elf_calories)
    for i in cal_str.split('|'):
        if i:
            count += int(i)
        else:
            sum_cals_elf.append(count)
            count = 0
    sum_cals_elf.append(count)
    return sum_cals_elf


def get_total_top_elves(total_calorie_list: list, num_elves_to_sum: int) -> int:
    """Takes in a list of total calories per elf and a number of elves
    returns the sum of the calorie counts for the inputted number elves
    with the highest calorie counts"""
    total_calorie_list.sort()
    top_elves = total_calorie_list[-num_elves_to_sum:]
    sum_top_elves = 0
    for elf_cals in top_elves:
        sum_top_elves += elf_cals
    return sum_top_elves


if __name__ == '__main__':
    print('Getting input data...')
    data = get_data(day=1, year=2022).splitlines()
    print('Calculating total calories per elf...')
    total_p_elf = get_total_per_elf(data)

    print('Getting the calorie count for the elf with the most calories...')
    max_cals = max(total_p_elf)
    print(f'The elf with the most calories has ***{max_cals}*** calories!')

    elf_count = 3
    print(f'Getting the calorie count for the top {elf_count} elves with the most calories...')
    total_top_elves = get_total_top_elves(total_p_elf, elf_count)
    print(f'The {elf_count} elves with the most calories together have a total of ***{total_top_elves}*** calories!')
