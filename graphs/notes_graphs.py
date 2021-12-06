'''
A graph is a collection of nodes that may or may not be connected one another. 

When approaching a graph problem, what are the key things, concepts or properties that I notice to be glaring?

    Is the graph connected? (any node can reach any node)
    Is it directed? (ex flight paths may be directed, facebook friendships may be undirected)
    Is it cyclic? (imagine if you have three or more nodes that go in an infinite loop or if you end up visiting the same node twice)
        If you are dealing with a cyclic graph, this is important due to preventing an algorithm locking itself into an infinite loop
    
Matrices are a graph structure

A graph is usually represented as an adjacency list

Space complexity of storing a graph is O(V+E)
Time complexity of traversing a graph is O(V+E)

Most common operation that is performed on graphs is a DFS and a BFS
    In a DFS, you go deep before wide, exploring the first in a list of connected vertices, with each vertex accessed
    In a BFS, you go wide before deep, exploring all connected vertices first, before moving on to the next

Other operations include adding/removing vertices/edges
'''
