"""
>>> r = Register()
>>> r.clear()
>>> r.put("y", -10)
>>> x = r.get("x")
>>> y = r.get("y")
>>> x, y
(0, -10)
>>> r.clear()
>>> line = "b inc 5 if a > 1"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
False
>>> r.clear()
>>> line = "b inc 5 if a < 1"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
True
>>> r.clear()
>>> line = "b inc 5 if a >= 0"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
True
>>> r.clear()
>>> line = "b inc 5 if a <= -1"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
False
>>> r.clear()
>>> line = "b inc 5 if a == 0"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
True
>>> r.clear()
>>> line = "b inc 5 if a != 1"
>>> x = Statement(line)
>>> x.condition.evaluate(r)
True
>>> r.clear()
>>> s1 = Statement("b inc 5 if a > 1")
>>> s1.process(r)
>>> s2 = Statement("a inc 1 if b < 5")
>>> s2.process(r)
>>> s3 = Statement("c dec -10 if a >= 1")
>>> s3.process(r)
>>> s4 = Statement("c inc -20 if c == 10")
>>> s4.process(r)
>>> r.values
{'a': 1, 'c': -10}
>>> r.max_value()
1
>>> r.max_seen
10
"""


class Instruction:
    def __init__(self, string):
        parts = string.split(" ")
        self.variable = parts[0]
        self.operator = parts[1]
        self.value = int(parts[2])
        return

    def to_string(self):
        return "Instruction:[variable=" + self.variable + ", operator=" + self.operator + ", value=" + self.value + "]"

    def apply(self, register):
        var = register.get(self.variable)
        if (self.operator == "inc"):
            var = var + self.value
        if (self.operator == "dec"):
            var = var - self.value
        register.put(self.variable, var)


class Condition:
    def __init__(self, string):
        parts = string.split(" ")
        self.variable = parts[0]
        self.operator = parts[1]
        self.value = int(parts[2])
        return

    def to_string(self):
        return "Condition:[variable=" + self.variable + ", operator=" + self.operator + ", value=" + self.value + "]"

    def evaluate(self, register):
        var = register.get(self.variable)
        if (self.operator == "<"):
            return var < self.value
        if (self.operator == "<="):
            return var <= self.value
        if (self.operator == ">"):
            return var > self.value
        if (self.operator == ">="):
            return var >= self.value
        if (self.operator == "=="):
            return var == self.value
        if (self.operator == "!="):
            return var != self.value


class Statement:
    def __init__(self, string):
        parts = string.split("if")
        self.instruction = Instruction(parts[0].strip())
        self.condition = Condition(parts[1].strip())
        return

    def to_string(self):
        return "Statement:[instruction=" + self.instruction.to_string() + ", condition=" + self.condition.to_string() + "]"

    def process(self, register):
        if self.condition.evaluate(register):
            self.instruction.apply(register)


class Register:
    values = {}
    max_seen = 0
    def get(self, key):
        if key in self.values:
            return self.values[key]
        return 0
    def put(self, key, value):
        self.values[key] = value
        if value > self.max_seen:
            self.max_seen = value
    def clear(self):
        self.values={}
    def max_value(self):
        return max(self.values.values())


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = [line for line in input_file]
    return lines


lines = read_input("input.txt")
r = Register();
for line in lines:
    s = Statement(line)
    s.process(r)
print("Part1 Result is ", r.max_value())
print("Part2 Result is ", r.max_seen)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
