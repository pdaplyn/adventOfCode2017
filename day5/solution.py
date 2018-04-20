"""
>>> count_steps([0,3,0,1,-3], simple_increment_counter)
5
>>> count_steps([0,3,0,1,-3], complex_increment_counter)
10
"""


def count_steps(instructions, increment_calculator):
    instruction_count = 0
    current_i = 0

    while  0 <= current_i  < len(instructions):
        instruction_count += 1
        jump = instructions[current_i]
        next_i = current_i + jump
        instructions[current_i] += increment_calculator(jump)
        current_i = next_i

    return instruction_count


def simple_increment_counter(jump):
    return 1


def complex_increment_counter(jump):
    if jump >= 3:
        return -1
    else:
        return 1


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = [];
    for line in input_file:
        lines.append( int( line.strip() ) )
    return lines


in_list = read_input("input.txt")
result = count_steps(in_list, simple_increment_counter)
print("Part1 Result is ", result)

in_list = read_input("input.txt")
result = count_steps(in_list, complex_increment_counter)
print("Part2 Result is ", result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
