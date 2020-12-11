from itertools import product
from copy import deepcopy
from typing import Callable

def get_adjacent_occupants(grid, row, seat):
    cols = filter(lambda n: 0 <= n < len(grid[0]), [seat + x for x in [-1, 0, 1]])
    seats = filter(lambda n: 0 <= n < len(grid), [row + x for x in [-1, 0, 1]])
    neighbours = filter(lambda x: x != (row, seat), product(seats, cols))
    count = 0
    for square in neighbours:
        count += 1 if grid[square[0]][square[1]] == "#" else 0
    return count

def get_next_grid(grid):
    next_grid = []
    changed = False
    for row in range(len(grid)):
        new_row = ''
        for seat in range(len(grid[row])):
            if grid[row][seat] == 'L':
                if get_adjacent_occupants(grid, row, seat) == 0:
                    new_row += '#'
                    changed = True
                else:
                    new_row += 'L'
            elif grid[row][seat] == '#':
                if get_adjacent_occupants(grid, row, seat) < 4:
                    new_row += '#'
                else:
                    new_row += 'L'
                    changed = True
            else:
                new_row += '.'
        next_grid.append(new_row)
    return changed, next_grid

def main(filename):
    original_grid = open("seats").read().split('\n')

    next_stage = (True, deepcopy(original_grid))
    while next_stage[0]:
        next_stage = get_next_grid(next_stage[1])
    print(sum([row.count('#') for row in next_stage[1]]))


if __name__ == "__main__":
    main("seats")