"""
>>> valid_passphrase("aa bb cc dd ee")
True
>>> valid_passphrase("aa bb cc dd aa")
False
>>> valid_passphrase("aa bb cc dd aaa")
True
>>> valid_passphrase_strict("abcde fghij")
True
>>> valid_passphrase_strict("abcde xyz ecdab")
False
>>> valid_passphrase_strict("a ab abc abd abf abj")
True
>>> valid_passphrase_strict("iiii oiii ooii oooi oooo")
True
>>> valid_passphrase_strict("oiii ioii iioi iiio")
False
"""


def valid_passphrase(passphrase):
    words = passphrase.split(" ")
    words_seen = set()
    for word in words:
        if word in words_seen:
            return False
        else:
            words_seen.add(word)
    return True


def valid_passphrase_strict(passphrase):
    words = passphrase.split(" ")
    words_seen = set()
    for word in words:
        chars = list(word)
        chars.sort()
        word = ''.join(chars)
        if word in words_seen:
            return False
        else:
            words_seen.add(word)
    return True


def calc_result(input_list, validator):
    answer = 0
    for row in input_list:
        answer += validator(row.strip())
    return answer


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = [];
    for line in input_file:
        lines.append(line)
    return lines


in_list = read_input("C:\\Users\\PeterDaplyn\\IdeaProjects\\adcventOfCode2017\\day4\\input.txt")
result = calc_result(in_list, valid_passphrase)
print("Part1 Result is ", result)
result = calc_result(in_list, valid_passphrase_strict)
print("Part2 Result is ", result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
