
from graph import graph,edge,node

g = graph.Graph()
#
# g.addEdge(0,1,10)
# g.addEdge(0,2,10)
# g.printEdges()
# print(g.adjacencyNodeListsDict)
# for nodeKey in  g.adjacencyNodeListsDict:
#     for tuple in g.adjacencyNodeListsDict[nodeKey]:
#         print(tuple[0])


testGraph = {
    'edges' : '1'
}
g.saveGraph(testGraph,'testGraph')