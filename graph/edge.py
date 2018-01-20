
class Node:
    """A simple Graph Edge class"""

    def __init__(self):
        self._fromNodeKey = None
        self._toNodeKey = None
        self._weight = None



    @property
    def fromNodeKey(self):
        return self._fromNodeKey

    @property
    def toNodeKey(self):
        return self._toNodeKey

    @property
    def weight(self):
        return self._weight

