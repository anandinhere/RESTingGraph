

class Node:
    """A simple Graph Node class"""

    def __init__(self,key):
        self._isVisited = None
        self._key = None
        self._inRecurseStack = None
        self._tempWeight = None
        self._parentKey = None

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