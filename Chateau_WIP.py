import maya.cmds as cmds

cmds.polyCylinder(n='TourBase',r=3,h=6)
cmds.xform(ws=True, piv=(0,3,0))
cmds.move(0,-3,0)

for i in range(2):
    cmds.polyCylinder(n='Tour1',r=3.2+(.1*i),h=0.3,sa=30)
    cmds.move(0,0.3*i,0)
    
cmds.group('Tour*',n='GroupTour')
cmds.select('GroupTour')
cmds.xform(ws=True, piv=(0,0.75,0))
cmds.move(0,-0.75,0, 'GroupTour')

cmds.polyPipe(n='Remp',r=3.4,h=2.5,t=0.5,sa=40)

for i in range(12):
    cmds.polyCube(n='Rempart',w=0.5,h=0.5,d=1)
    cmds.xform(ws=True,piv=(0,-.25,0))
    cmds.move(0,.25,0)
    cmds.move(0,.2,3.2, relative=True)
    cmds.xform(ws=True, rotatePivot=(0,0,0))
    cmds.rotate(0,30*i,0)


for i in range(12):
    cmds.polyCube(n='Fente',w=1,h=.5,d=.1)
    cmds.move(3.2,0,0, relative=True)
    cmds.xform(ws=True, rotatePivot=(0,0,0))
    cmds.rotate(0,30*i,0)



cmds.group('Fente*', n='GroupFentes')
cmds.group('Remp*',n='GroupRempart')

cmds.rotate(0,15,0,)

cmds.polyUnite('Fente*','Rempart*',n='TrouResult')
cmds.polyBoolOp('Remp','TrouResult', op=2, n='RempartResult')
cmds.move(0,0.2,0)

cmds.group('GroupTour','GroupFentes','GroupRempart','RempartResult','TrouResult', n='Tour')

cmds.duplicate('Tour',n='TourHaut')
cmds.move(0,3,0)
cmds.scale(.8,.8,.8)
