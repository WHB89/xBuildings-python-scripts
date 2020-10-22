#Callback-Script: Jump to node and set flags
hou.pwd().node("editViewSwitch").setDisplayFlag(1); hou.pwd().node("__a_paintProps").setSelected(True); hou.pwd().node("editViewSwitch").parm("input").set(2); hou.pwd().node("merge11").setTemplateFlag(1)
#Editable nodes in type property for access
editViewSwitch __a_paintWalls/PaintWallsOutput0 __a_paintWalls __a_paintProps/PropOutput0 __a_paintProps __a_paintDoor/DoorOutput0 __a_paintDoor __a_paintHoles/PaintHolesOutput0 __a_paintHoles StairsStartPointOutput/OutputStairsStartPoint merge11
