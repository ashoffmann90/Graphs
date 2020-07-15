from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # creating graph
    for pair in ancestors:
        # checking each node to see if it already exists, if it is then add the vertex
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    q = Queue()
    longest_path = []
    # node_location = 0
    q.enqueue([starting_node])

    while q.size() > 0:
        deq = q.dequeue()
        if len(deq) > len(longest_path):
            longest_path = deq
        if len(deq) == len(longest_path):
            if deq[-1] < longest_path[-1]:
                longest_path = deq
        for neighbor in graph.get_neighbors(deq[-1]):
            temp_path = deq.copy()
            temp_path.append(neighbor)
            q.enqueue(temp_path)
    if len(longest_path) <= 1:
        return -1
    return longest_path[-1]


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

    # Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

    # Clarifications:
    # * The input will not be empty.
    # * There are no cycles in the input.
    # * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    # * IDs will always be positive integers.
    # * A parent may have any number of children.

    # # DFS
    # # init a graph
    # graph = Graph()
    # # storing what we need to check next, FILO
    # stack = Stack()
    # # start here, by adding starting_point to the stack
    # path = [starting_node]
    # # add path to the stack, path is going to be the entire path (not just a single node)
    # stack.push(path)
    # # create a dictionary, each k, v pair is going to be an edge
    # graph = {}
    # # looping through input to create the graph
    # for k, v in ancestors:
    #     if v not in graph:
    #         graph[v] = set()
    #         print(v)
    #     if k not in graph:
    #         graph[k] = set()
    #         print(k)
    #     graph[v].add(k)

    # visited = []

    # ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
    #              (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
