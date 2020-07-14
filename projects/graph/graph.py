"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # init queue
        q = Queue()
        # init checked
        visited = set()
        # put starting vert in q
        q.enqueue(starting_vertex)
        # check while there is stuff in the q
        while q.size() > 0:
            # dequeue that next node
            visit = q.dequeue()
            # THIS IS WHERE YOU WOULD DO STUFF
            # print('BFT', visited)
            # if that node isn't in visited
            if visit not in visited:
                # add to visited set
                visited.add(visit)
                print(visit)
                # queue up it's neighbors
                for neighbor in self.get_neighbors(visit):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        # while there is stuff to check
        while s.size() > 0:
            # pop top vert
            visit = s.pop()
            # THIS IS WHERE YOU DO THE THINGS
            # print(visit)
            if visit not in visited:
                # add to visited
                visited.add(visit)
                print(visit)
                # push it's neighbors to the stack
                for neighbor in self.get_neighbors(visit):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # BECAUSE IT'S RECURSIVE YOU START WITH THIS IF STATEMENT
        print(starting_vertex)
        if visited is None:
            visited = set()
        visited.add(starting_vertex)

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        path = Queue()
        # Create a Set to store visited vertices
        visited = set()
        path.enqueue([starting_vertex])
        # While the queue is not empty...
        while path.size() > 0:
            # Dequeue the first PATH
            p = path.dequeue()
        # Grab the last vertex from the PATH
            last_vertex = p[-1]
        # If that vertex has not been visited...
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN PATH
            if last_vertex not in visited:
                # Mark it as visited...
                visited.add(last_vertex)
        # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
                # COPY THE PATH
                npath = p.copy()
        # APPEND THE NEIGHOR TO THE BACK
                npath.append(neighbor)

                if neighbor == destination_vertex:
                    return npath
                path.enqueue(npath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        path = Stack()
        # Create a Set to store visited vertices
        visited = set()
        path.push([starting_vertex])
        # While the queue is not empty...
        while path.size() > 0:
            # Dequeue the first PATH
            p = path.pop()
        # Grab the last vertex from the PATH
            last_vertex = p[-1]
        # If that vertex has not been visited...
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN PATH
            if last_vertex not in visited:
                # Mark it as visited...
                visited.add(last_vertex)
        # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
                # COPY THE PATH
                npath = p.copy()
        # APPEND THE NEIGHOR TO THE BACK
                npath.append(neighbor)

                if neighbor == destination_vertex:
                    return npath
                path.push(npath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(starting_vertex)
        if visited is None:
            visited = set()

        if path == None:
            path = []

        visited.add(starting_vertex)
        npath = [*path, starting_vertex]

        if npath[-1] == destination_vertex:
            return npath

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighborpath = self.dfs_recursive(
                    neighbor, destination_vertex, visited, npath)
                if neighborpath:
                    return neighborpath


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
