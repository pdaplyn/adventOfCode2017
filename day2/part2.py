"""
>>> a = [5, 9, 2, 8]
>>> b = [9, 4, 7, 3]
>>> c = [3, 8, 6, 5]
>>> divisor_result(a)
4
>>> divisor_result(b)
3
>>> divisor_result(c)
2
>>> input_matrix = [a, b, c]
>>> calc_result(input_matrix)
9
"""


def divisor_result(input_list):
    input_list.sort()
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[j] % input_list[i] == 0:
                return input_list[j] // input_list[i]
    return 0


def calc_result(input_matrix):
    answer = 0
    for row in input_matrix:
        result = divisor_result(row)
        answer = answer + result
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
