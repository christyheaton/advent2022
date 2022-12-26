import pandas as pd


with open('data/day8_input.txt') as f:
    lines = f.readlines()


# lines = ['30373\n',
#         '25512\n',
#         '65332\n',
#         '33549\n',
#         '35390\n']

def data_list_to_df(data):
    data_list = []
    x = 0
    y = 0
    while x < len(lines):
        for line in lines[x]:
            for num in line:
                if line == '\n':
                    continue
                data_list.append({'val': int(line), 'xcoord': x, 'ycoord': y})
                y += 1
        x += 1
        y = 0
    return pd.DataFrame(data_list)


def calc_visible(df, col):
    considering_row = 0
    highest_value = -1
    for i, tree in df.iterrows():
        if tree[col] != considering_row:
            # We've moved to a new row - reset highest_value to -1
            considering_row = tree[col]
            highest_value = -1

        if tree['val'] > highest_value:
            df.loc[i, 'visible'] = True
            highest_value = tree['val']
    return df


if __name__ == '__main__':
    data_df = data_list_to_df(lines)
    data_df['visible'] = False
    data_df = calc_visible(data_df, 'xcoord')
    data_df = data_df.sort_values(by=['xcoord',
                                      'ycoord'], ascending=[False,
                                                            False]).reset_index()

    data_df.drop('index', axis=1, inplace=True)
    data_df = calc_visible(data_df, 'xcoord')
    data_df = data_df.sort_values(by=['ycoord',
                                      'xcoord']).reset_index()

    data_df.drop('index', axis=1, inplace=True)
    data_df = calc_visible(data_df, 'ycoord')
    data_df = data_df.sort_values(by=['ycoord',
                                      'xcoord'], ascending=[False,
                                                            False]).reset_index()

    data_df.drop('index', axis=1, inplace=True)
    data_df = calc_visible(data_df, 'ycoord')
    print(data_df.visible.value_counts())
