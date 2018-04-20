"""
>>> extract_relationships("ktlj (57)")
({}, {})
>>> extract_relationships("fwft (72) -> ktlj, cntj, xhth")
({'fwft': ['ktlj', 'cntj', 'xhth']}, {'ktlj': 'fwft', 'cntj': 'fwft', 'xhth': 'fwft'})
>>> head_of_tree( { "A" : "B", "B" : "C", "C" : "D" } )
'D'
>>> node_weight("cntj (57)")
{'cntj': 57}
>>> node_weight("ugml (68) -> gyxo, ebii, jptl")
{'ugml': 68}
>>> tree = { "A" : "B", "B" : "C", "D" : "E", "E" : "F", "C" : "E", "F": "G" }
>>> weights = { "A" : 1, "B" : 2, "C": 3, "D" : 4, "E": 5, "F": 6 }
>>> calc_weights(tree, weights)
{'A': 1, 'B': 3, 'C': 6, 'D': 4, 'E': 15, 'F': 21}
>>> lines = [
... "pbga (66)",
... "xhth (57)",
... "ebii (61)",
... "havc (66)",
... "ktlj (57)",
... "fwft (72) -> ktlj, cntj, xhth",
... "qoyq (66)",
... "padx (45) -> pbga, havc, qoyq",
... "tknk (41) -> ugml, padx, fwft",
... "jptl (61)",
... "ugml (68) -> gyxo, ebii, jptl",
... "gyxo (61)",
... "cntj (57)"
... ]
>>> (parent_to_children_tree, child_to_parent_tree, weights) = map_lines( lines )
>>> head = head_of_tree( child_to_parent_tree )
>>> cum_weights = calc_weights(child_to_parent_tree, weights)
>>> ugml_weight = cum_weights['ugml']
>>> padx_weight = cum_weights['padx']
>>> fwft_weight = cum_weights['fwft']
>>> unbalanced_node = find_unbalanced_node(head, parent_to_children_tree, cum_weights)
>>> correct_weight = find_correct_weight(unbalanced_node, child_to_parent_tree[unbalanced_node], parent_to_children_tree, weights, cum_weights)
>>> print( head, ugml_weight, padx_weight, fwft_weight, unbalanced_node, correct_weight )
tknk 251 243 243 ugml 60
"""


def extract_relationships(input):
    child_to_parent = {}
    parent_to_children = {}
    if " -> " in input:
        (parent, children) = input.split(" -> ")
        (parentName, weight) = (x.strip() for x in parent.split(" "))
        children = [x.strip() for x in children.split(",")]

        parent_to_children[parentName] = children
        for child in children:
            child_to_parent[child] = parentName

    return parent_to_children, child_to_parent


def node_weight(line):
    if " -> " in line:
        line = line.split(" -> ")[0].strip()

    (name, weight) = (x.strip() for x in line.split(" "))
    weight = int( weight.replace("(","").replace(")",""))
    return { name: weight }


def map_lines( lines ):
    child_to_parent_tree = {}
    parent_to_children_tree = {}
    weights = {}
    for line in lines:
        weights.update( node_weight( line ) )
        (parent_to_children, child_to_parent) = extract_relationships(line)
        child_to_parent_tree.update( child_to_parent )
        parent_to_children_tree.update(parent_to_children)
    return parent_to_children_tree, child_to_parent_tree, weights


def head_of_tree( tree ):
    item = list(tree.keys())[0]
    while item in tree:
        item = tree[ item ]
    return item


def read_input(filename):
    print("Opening file ", filename)
    input_file = open(filename, "r")
    lines = [line for line in input_file]
    return lines


in_list = read_input("input.txt")
(parent_to_children_tree, child_to_parent_tree, weights) = map_lines(in_list)
head = head_of_tree( child_to_parent_tree )
print("Part1 Result is ", head)


def calc_weights(tree, weights):
    cum_weights = weights.copy()
    for node in tree.keys():
        weight = weights[node]
        parent = tree[node]
        while parent in tree:
            cum_weights[parent] = cum_weights[parent] + weight
            parent = tree[parent]
    return cum_weights


cumulative_weights = calc_weights(child_to_parent_tree, weights)


def find_unbalanced_node(head, tree, weights):
    current_node = head;
    while current_node in tree:
        children = tree[current_node];
        # find which of the children differs
        weight_count = {}
        for child in children:
            weight = weights[child]
            if weight in weight_count:
                weight_count[weight] += 1
            else:
                weight_count[weight] = 1

        next=""
        for weight, count in weight_count.items():
            if count == 1:
                for child in children:
                    if weights[child] == weight:
                        next = child

        if next == "":
            # no unbalanced child found, so must be this node
            return current_node
        else:
            # unbalanced child found - drill into that one
            current_node = next

    return current_node


unbalanced_node = find_unbalanced_node(head, parent_to_children_tree, cumulative_weights)


def find_correct_weight(unbalanced_node, parent, parent_to_children_tree, weights, cum_weights):
    children = parent_to_children_tree[parent]
    target_weight = 0
    for child in children:
        if child != unbalanced_node:
            target_weight = cum_weights[child]

    diff = target_weight - cum_weights[unbalanced_node]
    return weights[unbalanced_node] + diff


correct_weight = find_correct_weight(unbalanced_node, child_to_parent_tree[unbalanced_node], parent_to_children_tree, weights, cumulative_weights)
print("Part2 Result is ", correct_weight)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
