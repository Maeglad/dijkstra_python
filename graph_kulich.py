from queue import Queue
import random
from memo import memo

def bfs(graph, init, is_end = lambda v: False):
    """
        graph fn which blah blah
    """
    to_visit = Queue()
    to_visit.put(init)
    # in n-th run of while loop this contains blah blah
    visited = {init:None}
    while not to_visit.empty():
        v = to_visit.get()
        if is_end(v):
            return visited, v
        for neigh in graph(v):
            if neigh not in visited:
                visited[neigh]=v
                to_visit.put(neigh)
    return visited, None



class ResultException(Exception):
    def __init__(self, val):
        self.val = val



def dfs(graph, init, is_end = lambda v: False):
    visited = {init:None}
    def _dfs(v):
        if is_end(v):
            raise ResultException(v)
        for neigh in graph(v):
            if neigh not in visited:
                visited[neigh] = v
                _dfs(neigh)
    try:
        _dfs(init)
    except ResultException as e:
        return visited, e.val
    return visited, None

def get_path(visited, end):
    path = ()
    v = end
    while True:
        path = (v,) + path
        v = visited[v]
        if v == None:
            break
    return path

def prob_grid(p):
    @memo
    def graph(v):
        x,y = v
        dd = [(-1,0), (1, 0), (0, -1), (0, 1)]
        return [(x+dx, y+dy) for dx, dy in dd if random.random() < p]
    return graph

def further_ge(n):
    def res(v):
        x,y = v
        return abs(x) + abs(y) >= n
    return res

if __name__ == '__main__':
    g = prob_grid(0.5)
    visited, end = bfs(prob_grid(0.6), (0,0), further_ge(10))
    if end:
        print(visited)
    else:
        print('To sa nedaaaaaa')
