from node import Node
from edge import Edge

class Graph:
    """A simple Graph class"""
    def __init__(self):
        self._graphName = None
        self._graphID = None
        self._nodeDict = {}
        self._adjacencyNodeListsDict = {}
        self._edgeList = []

    #Getters
    @property
    def graphName(self):
        return self._graphName

    @property
    def graphID(self):
        return self._graphID

    @property
    def nodeDict(self):
        return self._nodeDict

    @property
    def adjacencyNodeListsDict(self):
        return self._adjacencyNodeListsDict

    @property
    def edgeList(self):
        return self._edgeList

    #Setters

    @graphName.setter
    def graphName(self,val):
        _graphName = val

    @graphID.setter
    def graphID(self, val):
        _graphID = val

    @nodeDict.setter
    def nodeDict(self, val):
        _nodeDict = val

    @adjacencyNodeListsDict.setter
    def adjacencyNodeListsDict(self, val):
        _adjacencyNodeListsDict = val

    #Instance Methods
    def addNode(self,node):
        if node.key not in self.nodeDict:
            self.nodeDict[node.key] = node
            self.adjacencyNodeListsDict[node.key] = []
        else:
            return

    def addEdge(self,from_key,to_key,edge_weight):
        if from_key not in self.nodeDict:
            self.addNode(from_key)

        if to_key not in self.nodeDict:
            self.addNode(to_key)

        self.adjacencyNodeListsDict[from_key].append(Node(key=to_key,weight=edge_weight))
        self.edgeList.append(Edge(from_key,to_key,edge_weight))

    def printEdges(self):
        for edge in self.edgeList:
            print edge._fromNodeKey, edge._toNodeKey, edge.weight


