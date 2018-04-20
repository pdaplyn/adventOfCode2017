"""
>>> list1 = List(5)
>>> list1.process(3)
>>> list1.position, list1.skip
(3, 1)
>>> list1.process(3)
>>> list1.position, list1.skip
(2, 2)
>>> list2 = List(5)
>>> list2.get_length(1,2)
[1, 2]
>>> list2.get_length(3,4)
[3, 4, 0, 1]
>>> list3 = List(5)
>>> list3.numbers
[0, 1, 2, 3, 4]
>>> list3.apply_list(1, (6, 7, 8))
>>> list3.numbers
[0, 6, 7, 8, 4]
>>> example = List(5)
>>> example.process(3)
>>> example.numbers
[2, 1, 0, 3, 4]
>>> example.process(4)
>>> example.numbers
[4, 3, 0, 1, 2]
>>> example.process(1)
>>> example.numbers
[4, 3, 0, 1, 2]
>>> example.process(5)
>>> example.numbers
[3, 4, 2, 1, 0]
>>> ascii_values("1,2,3")
[49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
>>> list4 = List(32)
>>> list4.blocks_of_sixteen()
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
>>> expected = 65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22
>>> expected
64
>>> xor((65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22))
64
>>> hex_block((64, 7, 255))
'4007ff'
"""


def xor(block):
    result = 0
    for i in block:
        result = result ^ i
    return result


def hex_block(block):
    result = ""
    for i in block:
        result += ("0" + hex(i).replace("0x",""))[-2:]
    return result


class List:
    def __init__(self, size):
        self.size = size
        self.numbers = list(range(size))
        self.position = 0
        self.skip = 0

    def get_length(self,position,length):
        extra_from_start = position + length - self.size
        if extra_from_start < 0:
            # no loop round
            return self.numbers[position:position+length]
        else :
            return self.numbers[position:] + self.numbers[:extra_from_start]

    # overwrite self.number with sub_list, starting at position and looping if needed
    def apply_list(self, start, sub_list):
        for x in sub_list:
            self.numbers[start] = x
            start = (start + 1) % self.size
        return

    def process(self, length):
        sub_list = self.get_length(self.position, length)
        sub_list.reverse()
        self.apply_list(self.position, sub_list)
        self.position = (self.position + length + self.skip) % self.size
        self.skip += 1

    def hash(self, input_list):
        for i in range(64):
            for x in input_list:
                self.process(x)

    def blocks_of_sixteen(self):
        blocks = []
        block = []
        for n in self.numbers:
            block.append(n)
            if len(block) == 16:
                blocks.append(block)
                block = []
        return blocks

    def dense_hash(self):
        blocks = self.blocks_of_sixteen()
        hash_numbers = []
        for block in blocks:
            hash_numbers.append(xor(block))
        return hex_block(hash_numbers)


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    line = input_file.readline()
    return line.strip()


def ascii_values(line):
    ascii_list = []
    for x in line:
        ascii_list.append( ord(x) )
    # add hard-coded sequence
    ascii_list.append(17)
    ascii_list.append(31)
    ascii_list.append(73)
    ascii_list.append(47)
    ascii_list.append(23)
    return ascii_list


input_line = read_input("input.txt")
csv = (int(x) for x in input_line.split(","))
puzzle = List(256)
for x in csv:
    puzzle.process(x)

result1 = puzzle.numbers[0] * puzzle.numbers[1]
print("Part1 Result is ", result1)

ascii_list = ascii_values(input_line)
puzzle2 = List(256)
puzzle2.hash(ascii_list)
result2 = puzzle2.dense_hash()
print("Part2 Result is ", result2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
