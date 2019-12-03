from collections import deque
from string import ascii_uppercase
from itertools import chain, product


def breadth_first_search(graph, root): 
    total = 0 
    # print(graph)
    visited, queue = set(), deque([root])
    while queue: 
        vertex = queue.popleft()
        if isinstance(vertex, Node):
            vertex = vertex.name
        for neighbour in graph[vertex]: 
            if neighbour.name not in visited: 
                visited.add(neighbour.name) 
                queue.append(neighbour) 
                # print(total, neighbour.metadata)
                total += sum(neighbour.metadata)
    return total
    
def value_node(vertex):
    value = 0
    if not vertex.child_nodes:
        value += sum(vertex.metadata)
        # print('value', value)
    else:
        # print(vertex.metadata)
        for i in vertex.metadata:
            i -= 1
            # print(i, len(vertex.child_nodes))
            try:
                new =  vertex.child_nodes[i]
                # print('new', new)
                value += value_node(new)
            except IndexError:
                pass
    return value

def letters():
    for chars in chain(*(product(ascii_uppercase, repeat=i+1) for i in range(3))):
        yield ''.join(chars)
        
names = letters()        
graph = {}

class Node():

    def __init__(self, name, nr_child_nodes, nr_metadata_entries, numbers):
        self.name = name
        self.nr_child_nodes = nr_child_nodes
        self.nr_metadata_entries = nr_metadata_entries
        self.numbers = numbers
        
        self.child_nodes = []
        self.metadata = []
        
        for nr_child_node in range(self.nr_child_nodes):
            child_nr_child_nodes = deque.popleft(self.numbers)
            child_nr_metadata_entries = deque.popleft(self.numbers)
            name = next(names)
            node = Node(name, child_nr_child_nodes, child_nr_metadata_entries, self.numbers)
            # print(node)
            self.child_nodes.append(node)
            
        for _ in range(nr_metadata_entries):
            self.metadata.append(deque.popleft(self.numbers))
            
        graph[self.name] = self.child_nodes

    def __str__(self):
        return '{}: {}'.format(self.name, [node.name for node in self.child_nodes])

def main(part=1, data=None):
    if data is None:
        with open('data/08.txt') as f:
            data = f.read().strip()
    numbers = deque(map(int, data.split()))
    
    while numbers:
        nr_child_nodes = deque.popleft(numbers)
        nr_metadata_entries = deque.popleft(numbers)
        name = next(names)
        node = Node(name, nr_child_nodes, nr_metadata_entries, numbers)
        # print(node)
        
    if part==1:
        return breadth_first_search(graph, 'A') + sum(node.metadata)
    else:
        return value_node(node)
                
        
if __name__ == '__main__':
    names = letters()        
    graph = {}
    data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    assert main(data=data) == 138
    assert main(part=2, data=data) == 66
    
    names = letters()        
    graph = {}
    # print(main())
    print(main(part=2))