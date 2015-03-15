import unittest
from graph import *
from graph_decorator import *

def rand_graph_end(n):
    def res(v):
        return v ==  n
    return res
def prob_dist(n):
    def res(v):
        return v == (n, 0)
    return res

class Test(unittest.TestCase):

    def setUp(self):
        self.val = 0

    def test_small(self):
        bfsprev, bfsnode = bfs(prob_grid(1), (0,0), prob_dist(5))
        dijdist, dijprev, dijnode = dijkstra(prob_grid(1,1), (0,0), prob_dist(5))
        path = get_path(bfsprev, bfsnode)
        path2 = get_path(dijprev, dijnode)
        self.assertEqual(path, path2)

    def test_bfs_dij_cena1(self):
        graph = random_graph(1,1)
        for i in range(10):
            randVal = random.randint(-1000,1000)
            bfsprev, bfsnode = bfs(graph, 0, rand_graph_end(randVal))
            dijdist, dijprev, dijnode = dijkstra(graph, 0, rand_graph_end(randVal))
            path = get_path(bfsprev, bfsnode)
            path2 = get_path(dijprev, dijnode)
            self.assertEqual(path, path2)

    def test_memo(self):
        #memo by malo volat pre rovnaku premennu funkciu iba raz
        @memo
        def pocitadlo(premenna):
            pocitadlo.pocet_volani += 1
            return premenna;

        pocitadlo.pocet_volani = 0

        pocitadlo(1)
        pocitadlo(1)
        self.assertEqual(pocitadlo.pocet_volani, 1)

        pocitadlo('aaaa')
        self.assertEqual(pocitadlo.pocet_volani, 2)


    def test_ten_bridge_problem(self):
        graph = bridge_graph(set(['A','B','C','D']),{'A':1, 'B':2, 'C':7, 'D':10})
        visited, prev, node = dijkstra(graph, ('',''), bridge_end)
        dist = visited[('t','ABCD')]
        self.assertEqual(dist, 17)

        graph = cena_dekorator(graph, ('',''), ('t','AB'),0 )
        visited, prev, node = dijkstra(graph, ('',''), bridge_end)
        dist = visited[('t','ABCD')]
        self.assertEqual(dist,15)

        graph = cena_dekorator(graph, ('',''), ('t','CD'),20 )
        visited, prev, node = dijkstra(graph, ('',''), bridge_end)
        dist = visited[('t','ABCD')]
        self.assertEqual(dist,15)


if __name__ == '__main__':
    unittest.main()
