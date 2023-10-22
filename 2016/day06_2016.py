import collections

def main():
    my_input = ['eedadn',
                'drvtee',
                'eandsr',
                'raavrd',
                'atevrs',
                'tsrnev',
                'sdttsa',
                'rasrtv',
                'nssdts',
                'ntnada',
                'svetve',
                'tesnvt',
                'vntsnd',
                'vrdear',
                'dvrsen',
                'enarar']

    answer_string = ''
    for i in range(len(my_input[0])):
        chars_at_index = ''
        for string in my_input:
            chars_at_index += string[i]
        most_common_letter = collections.Counter(chars_at_index).most_common(1)[0][0]
        answer_string += most_common_letter
    print(answer_string)

if __name__ == '__main__':
    main()
