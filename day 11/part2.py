from itertools import product
from copy import deepcopy
from typing import Callable

def get_visible_occupants(grid, row, seat):
    directions = filter(lambda y: not y[0] == y[1] == 0,
                        product([-1, 0, 1], [-1, 0, 1]))
    count = 0
    for direction in directions:
        multiplier = 1
        found = False
        while not found:
            y, x = row + (multiplier * direction[0]), seat + (multiplier * direction[1])
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if grid[y][x] == '.':
                    multiplier += 1
                else:
                    found = True
                    count += 1 if grid[y][x] == '#' else 0
            else:
                found = True
    return count

def get_next_grid(grid):
    next_grid = []
    changed = False
    for row in range(len(grid)):
        new_row = ''
        for seat in range(len(grid[row])):
            if grid[row][seat] == 'L':
                if get_visible_occupants(grid, row, seat) == 0:
                    new_row += '#'
                    changed = True
                else:
                    new_row += 'L'
            elif grid[row][seat] == '#':
                if get_visible_occupants(grid, row, seat) < 5:
                    new_row += '#'
                else:
                    new_row += 'L'
                    changed = True
            else:
                new_row += '.'
        next_grid.append(new_row)
    return changed, next_grid

def main(filename):
    original_grid = open(filename).read().split('\n')

    next_stage = (True, deepcopy(original_grid))
    while next_stage[0]:
        next_stage = get_next_grid(next_stage[1])

    print(sum([row.count('#') for row in next_stage[1]]))


if __name__ == "__main__":
    main("seats")