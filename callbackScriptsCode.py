hou.pwd().node("paintWallIDs").parm('reset').pressButton() 

hou.pwd().node("paintWallIDs").setSelected(True)

hou.pwd().node("editViewSwitch").parm(“input”).set(2)

#editable in building gen
paintWallIDs paintWallIDs/paintWallIDs switchoverride pattern_vis


#Callback-Script:
hou.pwd().node("editViewSwitch").setDisplayFlag(1); hou.pwd().node("__a_paintProps").setSelected(True); hou.pwd().node("editViewSwitch").parm("input").set(2); hou.pwd().node("merge11").setTemplateFlag(1)


editable nodes
editViewSwitch __a_paintWalls/PaintWallsOutput0 __a_paintWalls __a_paintProps/PropOutput0 __a_paintProps __a_paintDoor/DoorOutput0 __a_paintDoor __a_paintHoles/PaintHolesOutput0 __a_paintHoles StairsStartPointOutput/OutputStairsStartPoint merge11
