"""
>>> array_size(1)
1
>>> array_size(8)
3
>>> array_size(23)
5
>>> find_middle(1)
(0, 0)
>>> find_middle(3)
(1, 1)
>>> find_middle(5)
(2, 2)
>>> find_location(1,1)
(0, 0)
>>> find_location(3,8)
(1, 2)
>>> find_location(5,21)
(0, 4)
>>> calc_result(1)
0
>>> calc_result(12)
3
>>> calc_result(23)
2
>>> calc_result(1024)
31

>>> next_cell(5, (2,2))
(3, 2)
>>> next_cell(5, (3,2))
(3, 1)
>>> next_cell(5, (3,1))
(2, 1)
>>> next_cell(5, (2,1))
(1, 1)
>>> next_cell(5, (1,1))
(1, 2)
>>> next_cell(5, (1,2))
(1, 3)
>>> next_cell(5, (1,3))
(2, 3)
>>> next_cell(5, (2,3))
(3, 3)
>>> next_cell(5, (3,3))
(4, 3)
>>> next_cell(5, (4,3))
(4, 2)
>>> next_cell(5, (4,2))
(4, 1)
>>> next_cell(5, (4,1))
(4, 0)
>>> next_cell(5, (4,0))
(3, 0)
>>> next_cell(5, (3,0))
(2, 0)
>>> next_cell(5, (2,0))
(1, 0)
>>> next_cell(5, (1,0))
(0, 0)
>>> next_cell(5, (0,0))
(0, 1)
>>> next_cell(5, (0,1))
(0, 2)
>>> next_cell(5, (0,2))
(0, 3)
>>> next_cell(5, (0,3))
(0, 4)
>>> next_cell(5, (0,4))
(1, 4)
>>> next_cell(5, (1,4))
(2, 4)
>>> next_cell(5, (2,4))
(3, 4)
>>> next_cell(5, (3,4))
(4, 4)

>>> get_cells_to_sum( (0,0) , 3)
{(0, 1), (1, 0), (1, 1)}
>>> get_cells_to_sum( (2,2) , 3)
{(1, 2), (1, 1), (2, 1)}

>>> matrix = [[2 for x in range(4)] for y in range(4)]
>>> sum_around(matrix, (1, 1))
16
"""
import math


def array_size(input):
    # size of square to accomodate all numbers
    answer = math.ceil(math.sqrt(input))
    # needs to be an odd number
    if answer % 2 == 0:
        answer += 1
    return answer

def find_middle(size):
    half_up = int(size / 2)
    return half_up, half_up


def find_location(size, target):
    # answer is always on the outside ring
    x = 0
    y = 0
    dimension = size - 1
    #print("Dimension", dimension)
    filled_square_max = (size - 2) ** 2
    #print("Filled Square Max", filled_square_max)
    additional = target - filled_square_max
    #print("Additional", additional)

    if additional <= dimension:
        # in right edge
        x = dimension
        y = dimension - additional
    elif additional <= dimension * 2:
        # in top row
        y = 0
        x = dimension - (additional - dimension)
    elif additional <= (size-1)*3:
        # in left edge
        x = 0
        y = additional - (dimension * 2)
    else:
        # in bottom row
        y = size-1
        x = additional - (dimension * 3)

    return x, y


def calc_result(input):
    size = array_size(input)
    #print("Size:", size)
    middle = find_middle(size)
    #print("Middle:", middle)
    target = find_location(size, input)
    #print("Target:", target)
    diff = {x - y for x in (middle) for y in target}
    #print("Diff:", diff)
    abs_diff = {abs(x) for x in diff}
    #print("Abs:", abs_diff)
    return sum(abs_diff)


def next_cell(size, current):
    x = current[0]
    y = current[1]
    middle = find_middle(size)

    # if bottom right, go right
    if current[0] == current[1] and current[0] >= middle[0] and current[1] >= middle[1]:
        x += 1
    # if top right, go left
    elif current[0] - middle[0] == middle[1] - current[1] and current[0] >= middle[0] and current[1] < middle[1]:
        x -= 1
    # if top left, go down
    elif current[0] == current[1] and current[0] < middle[0] and current[1] < middle[1]:
        y += 1
    # if bottom left, go right
    elif middle[0] - current[0] == current[1] - middle[1] and current[0] < middle[0] and current[1] > middle[1]:
        x += 1

    # if on right edge go up
    elif middle[0] < current[0] and abs(middle[0] - current[0]) > abs(middle[1] - current[1]):
        y -= 1
    # if on top edge go left
    elif middle[1] > current[1] and abs(middle[0] - current[0]) < abs(middle[1] - current[1]):
        x -= 1
    # if on left edge go down
    elif middle[0] > current[0] and abs(middle[0] - current[0]) > abs(middle[1] - current[1]):
        y += 1
    # if on bottom edge go right
    elif middle[1] < current[1] and abs(middle[0] - current[0]) < abs(middle[1] - current[1]):
        x += 1

    return (x,y)


def get_cells_to_sum(current, size):
    cells = {(x,y)
             for x in range(current[0]-1,current[0]+2)
             for y in range(current[1]-1,current[1]+2)
             if size > x >= 0 and size > y >= 0 and not (x == current[0] and y == current[1])
             }
    return cells


def sum_around(matrix, current):
    cells = get_cells_to_sum(current, len(matrix))
    answer = 0
    for cell in cells:
        answer += matrix[cell[0]][cell[1]]
    return answer


def populate_to_limit(size, limit):
    matrix = [[0 for x in range(size)] for y in range(size)]
    current = find_middle(size)
    # init first
    matrix[current[0]][current[1]] = 1
    while matrix[current[0]][current[1]] < limit:
        current = next_cell(size, current)
        value = sum_around(matrix, current)
        matrix[current[0]][current[1]] = value
    return matrix[current[0]][current[1]]


def calc_part2(input):
    size = array_size(input)
    print("Size:", size)
    value = populate_to_limit(size, input)
    return value


input = 368078
result = calc_result(input)
print("Result is ", result)

result = calc_part2(input)
print("Part2 result is", result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
