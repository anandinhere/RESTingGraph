import graph

#Idea is to have graph global variable which gets updated every 'x' period of time with a exclusive lock.

def dfs(inputGraph, startNode):
    adjList = inputGraph.adjacencyNodeListsDict
    graphNodes = inputGraph.nodeDict

    nodeStack = []
    nodeStack.append(startNode)
    while len(nodeStack)>0:
        topNode = nodeStack.pop()
        if(topNode.isVisited):
            continue
        topNode.isVisited=True
        print(topNode.key)
        adjNodes = adjList[topNode.key]
        for tuple in adjNodes:
            nodeStack.append(graphNodes[tuple[0]])