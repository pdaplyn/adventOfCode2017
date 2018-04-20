"""
>>> grid = Grid(0,0)
>>> grid.move("ne")
>>> grid.move("ne")
>>> grid.move("ne")
>>> grid.longitude, grid.latitude, grid.distance()
(3, 1.5, 3)
>>> grid = Grid(0,0)
>>> grid.move("ne")
>>> grid.move("ne")
>>> grid.move("sw")
>>> grid.move("sw")
>>> grid.longitude, grid.latitude, grid.distance()
(0, 0.0, 0)
>>> grid = Grid(0,0)
>>> grid.move("ne")
>>> grid.move("ne")
>>> grid.move("s")
>>> grid.move("s")
>>> grid.longitude, grid.latitude, grid.distance()
(2, -1.0, 2)
>>> grid = Grid(0,0)
>>> grid.move("se")
>>> grid.move("sw")
>>> grid.move("se")
>>> grid.move("sw")
>>> grid.move("sw")
>>> grid.longitude, grid.latitude, grid.distance()
(-1, -2.5, 3)
"""


class Grid:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        self.max_distance = 0
        self.record_max = 1

    def move(self, direction):
        prev_long = self.longitude
        prev_lat = self.latitude
        if direction == "n":
            self.latitude += 1
        elif direction == "s":
            self.latitude -= 1
        elif direction == "ne":
            self.latitude += 0.5
            self.longitude += 1
        elif direction == "se":
            self.latitude -= 0.5
            self.longitude += 1
        elif direction == "sw":
            self.latitude -= 0.5
            self.longitude -= 1
        elif direction == "nw":
            self.latitude += 0.5
            self.longitude -= 1
        self.check_max(prev_long, prev_lat, self.longitude, self.latitude)

    def print(self):
        print("Location: ", self.longitude, self.latitude)

    def distance(self):
        moves = 0
        while self.longitude != 0 or self.latitude != 0:
            # move diagonally first
            if self.longitude > 0:
                if self.latitude > 0:
                    self.move("sw")
                elif self.latitude < 0:
                    self.move("nw")
                else:
                    # just west - either north or south is fine
                    self.move("nw")
            elif self.longitude < 0:
                if self.latitude > 0:
                    self.move("se")
                elif self.latitude < 0:
                    self.move("ne")
                else:
                    # just east - either north or south is fine
                    self.move("ne")
            else:
                if self.latitude > 0:
                    self.move("s")
                elif self.latitude < 0:
                    self.move("n")
            moves += 1
            #self.print()

        return moves

    def check_max(self, prev_longitude, prev_latitude, new_longitude, new_latitude):
        if self.record_max == 0:
            return

        # if moved further away from center, check max distance
        if abs(new_longitude) > abs(prev_longitude) or abs(new_latitude) > abs(prev_latitude):
            # clone grid to check how many moves away
            clone = Grid(self.longitude, self.latitude)
            clone.record_max = 0
            distance = clone.distance()
            if distance > self.max_distance:
                self.max_distance = distance

    def get_max(self):
        return self.max_distance


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    line = input_file.readline()
    return line.strip()


input_line = read_input("input.txt")
csv = (x for x in input_line.split(","))
puzzle = Grid(0,0)
for x in csv:
    puzzle.move(x)
puzzle.print()

result1 = puzzle.distance()
print("Part1 Result is ", result1)
print("Part2 Result is ", puzzle.get_max())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
