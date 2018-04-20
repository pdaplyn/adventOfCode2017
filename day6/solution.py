"""
>>> find_index_of_highest([0,3,0,1,-3])
1
>>> find_index_of_highest([0,3,0,13,-3])
3
>>> redistribute_value_at([0,2,7,0],2)
[2, 4, 1, 2]
>>> redistribute_value_at([2, 4, 1, 2], 1)
[3, 1, 2, 3]
>>> redistribute_value_at([3, 1, 2, 3], 0)
[0, 2, 3, 4]
>>> redistribute_value_at([0, 2, 3, 4], 3)
[1, 3, 4, 1]
>>> redistribute_value_at([1, 3, 4, 1], 2)
[2, 4, 1, 2]
>>> redistributions_before_loop([0,2,7,0])
situation  2, 4, 1, 2  first seen after  1  reallocations
loop length:  4
5
"""


def find_index_of_highest(numbers):
    highest = 0;
    highest_index = 0;
    for index, value in enumerate(numbers):
        if value > highest:
            highest = value
            highest_index = index
    return highest_index


def redistribute_value_at(numbers, index):
    value = numbers[index]
    numbers[index] = 0
    loop_index = index + 1
    while value > 0:
        # wrap around to start
        if loop_index >= len(numbers):
            loop_index = 0

        # allocate value
        value -= 1
        numbers[loop_index] += 1

        # move to next
        loop_index += 1
    return numbers


def redistributions_before_loop(numbers):
    allocations_seen = {}

    reallocations = 0;
    string_rep_of_numbers = ', '.join(str(x) for x in numbers)
    while string_rep_of_numbers not in allocations_seen.keys():
        # add to seen
        allocations_seen[string_rep_of_numbers] = reallocations

        # find highest index
        highest_index = find_index_of_highest(numbers)

        # redistribute
        numbers = redistribute_value_at(numbers, highest_index)
        reallocations += 1

        string_rep_of_numbers = ', '.join(str(x) for x in numbers)

    print("situation ", string_rep_of_numbers, " first seen after ", allocations_seen[string_rep_of_numbers], " reallocations")
    print("loop length: ", reallocations - allocations_seen[string_rep_of_numbers])

    return reallocations


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    line = input_file.readline()
    numbers = [int(x) for x in line.split("\t")]
    return numbers


in_list = read_input("input.txt")
result = redistributions_before_loop(in_list)
print("Part1 Result is ", result)

#in_list = read_input("input.txt")
#result = count_steps(in_list, complex_increment_counter)
#print("Part2 Result is ", result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
