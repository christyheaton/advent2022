from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Point:
    x: int
    y: int


class Rope:
    def __init__(self, length):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.length = length
        self.body = [Point(0, 0) for x in range(length)]

    def is_touching(self, a, b):
        if abs(a.x - b.x) < 2 and abs(a.y - b.y) < 2:
            return True

    def move_segment(self, a, b):
        above = False
        right = False

        if self.is_touching(a, b):
            return
        elif a.x == b.x:
            # On the same horizontal plane -- move tail vertically
            if a.y < b.y:
                b.y -= 1
            else:
                b.y += 1
        elif a.y == b.y:
            # On the same vertical plane - move tail horizontally
            if a.x < b.x:
                b.x -= 1
            else:
                b.x += 1
        else:
            if a.x > b.x:
                right = True
            if a.y > b.y:
                above = True

            if above and right:
                b.x += 1
                b.y += 1
            elif above and not right:
                b.x -= 1
                b.y += 1
            elif not above and right:
                b.x += 1
                b.y -= 1
            else:
                b.x -= 1
                b.y -= 1

    def move_head(self, direction):
        match direction:
            case 'U':
                self.body[0].y += 1
            case 'D':
                self.body[0].y -= 1
            case 'R':
                self.body[0].x += 1
            case 'L':
                self.body[0].x -= 1

    def move_body(self):
        for segment_i in range(1, len(self.body)):
            self.move_segment(self.body[segment_i - 1], self.body[segment_i])


if __name__ == '__main__':
    moves = get_data(day=9, year=2022).splitlines()

    # use 2 for part 1 and 10 for part 2
    r = Rope(2)
    visited = set()
    visited.add((0, 0))

    for m in moves:
        direction, amount = m.split()
        for i in range(int(amount)):
            r.move_head(direction)
            r.move_body()
            visited.add((r.body[-1].x, r.body[-1].y))

    print(f'Number of positions occupied by tail: {len(visited)}')



