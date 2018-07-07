import sys


class Vertex:
    """
    Class to store vertex information as adjacency list
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
        Connect nodes to the vertex
        :param nbr: Another Vertex
        :param weight: cost to travel from current Vertex to Neighbor
        :return:
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectsTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        :return: List of connected vertices
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        :return: The id(name )of the Vertex
        """
        return self.id

    def getWeight(self, nbr):
        """
        returns the cost to travel to a connected vertex
        :param nbr:
        :return:
        """
        return self.connectedTo[nbr]


class Graph:
    """
    Master class that store all vertices
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Adds a new vertex to the graph
        :param key: str::id
        :return: Vertex
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        :param n: str::id
        :return: Vertex if exists, none otherwise
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        """
        Connects two verices
        :param f: From Vertex
        :param t: To Vertex
        :param cost: int::Edge Weight or Cost
        :return:
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """
        :return: All the ids of the vertices in the graph
        """
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def getRouteCost(g, route):
    """
    For a given graph and route, returns the associated cost
    :param g: Graph
    :param route: str::Route (example: "A-B-C")
    :return:int:: cost or NO SUCH ROUTE
    """
    route = route.split('-')
    idx = 1
    routeCost = 0
    try:
        while (idx < len(route)):
            routeCost += ((g.getVertex(route[idx - 1])).getWeight(g.getVertex(route[idx])))
            idx += 1
        return routeCost
    except KeyError:
        return "NO SUCH ROUTE"


def findShortestPath(g, source, dest, visited=[], costs={}, lastVisited={}):
    """
    Return Shortest Path using dijkstra algorithm (recursive)
    :param g: Graph
    :param source: Source Vertex
    :param dest: Destination Vertex
    :param visited: list of already visited vertices
    :param costs: Dictionary containing the costs for the visits
    :param lastVisited: Last visited vertex
    :return:
    """
    if len(visited) == 0:
        costs[source] = 0
        if source == dest:
            return 0

    if source == dest:
        path = []
        while dest != None:
            path.append(dest)
            dest = lastVisited.get(dest, None)
        return costs[source]

    for nbr in g.getVertex(source).getConnections():
        if nbr.getId() not in visited:
            prevCost = costs.get(nbr.getId(), sys.maxsize)
            newCost = costs[source] + g.getVertex(source).getWeight(nbr)
            if newCost < prevCost:
                costs[nbr.getId()] = newCost
                lastVisited[nbr.getId()] = source
    visited.append(source)
    notVisited = dict((v.getId(), costs.get(v.getId(), sys.maxsize)) for v in g if v.getId() not in visited)
    nearest = min(notVisited, key=notVisited.get)
    return findShortestPath(g, nearest, dest, visited, costs, lastVisited)


def initializeGraph(input_data=['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']):
    """
    Initializes the graph, must me list of strs
    :param input_data: list of strs
    :return: Graph
    """
    g = Graph()
    vertList = []
    for i in input_data:
        if i[0] not in vertList:
            vertList.append(i[0])
        if i[1] not in vertList:
            vertList.append(i[1])
    for v in vertList:
        g.addVertex(v)
    for e in input_data:
        g.addEdge(e[0], e[1], int(e[2:]))
    return g


if __name__ == '__main__':
    #######1-5#########
    routes = ['A-B-C', 'A-D', 'A-D-C', 'A-E-B-C-D', 'A-E-D']
    for route in routes:
        print(getRouteCost(initializeGraph(), route))
    #######8-9#########
    print(findShortestPath(initializeGraph(), 'A', 'C', visited=[], costs={}, lastVisited={}))
    print(findShortestPath(initializeGraph(), 'C', 'C', visited=[], costs={}, lastVisited={}))

