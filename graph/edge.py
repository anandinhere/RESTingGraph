


class Edge:
    """A simple Graph Edge class"""

    def __init__(self,fromNodeKey,toNodeKey,weight):
        self._fromNodeKey = fromNodeKey
        self._toNodeKey = toNodeKey
        self._weight = weight



    @property
    def fromNodeKey(self):
        return self._fromNodeKey

    @property
    def toNodeKey(self):
        return self._toNodeKey

    @property
    def weight(self):
        return self._weight

    #Setters
    @fromNodeKey.setter
    def fromNodeKey(self,val):
        _fromNodeKey = val

    @toNodeKey.setter
    def toNodeKey(self,val):
        _toNodeKey = val

    @weight.setter
    def weight(self,val):
        _weight = val

