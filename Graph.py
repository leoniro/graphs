class Graph():
    def __init__(self):
        self.matrix = []
        self.size = 0

    def isAdjacent(self, i, j):
        return self.matrix[i][j] is not None
    
    def edgesFrom(self, i):
        return [(j, wt) for j, wt in enumerate(self.matrix[i]) if wt is not None ]
    
    def edgesTo(self, j):
        col =  [row[j] for row in self.matrix]
        return [(i, wt) for i, wt in enumerate(col) if wt is not None]
    
    def addVertex(self, n = 1):
        for i in range(0,n):
            [[ row.append(None) for row in self.matrix ]]
            self.size += 1
            self.matrix.append([None] * self.size)
        return self.size
    
    def removeVertex(self, i):
        [_.pop(i) for _ in self.matrix ]
        self.matrix.pop(i)
        return None
    
    def addEdge(self, i, j, wt):
        self.matrix[i][j] = wt
        return None

    def removeEdge(self, i, j):
        self.matrix[i][j] = None
        return None

    def getWeight(self, i,j):
        return self.matrix[i][j]


x = Graph()
