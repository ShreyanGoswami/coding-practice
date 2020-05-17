#Incomplete
'''
To pass TLE implement using union by rank and path compression. 
'''
class DisjointSet:


    # Initialise every value to be a node
    def __init__(self, l):
        self.d = {}
        for x in l:
            self.d[x] = set([x])
    
    # Here a and b are not representative elements. They are the individual element
    # For each element see who is the parent. 
    # The parent with lesser rank needs to point to the parent of higher rank. 
    # In case two parents have the same rank take the first parent.
    # Increment the rank of the higher parent
    def union(self, a, b):
        self.d[a].update(list(self.d[b]))
        del(self.d[b])
    
    # Here x is the element whose representative element needs to be found
    # First way is to keep traversing through parent till we find the parent whose parent is none
    # In that case return that parent. Before returning connect the initial element to the top level parent(path compression)
    def find(self, x):
        for k,v in self.d.items():
            if x in v:
                return k

class Node:
    def __init__(self, data, rank):
        self.data = data
        self.rank = rank
        self.parent = None
    
    def setParent(self, parent):
        self.parent = parent
    
    def incrementRank(self):
        self.rank += 1

class DisjointSetOptimized():
    def __init__(self, l):
        self.l = {}
        for x in l:
            self.l[x] = Node(x, 0)
    
    def union(self, a, b):
        nodeA = self.l[a]
        nodeB = self.l[b]

        if nodeB.rank > nodeA.rank:
            nodeA.setParent(nodeB)
            nodeB.incrementRank()
        else:
            nodeB.setParent(nodeA)
            nodeA.incrementRank()
    
    def find(self, x):
        curr = self.l[x]
        if curr.parent is None:
            return x
        if curr.parent.parent is None:
            return curr.parent.data
        while curr.parent != None:
            curr = curr.parent
        nodeX = self.l[x]
        nodeX.parent = curr
        return curr.data

def constructEdges(graph):
    for k,v in graph.items():
        for x in set(v):
            try:
                graph[x].remove(k)
            except ValueError:
                pass
            yield [k,x]

def isCyclic(g,n):
    ds = DisjointSetOptimized(range(n))

    for edge in constructEdges(g):
        represent1 = ds.find(edge[0])
        represent2 = ds.find(edge[1])
        if represent1 == represent2:
            return 1
        ds.union(represent1, represent2)
    return 0

if __name__ == "__main__":
    d =  {0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
    print(isCyclic(d, 5))