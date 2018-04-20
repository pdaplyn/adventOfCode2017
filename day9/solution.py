"""
>>> score("{}")
(1, 0)
>>> score("{{{}}}")
(6, 0)
>>> score("{{!{}}")
(3, 0)
>>> score("{{},{}}")
(5, 0)
>>> score("{{{},{},{{}}}}")
(16, 0)
>>> score("{<a>,<a>,<a>,<a>}")
(1, 4)
>>> score("{{<ab>},{<ab>},{<ab>},{<ab>}}")
(9, 8)
>>> score("{{<!!>},{<!!>},{<!!>},{<!!>}}")
(9, 0)
>>> score("{{<a!>},{<a!>},{<a!>},{<ab>}}")
(3, 17)
"""

def score(line):
    total = 0
    garbage = 0
    current_score = 0
    ignore = False
    index = 0
    while index < len(line):
        char = line[index]

        if char == "{" and not ignore:
            current_score += 1

        elif char == "}" and not ignore:
            total += current_score
            current_score -= 1

        elif char == "!":
            index += 1

        elif char == "<" and not ignore:
            ignore = True
            garbage -= 1

        elif char == ">":
            ignore = False

        if ignore and char != "!":
            garbage += 1

        index += 1
    return total, garbage


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    line = input_file.readline()
    return line


input = read_input("input.txt")
total, garbage = score(input)
print("Part1 Result is ", total)
print("Part2 Result is ", garbage)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
