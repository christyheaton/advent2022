from aocd import get_data
from dataclasses import dataclass

test_data = """30373
25512
65332
33549
35390"""


@dataclass()
class Tree:
    row: int
    col: int
    height: str
    visible: bool = False
    view_score: int = 0


class Forest:
    def __init__(self, forest: str) -> None:
        self.input_data = forest
        self.grid = {}
        self.visible_trees = []
        self.total_rows = len(forest.splitlines())
        self.total_cols = len(list(forest.splitlines()[0]))

        self.populate_grid()

    def populate_grid(self) -> None:
        row = 0
        col = 0
        for line in self.input_data.splitlines():
            for height in list(line):
                self.grid[(row, col)] = Tree(row, col, height)
                col += 1
            row += 1
            col = 0

    def check_visibility(self, coord_list1: range, coord_list2: range, orientation: str) -> None:
        # Set an initial null tree so that every edge tree is visible in comparison
        for coord1 in coord_list1:
            highest_so_far = -1  # Set an initial null tree when starting a new row or column
            for coord2 in coord_list2:
                if orientation == 'horizontal':
                    current_tree = self.grid.get((coord1, coord2))
                else:
                    current_tree = self.grid.get((coord2, coord1))
                if int(highest_so_far) < int(current_tree.height):
                    current_tree.visible = True
                    highest_so_far = current_tree.height

    def count_vis_total(self) -> int:
        visible = 0
        for key in self.grid.keys():
            tree = self.grid.get(key)
            if tree.visible:
                visible += 1
        return visible

    def count_visible_trees(self) -> int:
        rows_top_to_bottom = range(0, self.total_rows)
        columns_left_to_right = range(0, self.total_cols)
        rows_bottom_to_top = rows_top_to_bottom[::-1]
        columns_right_to_left = columns_left_to_right[::-1]

        # Left to right
        self.check_visibility(rows_top_to_bottom, columns_left_to_right, 'horizontal')
        # Right to left
        self.check_visibility(rows_top_to_bottom, columns_right_to_left, 'horizontal')
        # Top to bottom
        self.check_visibility(rows_top_to_bottom, columns_left_to_right, 'vertical')
        # Bottom to top
        self.check_visibility(columns_left_to_right, rows_bottom_to_top, 'vertical')
        return f.count_vis_total()

    def get_directional_view_score(self, direction: str, tree: Tree) -> int:
        row = tree.row
        col = tree.col
        directional_view_score = 0

        while True:
            match direction:
                case 'up':
                    row -= 1
                case 'down':
                    row += 1
                case 'left':
                    col -= 1
                case 'right':
                    col += 1
                case other:
                    raise ValueError(f'Bad input for check_view_direction function: {direction}')

            if row < 0 or row > self.total_rows - 1 or col < 0 or col > self.total_cols - 1:
                break
            else:
                comparison_height = self.grid.get((row, col)).height
                directional_view_score += 1
                if comparison_height >= tree.height:
                    break

        return directional_view_score

    def calculate_total_view_score(self, tree: Tree) -> int:
        total = 1
        all_view_scores = [self.get_directional_view_score(x, tree) for x in ['up',
                                                                              'down',
                                                                              'left',
                                                                              'right']]
        for score in all_view_scores:
            if score:
                total = total * score
        return total

    def get_view_scores_for_every_tree(self) -> int:
        return max([f.calculate_total_view_score(x) for x in self.grid.values()])


if __name__ == '__main__':
    input_data = get_data(day=8, year=2022)
    f = Forest(input_data)

    print(f'Part 1. Total visible trees: {f.count_visible_trees()}')
    print(f'Part 2. Highest view score: {f.get_view_scores_for_every_tree()}')
