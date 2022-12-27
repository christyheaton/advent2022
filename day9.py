# from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Point:
    x: int
    y: int


class Rope:
    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)

    def is_touching(self):
        if abs(self.head.x - self.tail.x) < 2 and abs(self.head.y - self.tail.y) < 2:
            return True

    def move_tail(self):
        above = False
        right = False

        if self.is_touching():
            return
        elif self.head.x == self.tail.x:
            # On the same horizontal plane -- move tail vertically
            if self.head.y < self.tail.y:
                self.tail.y -= 1
            else:
                self.tail.y += 1
        elif self.head.y == self.tail.y:
            # On the same vertical plane - move tail horizontally
            if self.head.x < self.tail.x:
                self.tail.x -= 1
            else:
                self.tail.x += 1
        else:
            if self.head.x > self.tail.x:
                right = True
            if self.head.y > self.tail.y:
                above = True

            if above and right:
                self.tail.x += 1
                self.tail.y += 1
            elif above and not right:
                self.tail.x -= 1
                self.tail.y += 1
            elif not above and right:
                self.tail.x += 1
                self.tail.y -= 1
            else:
                self.tail.x -= 1
                self.tail.y -= 1

    def move_head(self, direction):
        match direction:
            case 'U':
                self.head.y += 1
            case 'D':
                self.head.y -= 1
            case 'R':
                self.head.x += 1
            case 'L':
                self.head.x -= 1


def main():
    # moves = get_data(day=9, year=2022).splitlines()
    with open('data/day9_input.txt') as f:
        moves = f.readlines()

    r = Rope()
    visited = set()
    visited.add((0, 0))

    for m in moves:
        direction, amount = m.split()
        for i in range(int(amount)):
            r.move_head(direction)
            r.move_tail()
            visited.add((r.tail.x, r.tail.y))

    print(f'Number of positions occupied by tail: {len(visited)}')
    return visited


if __name__ == '__main__':
    main()
