"""
>>> layer = Layer(0, 2)
>>> layer.scanner_position
1
>>> layer.tick()
>>> layer.scanner_position
2
>>> layer.tick()
>>> layer.scanner_position
1
>>> layer.tick()
>>> layer.scanner_position
2
>>> firewall = Firewall()
>>> firewall.add_layer(Layer(0,3))
>>> firewall.add_layer(Layer(1,2))
>>> firewall.add_layer(Layer(4,4))
>>> firewall.add_layer(Layer(6,4))
>>> firewall.max_layer_id
6
>>> firewall.tick()
>>> firewall.tick()
>>> firewall.tick()
>>> firewall.layers[0].scanner_position, firewall.layers[1].scanner_position, firewall.layers[4].scanner_position, firewall.layers[6].scanner_position
(2, 2, 4, 4)
>>> firewall = Firewall()
>>> firewall.add_layer(Layer(0,3))
>>> firewall.add_layer(Layer(1,2))
>>> firewall.add_layer(Layer(4,4))
>>> firewall.add_layer(Layer(6,4))
>>> firewall.play(False)
>>> firewall.packet_position
7
>>> firewall.detections
[0, 6]
>>> firewall.calc_severity()
24
>>> l3 = Layer(0,3)
>>> l3.detect_after(1)
True
>>> l3.detect_after(2)
False
>>> l3.detect_after(3)
False
>>> l3.detect_after(4)
False
>>> l3.detect_after(5)
True
>>> firewall.find_delay_for_clear_run_simulation()
10
>>> firewall.find_delay_for_clear_run_math()
10
"""


class Layer:
    def __init__(self, id, depth):
        self.id = id
        self.depth = depth
        self.scanner_position = 1
        self.direction = 1
        self.modulus = (depth * 2) - 2

    def reset(self):
        self.scanner_position = 1
        self.direction = 1

    def tick(self):
        next_position = self.scanner_position + self.direction
        if next_position < 1 or next_position > self.depth:
            # change direction
            self.direction *= -1
            next_position = self.scanner_position + self.direction
        self.scanner_position = next_position

    def detect_after(self, time):
        return time % self.modulus == 1


class Firewall:
    def __init__(self):
        self.layers = {}
        self.max_layer_id = 0
        self.packet_position = -1
        self.detections = []

    def reset(self):
        self.packet_position = -1
        self.detections = []
        for layer in self.layers.values():
            layer.reset()

    def delay(self, delay):
        self.packet_position -= delay

    def add_layer(self, layer):
        self.layers[layer.id] = layer
        self.max_layer_id = max(self.max_layer_id, layer.id)

    def tick(self):
        self.packet_position += 1
        # check detection
        if self.packet_position in self.layers.keys():
            layer = self.layers[self.packet_position]
            if layer.scanner_position == 1:
                self.detections.append(layer.id)
        # move scanners
        for layer in self.layers.values():
            layer.tick()

    def play(self, stop_at_first):
        while self.packet_position <= self.max_layer_id:
            self.tick()
            if stop_at_first and len(self.detections) > 0:
                break

    def calc_severity(self):
        severity = 0
        for layer_id in self.detections:
            layer = self.layers[layer_id]
            severity += layer.id * layer.depth
        return severity

    # brute-force solution, doesn't scale
    def find_delay_for_clear_run_simulation(self):
        delay = 0
        while True:
            self.reset()
            self.delay(delay)
            self.play(True)
            if len(self.detections) == 0:
                break;
            # print("Delay: " , delay,  "; Detections: " , self.detections)
            delay += 1
        return delay

    # algorithmic
    def find_delay_for_clear_run_math(self):
        delay = 0
        while True:
            detection = False
            for layer in self.layers.values():
                if layer.detect_after(1 + delay + layer.id):
                    detection = True
                    break
            if not detection:
                return delay
            delay += 1


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = (line for line in input_file)
    return lines


input_lines = read_input("input.txt")
firewall = Firewall()
for line in input_lines:
    id, depth = line.split(": ")
    layer = Layer(int(id), int(depth))
    firewall.add_layer(layer)

firewall.play(False)

result1 = firewall.calc_severity()
print("Part1 Result is ", result1)
result2 = firewall.find_delay_for_clear_run_math()
print("Part2 Result is ", result2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
