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
        my_str = ''
        for word in my_input:
            my_str += word[i]
        new_letter = collections.Counter(my_str).most_common(1)[0][0]
        answer_string += new_letter
    print(answer_string)

if __name__ == '__main__':
    main()
