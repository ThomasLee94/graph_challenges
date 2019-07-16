# graph

## Graph
```python
Graph(self)
```

### add_vertex
```python
Graph.add_vertex(self, key: str) -> object
```

add a new vertex object to the graph with
the given key and return the vertex

### get_vertex
```python
Graph.get_vertex(self, key: str)
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
# vertex

## Vertex
```python
Vertex(self, vertex: str)
```

### add_neighbor
```python
Vertex.add_neighbor(self, vertex: object, weight=0)
```

add a neighbor along a weighted edge

### get_neighbors
```python
Vertex.get_neighbors(self) -> dict
```
returns all vertices (nodes) connected to this vertex (node)
