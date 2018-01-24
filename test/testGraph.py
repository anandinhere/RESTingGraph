
from graph import graph,edge,node,graphFacade
import threading,time

from queue import Queue

readGraph = graph.Graph()

#
# g.addEdge(0,1,10)
# g.addEdge(0,2,10)
# g.printEdges()
# print(g.adjacencyNodeListsDict)
# for nodeKey in  g.adjacencyNodeListsDict:
#     for tuple in g.adjacencyNodeListsDict[nodeKey]:
#         print(tuple[0])

class ThreadTest(threading.Thread):
    def __init__(self,updateGraphEvent, readGraph,threadQueue):
        threading.Thread.__init__(self)
        self._updateGraphEvent = updateGraphEvent
        self._readGraph = readGraph

        def run(self):
            self._updateGraphEvent.wait()
            threadQueue.put(self)
            time.sleep(100)
            self._readGraph.printEdges()

testGraph = {
    'edges' : '1'
}
readGraph.saveGraph(testGraph,'testGraph')



updateGraphEvent = threading.Event()
gf = graphFacade.GraphFacade(updateGraphEvent,readGraph)
gf.start()


threadTest = ThreadTest(updateGraphEvent,readGraph)






