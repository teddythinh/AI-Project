import numpy as np
from collections import defaultdict
import sys
from queue import PriorityQueue

def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
    #path=[]
    #visited={} 

    #return visited, path
    # if found the end, return the path
    matrix = np.array(matrix)
    visited = {}
    path = []
    stack = []
    stack.append(start)
    visited[start] = None
    while stack:
        node = stack.pop()
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                stack.append(i)
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)
            end=visited[end]
        path.append(start)
        path.reverse()
    return visited, path

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    #path=[]
    #visited={}
   
    #return visited, path

    matrix = np.array(matrix)
    visited = {}
    path = []
    queue = []
    queue.append(start)
    visited[start] = None
    while queue:
        node = queue.pop(0) # make a queue
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                queue.append(i)
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)
            end=visited[end]
        path.append(start)
        path.reverse()
    
    return visited, path

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    #path=[]
    #visited={}
    #return visited, path

    matrix = np.array(matrix)
    visited = {}
    path = []
    frontier = PriorityQueue()
    cost = 0
    node = start
    visited[start] = None
    frontier.put((cost, node))
    while not frontier.empty():
        node = frontier.get()[1]
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                cost = matrix[node][i]
                frontier.put((cost, i))
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)
            end=visited[end]
        path.append(start)
        path.reverse()
    return visited, path
    
def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    #path=[]
    #visited={}
    #return visited, path
    #using priority queue
    matrix = np.array(matrix)
    visited = {}
    path = []
    queue = PriorityQueue()
    cost = 0
    node = start
    # heuristic = edge weight
    heuristic = matrix[node]
    heuristic[node] = 0
    visited[start] = None
    queue.put((cost, node))
    while not queue.empty():
        node = queue.get()[1]
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                cost = matrix[node][i]
                queue.put((cost, i))
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)
            end=visited[end]
        path.append(start)
        path.reverse()
    return visited, path

def euclidean_distance(a, b):
    ans = np.linalg.norm(a - b)
    return ans

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    #path=[]
    #visited={}
    #return visited, path
    #using euclidean distance
    
    matrix = np.array(matrix)
    visited = {}
    path = []
    open = []
    close = []
    node = start
    visited[start] = None
    open.append(start)
    heuristic = matrix[node]
    heuristic[node] = 0
    while open:
        node = open.pop(0)
        close.append(node)
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                heuristic[i] = euclidean_distance(pos[node], pos[i])
                open.append(i)
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)
            end=visited[end]
        path.append(start)
        path.reverse()
    return visited, path





