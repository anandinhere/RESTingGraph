

class Node:
    """A simple Graph Node class"""

    def __init__(self,key=None,weight=None):
        self._isVisited = None
        self._key = key
        self._inRecurseStack = None
        self._tempWeight = None
        self._parentKey = None
        self._edgeWeight=weight

    @property
    def isVisited(self):
        return self._isVisited

    @property
    def key(self):
        return self._key

    @property
    def inRecurseStack(self):
        return self._inRecurseStack

    @property
    def tempWeight(self):
        return self._tempWeight

    @property
    def parentKey(self):
        return self._parentKey

    @property
    def edgeWeight(self):
        return self._edgeWeight


    #Setters
    @isVisited.setter
    def isVisited(self,val):
        _isVisited = val

    @key.setter
    def key(self,val):
        _isVisitedkey = val

    @inRecurseStack.setter
    def inRecurseStack(self,val):
        _inRecurseStack = val

    @tempWeight.setter
    def tempWeight(self,val):
        _tempWeight = val

    @parentKey.setter
    def parentKey(self,val):
        _parentKey = val

    @edgeWeight.setter
    def edgeWeight(self,val):
        _edgeWeight = val