import queue
import random
import math
import itertools
from memo import memo
from graph_decorator import *

def bfs(graph, init, is_end = lambda v: False):
        """
             graph fn which blah blah
        """
        to_visit = queue.Queue()
        to_visit.put(init)
        # in n-th run of while loop this contains blah blah
        visited = {init:None}
        while not to_visit.empty():
            v = to_visit.get()
            if is_end(v):
                return visited, v
            for neigh, val in graph(v):
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
        for neigh, val in graph(v):
            if neigh not in visited:
                visited[neigh] = v
                _dfs(neigh)

    try:
        _dfs(init)
    except ResultException as e:
        return visited, e.val
    return visited, None

def dijkstra(graph, init, is_end = lambda v:False):
    distance = {}
    distance[init] = 0
    prev = {}
    prev[init] = None

    to_visit = {}
    to_visit[init] = 0
    while to_visit:

        sortedList = sorted(to_visit.items(), key=lambda x:x[1])
        node, nodeDist = sortedList[0]

        del to_visit[node]

        distance[node] = nodeDist

        if is_end(node):
            return distance, prev, node
        for v, dist in graph(node):
            tmp = nodeDist + dist

            if v in distance:
                if tmp < distance[v]:
                    raise StandardError

            elif v not in to_visit:
                to_visit[v] = tmp
                prev[v] = node


            elif v in to_visit:
                if to_visit[v] > tmp:
                    to_visit[v] = tmp
                    prev[v] = node

    return distance, prev

def random_graph(p, val = -1):
    @memo
    def graph(v):
        res = []
        for i in range(-99, 99):
            if random.random() < math.pow(p,abs(i)):

                if val == -1:
                    randVal = rng.random()
                else:
                    randVal = val
                res.append( (v+i, randVal) )
        return res
    return graph
\


#ludia je set stringov kazdy bude mat jeden znak vo vrchole bude string ktory sa bude rozkladat, cenyLudi je dict s klucmi s ludia
def bridge_graph(ludia, cenyLudi):
    @memo
    def graph(v):
        """
            vrchol reprezentovat stranu mosta na ktoru sa chcem dostat
            bude to dvojica t a set
                t znamena ci tam je torch
                set budu ludia na tej strane
                ak je vo v torch tak vrati ('', set-1 ) set-1 znamena vsetky kombinacie z velkostou set-1
                ak tam torch nie je vrati ('t', set+2) set+2 znamena setVsetkychLudi - set a z toho dvojkombinacie

            pouzijem itertools.combinations(iterable, size) na generovanie 1 a 2 kombinacii
        """
        torch, peopleString = v
        people = set()
        for x in peopleString:
            people.add(x)

        res = []

        if(torch == 't'):
            pom = itertools.combinations(people, 1)
            for x in pom:
                foo = set(x)
                res.append( ( ('', ''.join(sorted(people-foo))), cenyLudi[foo.pop()] ) )

        if(torch == ''):
            pom = ludia - people
            pom = itertools.combinations(pom, 2)
            for x in pom:
                a = x[0]
                b = x[1]
                foo = set()
                for y in x:
                    foo.add(y)
                val = max(cenyLudi[a],cenyLudi[b])
                #ktory idiot navrhol ze zjednotenie bude | a nie +
                res.append( ( ('t', ''.join(sorted(people | foo))), val ) )

        return res
    return graph

def prob_grid(p, val = -1):
    @memo
    def graph(v):
        x,y = v
        dd = [(-1,0), (1, 0), (0, -1), (0, 1)]
        res = []
        for dx, dy in dd:
            if random.random() < p:
                if val == -1:
                    randVal = random.randint(1,5)
                else:
                    randVal = val
                res.append( ((x+dx, y+dy), randVal) )
        return res
    return graph

def end_dist(n):
    def res(v):
        return v == n
    return res


def get_path(visited, end):
    path = ()
    v = end
    while True:
        path = (v,) + path
        v = visited[v]
        if v == None:
            break
    return path

def get_path_dijkstra(visited, end, dist):
    path = ()
    v = end
    while True:
        path = ([v, dist[v]],) + path
        v = visited[v]
        if v == None:
            break
    return path

def bridge_end(v):
    torch, pS = v
    return pS == 'ABCD'

def simple_graph(v):
    return [(v+1,random.randint(1,2))]

def simple_end(n):
    def res(v):
        return v == n
    return res

if __name__ == '__main__':
    graph = simple_graph
    #graph = bridge_graph(set(['A','B','C','D']), {'A':7, 'B':2, 'C':1, 'D':10})
    #print(graph(('','')))
    #for x, val in graph(('','')):
    #    print(x, val)
#    visited, prev, node = dijkstra(graph, ('','') , bridge_end)
#    bfsprev, bfsnode = bfs(graph, ('','') , bridge_end)
    visited, prev, node = dijkstra(graph, 0 , simple_end(5))
    graph = cena_dekorator(graph, 0, 1, 1)
    bfsprev, bfsnode = bfs(graph, 0 , simple_end(5))
    if prev:
        print(get_path_dijkstra(prev, node,visited))

        #print(visited[node])
        print(get_path(bfsprev, bfsnode))
        print('')

    else:
        print('To sa nedaaaaaa')

