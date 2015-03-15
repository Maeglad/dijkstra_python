def cena_dekorator(graph, od, do, cena):
    def wraper(v):
        if v == od:
            res = graph(v)
            for x in res:
                v, dist = x
                if v == do:
                    res.remove(x)
            res.append((do,cena))
        else:
            return graph(v)
        return res
    return wraper

