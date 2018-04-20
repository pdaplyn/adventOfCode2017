"""
>>> a = [5, 1, 9, 5]
>>> b = [7, 5, 3]
>>> c = [2, 4, 6, 8]
>>> max_diff(a)
8
>>> max_diff(b)
4
>>> max_diff(c)
6
>>> input_matrix = [a, b, c]
>>> calc_result(input_matrix)
18
"""


def max_diff(input_list):
    input_list.sort()
    smallest = input_list[0]
    largest = input_list[len(input_list)-1]
    return largest - smallest


def calc_result(input_matrix):
    answer = 0
    for row in input_matrix:
        diff = max_diff(row)
        answer = answer + diff
    return answer


def read_input(filename):
    print("Opening file ", filename)
    matrix = []
    input_file = open(filename, "r")
    for line in input_file:
        row = [int(x) for x in line.split()]
        print(row)
        matrix.append(row)
    return matrix


in_matrix = read_input("C:\\Users\\PeterDaplyn\\IdeaProjects\\adcventOfCode2017\\day2\\input.txt")
result = calc_result(in_matrix)
print("Result is ", result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
