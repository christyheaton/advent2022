from aocd import get_data
from dataclasses import dataclass


@dataclass()
class Point:
    x: int
    y: int


class Rope:
    def __init__(self, length: int) -> None:
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.length = length
        self.body = [Point(0, 0) for _ in range(length)]

    def is_touching(self, a: Point, b: Point) -> bool:
        if abs(a.x - b.x) < 2 and abs(a.y - b.y) < 2:
            return True

    def move_segment(self, a: Point, b: Point) -> None:
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

    def move_head(self, direction: str) -> None:
        match direction:
            case 'U':
                self.body[0].y += 1
            case 'D':
                self.body[0].y -= 1
            case 'R':
                self.body[0].x += 1
            case 'L':
                self.body[0].x -= 1

    def move_body(self) -> None:
        for segment_i in range(1, len(self.body)):
            self.move_segment(self.body[segment_i - 1], self.body[segment_i])


def num_positions_occupied_by_tail(rope: Rope, instructions) -> int:
    visited = set()
    visited.add((0, 0))

    for m in instructions:
        direction, amount = m.split()
        for i in range(int(amount)):
            rope.move_head(direction)
            rope.move_body()
            visited.add((rope.body[-1].x, rope.body[-1].y))
    return len(visited)


def main() -> None:
    moves = get_data(day=9, year=2022).splitlines()

    print(f'Part 1: {num_positions_occupied_by_tail(Rope(2), moves)}')
    print(f'Part 2: {num_positions_occupied_by_tail(Rope(10), moves)}')


if __name__ == '__main__':
    main()
