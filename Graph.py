class Graph():
    def __init__(self):
        self.keys = []
        self.matrix = []
        self.size = 0

    def isAdjacent(self, i, j):
        return self.matrix[i][j] is not None
    
    def edgesFrom(self, i):
        return [(j, wt) for j, wt in enumerate(self.matrix[i]) if wt is not None ]
    
    def edgesTo(self, j):
        col =  [row[j] for row in self.matrix]
        return [(i, wt) for i, wt in enumerate(col) if wt is not None]
    
    def addVertex(self, key):
        [[ row.append(None) for row in self.matrix ]]
        self.size += 1
        self.matrix.append([None] * self.size)
        self.keys.append(key)
        return self.size
    
    def removeVertex(self, key):
        try:
            i = self.keys.index(key)
        except:
            print("chave não existe")
            return None
        [_.pop(i) for _ in self.matrix ]
        self.matrix.pop(i)
        return None
    
    def addEdge(self, k1, k2, wt):
        try:
            i = self.keys.index(k1)
            j = self.keys.index(k2)
        except:
            print("alguma das chaves não existe")
            return None
        self.matrix[i][j] = wt
        return None

    def removeEdge(self, k1, k2):
        try:
            i = self.keys.index(k1)
            j = self.keys.index(k2)
        except:
            print("alguma das chaves não existe")
            return None
        self.matrix[i][j] = None
        return None

    def getWeight(self, k1, k2):
        try:
            i = self.keys.index(k1)
            j = self.keys.index(k2)
        except:
            print("alguma das chaves não existe")
            return None
        return self.matrix[i][j]

def dfs(g: Graph, x, i = 0):
    n = i
    visited = [n]
    stack = g.edgesFrom(n)
    while len(stack) > 0:
        n = stack.pop()



def bfs(g, x, i = 0):
    visited = [i]
    queue = []


x = Graph()