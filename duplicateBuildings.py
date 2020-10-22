import hou

def export(outputName, path):
    fileNode = hou.node(path)
    fileNode.parm('file').set("$JOB/geo/"+outputName+".bgeo")
    fileNode.parm('filemode').set(2)
    fileNode.cook()
    fileNode.parm('filemode').set(1)
    
selection = hou.selectedNodes()
nodeForCloning = hou.node('/obj/BuildingA_1/')


for node in selection:
    print node.name()
    newNodeName = node.name()
    newBuildingNode = hou.copyNodesTo( [nodeForCloning], hou.node("/obj") )
    newBuildingNode[0].setName(newNodeName)
    
    buildingGenNode = hou.node('/obj/'+str(newNodeName)+'/building/buildingWallsGen/')
    buildingGenNode.parm("objpath6").set(str(node.path()))
    export(newNodeName + "CacheMainOutput",'/obj/'+str(newNodeName)+'/building/CacheMainOutput/')
    export(newNodeName + "CacheAddGeoOutput",'/obj/'+str(newNodeName)+'/building/CacheAddGeoOutput/')
    export(newNodeName + "CacheInteriorGeoOutput",'/obj/'+str(newNodeName)+'/building/CacheInteriorGeoOutput1/')
