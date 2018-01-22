
from graph.edge import Edge
from graph.node import Node
import json
import os

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
            self.addNode(Node(from_key))

        if to_key not in self.nodeDict:
            self.addNode(Node(to_key))

        self.adjacencyNodeListsDict[from_key].append((to_key,edge_weight))
        self.edgeList.append(Edge(from_key,to_key,edge_weight))

    def printEdges(self):
        for edge in self.edgeList:
            print(edge._fromNodeKey, edge._toNodeKey, edge.weight)


    def saveGraph(self,graphJson, graphName):
        JSON_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'graphFileDB')
        with open(os.path.join(JSON_FILES_PATH, 'graphName'), 'w') as outfile:
            json.dump(graphJson, outfile, indent=4)


