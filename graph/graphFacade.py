

import threading
import time
from graph.graph import Graph
from queue import Queue


class GraphFacade(threading.Thread):
    def __init__(self,updateGraphEvent, readGraph,threadQueue):
        threading.Thread.__init__(self)
        self._updateGraphEvent = updateGraphEvent

        def run(self):
            while True:
                time.sleep(60)
                self._updateGraphEvent.clear()
                #wait until running threads are complete
                threadQueue.join()
                readGraph.addEdge(2,3,4)
                self._updateGraphEvent.set()