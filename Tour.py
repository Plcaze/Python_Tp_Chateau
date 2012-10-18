
#boucle FOR 

Radius=1
i=0

for i in range (0,30):
    cmds.polyCylinder(n="TourBase",r=Radius+i,h=2,sx=60)
    


#TOUR
TourBaseH=20
TourMilieuH=TourBaseH*0.30
TourHautH=TourBaseH*0.15
TourRadius=5

cmds.polyCylinder(n='TourBase',r=TourRadius ,h=TourBaseH )  #CylindreBase de la tour
cmds.xform('TourBase',ws=True,piv=(0,(-(TourBaseH)/2),0))
cmds.move(0,(TourBaseH/2),0)

cmds.polyCylinder(n='TourMilieu',r=TourRadius*0.6 ,h=TourMilieuH) #CylindreMilieu de la tour
cmds.xform(ws=True,piv=(0,(-(TourMilieuH)/2),0))
cmds.move(0,TourBaseH+(TourMilieuH/2),0)

cmds.polyCylinder(n='TourHaut',r=TourRadius*0.4 ,h=TourHautH) #CylindreHaut de la tour
cmds.xform(ws=True,piv=(0,(-(TourHautH)/2),0))
cmds.move(0,TourBaseH+TourMilieuH+TourHautH/2,0)


import maya.cmds as cmds

cmds.polyCylinder(n='Tour2',r=3,h=6)
cmds.xform(ws=True, piv=(0,3,0))
cmds.move(0,-3,0)

for i in range(3):
    cmds.polyCylinder(n='Tour1',r=3.2+(.1*i),h=0.3,sa=30)
    cmds.move(0,0.3*i,0)
    
cmds.group('Tour*',n='GroupTour')
cmds.select('GroupTour')
cmds.xform(ws=True, piv=(0,0.75,0))
cmds.move(0,-0.75,0, 'GroupTour')

for i in range(20):
    cmds.polyCube(n='Rempart',w=2,h=1,d=1)
    cmds.xform(ws=True,piv=(0,-0.5,0.5))
    cmds.move(0,0.5,-.5)
    cmds.scale(.25,.25,.25)
    cmds.move(0,0,3.4, relative=True)
    cmds.xform(ws=True, rotatePivot=(0,0,0))
    cmds.rotate(0,18*i,0)
    
cmds.group('Rempart*',n='GroupRempart')
cmds.group('GroupTour','GroupRempart','Tour2',n='TourBase')

cmds.duplicate('TourBase',n='TourHaut')
cmds.move(0,3,0)
cmds.scale(.8,.8,.8)




#01:00

import maya.cmds as cmds

cmds.polyCylinder(n='Tour2',r=3,h=6)
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

cmds.select('Rempart*')
cmds.polyUnite(n='Trou')
    
cmds.polyPipe(n='Test',r=3.4,h=2,t=1,sa=40)
cmds.move(2.9,0,0)
cmds.polyBoolOp('Remp','Trou', op=2, n='Result')


cmds.group('Rempart*',n='GroupRempart')
cmds.group('GroupTour','GroupRempart','Tour2',n='TourBase')

cmds.duplicate('TourBase',n='TourHaut')
cmds.move(0,3,0)
cmds.scale(.8,.8,.8)
