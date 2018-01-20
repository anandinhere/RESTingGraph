

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

