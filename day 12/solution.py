"""
>>> net = Network()
>>> net.add_node("0 <-> 2")
>>> net.add_node("0 <-> 2")
>>> net.add_node("0 <-> 2")
>>> net.add_node("1 <-> 1")
>>> net.add_node("2 <-> 0, 3, 4")
>>> net.add_node("3 <-> 2, 4")
>>> net.add_node("4 <-> 2, 3, 6")
>>> net.add_node("5 <-> 6")
>>> net.add_node("6 <-> 4, 5")
>>> len(net.nodes)
7
>>> net.nodes["4"].connections
['2', '3', '6']
>>> len(net.connected("0"))
6
>>> net.group_count()
2
"""


class Node:
    def __init__(self, id, cons):
        self.id = id
        self.connections = [x.strip() for x in cons.split(",")]


class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, line):
        node, connections = line.split(" <-> ")
        self.nodes[node] = Node(node, connections)
        return

    def connected(self, node_id):
        nodes_connected = set()
        nodes_to_check = set()
        nodes_to_check.add(node_id)
        while(len(nodes_to_check)>0):
            node_id = nodes_to_check.pop()
            nodes_connected.add(node_id)
            connections = self.nodes[node_id].connections
            for connection in connections:
                if connection not in nodes_connected:
                    nodes_to_check.add(connection)

        return nodes_connected

    def group_count(self):
        groups = 0;
        node_ids = set(self.nodes.keys())
        while len(node_ids) > 0:
            node_id = node_ids.pop()
            groups += 1
            connected = self.connected(node_id)
            node_ids = node_ids.difference(connected)
        return groups


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = (line for line in input_file)
    return lines


input_lines = read_input("input.txt")
net = Network()
for line in input_lines:
    net.add_node(line)


result1 = len(net.connected("0"))
print("Part1 Result is ", result1)
print("Part2 Result is ", net.group_count())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
