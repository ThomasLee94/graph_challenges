# classes.util.read_data

## graph_from_file
```python
graph_from_file(filepath)
```

Opens a text file and returns:
 graph: graph instance
 verticies: list
 edges: list of tuples

## string_to_tuple
```python
string_to_tuple(string)
```

turns a string into a tuple

# classes.linkedlist

## LinkedList
```python
LinkedList(self, iterable=None)
```

### items
```python
LinkedList.items(self)
```
Return a list of all items in this linked list.
Best and worst case running time: Theta(n) for n items in the list
because we always need to loop through all n nodes.
### is_empty
```python
LinkedList.is_empty(self) -> bool
```
Return True if this linked list is empty, or False.
### length
```python
LinkedList.length(self)
```
Return the length of this linked list by traversing its nodes.
Best and worst case running time: ??? under what conditions? [TODO]
### get_at_index
```python
LinkedList.get_at_index(self, index)
```
Return the item at the given index in this linked list, or
raise ValueError if the given index is out of range of the list size.
Best case running time: ??? under what conditions? [TODO]
Worst case running time: ??? under what conditions? [TODO]
### get_index_node
```python
LinkedList.get_index_node(self, index)
```

Return node at given index

### insert_at_index
```python
LinkedList.insert_at_index(self, index, item)
```
Insert the given item at the given index in this linked list, or
raise ValueError if the given index is out of range of the list size.
### append
```python
LinkedList.append(self, item)
```
Insert the given item at the tail of this linked list.
Best and worst case running time: ??? under what conditions? [TODO]
### prepend
```python
LinkedList.prepend(self, item)
```
Insert the given item at the head of this linked list.
Best and worst case running time: ??? under what conditions? [TODO]
### find
```python
LinkedList.find(self, quality)
```
Return an item from this linked list satisfying the given quality.
Best case running time: Omega(1) if item is near the head of the list.
Worst case running time: O(n) if item is near the tail of the list or
not present and we need to loop through all n nodes in the list.
### replace
```python
LinkedList.replace(self, old_item, new_item)
```
Replace the given old_item in this linked list with given new_item
using the same node, or raise ValueError if old_item is not found.
### delete
```python
LinkedList.delete(self, item)
```
Delete the given item from this linked list, or raise ValueError.
Best case running time: ??? under what conditions? [TODO]
Worst case running time: ??? under what conditions? [TODO]
# classes.queue

## LinkedQueue
```python
LinkedQueue(self, iterable=None)
```

### is_empty
```python
LinkedQueue.is_empty(self) -> bool
```
Return True if this queue is empty, or False otherwise.
### length
```python
LinkedQueue.length(self) -> int
```
Return the number of items in this queue.
### enqueue
```python
LinkedQueue.enqueue(self, item)
```
Insert the given item at the back of this queue.
### front
```python
LinkedQueue.front(self)
```
Return the item at the front of this queue without removing it,
or None if this queue is empty.
### dequeue
```python
LinkedQueue.dequeue(self)
```
Remove and return the item at the front of this queue,
or raise ValueError if this queue is empty.
# classes.stack

## LinkedStack
```python
LinkedStack(self, iterable=None)
```

### is_empty
```python
LinkedStack.is_empty(self)
```
Return True if this stack is empty, or False otherwise.
### length
```python
LinkedStack.length(self)
```
Return the number of items in this stack.
### push
```python
LinkedStack.push(self, item)
```
Insert the given item on the top of this stack.
### peek
```python
LinkedStack.peek(self)
```
Return the item on the top of this stack without removing it,
or None if this stack is empty.
### pop
```python
LinkedStack.pop(self)
```
Remove and return the item on the top of this stack,
or raise ValueError if this stack is empty.
# classes.vertex

## Vertex
```python
Vertex(self, vertex: str)
```

### add_neighbour
```python
Vertex.add_neighbour(self, vertex: object, weight=0)
```

add a neighbour along a weighted edge

### get_neighbours
```python
Vertex.get_neighbours(self) -> dict
```
returns all vertices (nodes) connected to this vertex (node)
# classes.graph

## Graph
```python
Graph(self)
```
essential facts and functionalities of an undirected graph
### add_vertex
```python
Graph.add_vertex(self, key: str) -> object
```

add a new vertex object to the graph with
the given key and return the vertex

### get_vertex
```python
Graph.get_vertex(self, key: str) -> object
```
return the vertex if it exists
### add_edge
```python
Graph.add_edge(self, vertex_a: str, vertex_b: str, weight=0)
```

add an edge from vertex a to vertex b with a weight

### get_vertices
```python
Graph.get_vertices(self)
```
return all the vertices in the graph
### get_edges
```python
Graph.get_edges(self, vertex: str) -> [<class 'str'>]
```
Returns all of the edges of given vertex
### breadth_first_search
```python
Graph.breadth_first_search(self, vertex_a: str, vertex_b: str) -> object
```

Executes a breadth for search on the given graph.

Args:
    vertex_a: from vertex.
    vertex_b: to vertex.
Returns:
    a dict of containing parent and child verticies.

### dfs_recursive
```python
Graph.dfs_recursive(self, vertex_a: str, vertex_b: str, visited_list: [<class 'str'>], visited_set, custom_func) -> (<class 'bool'>, [<class 'str'>])
```

Executes a depth first search on the given graph.
Args
    vertex_a: start vertex
    vertex_b: to vertex
    visited_list: keeps track of visited verticies in order of traversal
    visited: set method to keep track of visited verticies.
    custom_func: execute custom function on vertex
Returns
    If vertex_b is in any branch from vertex_a: return (True, verticies_list)
    If vertex_b not in any branch from vertex_a: return (False, verticies_list)

### min_weight_path
```python
Graph.min_weight_path(self, vertex_a: str, vertex_b: str) -> object
```

An implementation of Dijkstra greedy algorithm, it will return the shortest weighted
path from vertex_a to vertex_b.
Args
    vertex_a: start vertex
    vertex_b: end vertex
Returns

## fill
```python
fill(graph: classes.graph.Graph, verticies: [<class 'str'>], edges_and_weight: [<class 'str'>]) -> classes.graph.Graph
```

Fills graph based on input verticies and edges and optional weights

# classes.digraph

## Digraph
```python
Digraph(self)
```
essential facts and functionalities of a directed graph
### add_edge
```python
Digraph.add_edge(self, vertex_a: str, vertex_b: str, weight=0)
```

add an edge between both vertex a to vertex b with a weight

### get_vertices
```python
Digraph.get_vertices(self)
```
return all the vertices in the graph
