from shapely.geometry import Polygon
from itertools import combinations
import random
#fixed joint locations are (0,0) and (1,0)
joint_locations=[[-1,-1],[-1,-0.75],[-1,-0.5],[-1,-0.25],[-1,0],[-1,0.25],[-1,0.5],[-1,0.75],[-1,1],[-0.75,-1],[-0.75,-0.75],[-0.75,-0.5],[-0.75,-0.25],[-0.75,0],[-0.75,0.25],[-0.75,0.5],[-0.75,0.75],[-0.75,1],[-0.5,-1],[-0.5,-0.75],[-0.5,-0.5],[-0.5,-0.25],[-0.5,0],[-0.5,0.25],[-0.5,0.5],[-0.5,0.75],[-0.5,1],[-0.25,-1],[-0.25,-0.75],[-0.25,-0.5],[-0.25,-0.25],[-0.25,0],[-0.25,0.25],[-0.25,0.5],[-0.25,0.75],[-0.25,1],[0,-1],[0,-0.75],[0,-0.5],[0,-0.25],[0,0.25],[0,0.5],[0,0.75],[0,1],[1,-1],[1,-0.75],[1,-0.5],[1,-0.25],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,-1],[0.75,-0.75],[0.75,-0.5],[0.75,-0.25],[0.75,0],[0.75,0.25],[0.75,0.5],[0.75,0.75],[0.75,1],[0.5,-1],[0.5,-0.75],[0.5,-0.5],[0.5,-0.25],[0.5,0],[0.5,0.25],[0.5,0.5],[0.5,0.75],[0.5,1],[0.25,-1],[0.25,-0.75],[0.25,-0.5],[0.25,-0.25],[0.25,0],[0.25,0.25],[0.25,0.5],[0.25,0.75],[0.25,1]]
#random.shuffle(joint_locations)
list_combinations=list()
list_combinations=list(combinations(joint_locations,3))
totalcombinations=len(list_combinations)
f=open('Dataset.txt','w')
#placeholders
joint1=[0,0]
joint2=[0,0]
joint3=[0,0]
joint4=[0,0]
joint5=[0,0]
joint6=[0,0]
joint7=[0,0]
count=0
for i in range(totalcombinations):
  #if(i%10000==0):
   # print(i)
  joint1=[0,0]
  joint2=list_combinations[i][0]
  joint3=[1,0]
  joint4=list_combinations[i][1]
  joint5=list_combinations[i][2]
  #check if any set of the three joints are coillinear
  notcoillinear=True
  jointlist=[joint1,joint2,joint3,joint4,joint5]
  checkcoillinearity=list()
  checkcoillinearity=list(combinations(jointlist,3))
  for k in range(10):
    point1=checkcoillinearity[k][0]
    point2=checkcoillinearity[k][1]
    point3=checkcoillinearity[k][2]
    if(point1[0]==point2[0] and point2[0]==point3[0]):
      notcoillinear=False
      break
    elif(point1[0]!=point2[0] and point2[0]!=point3[0]):
      slopefrompoints1to2=(point1[1]-point2[1])/(point1[0]-point2[0])
      slopefrompoints2to3=(point2[1]-point3[1])/(point2[0]-point3[0])
      if(slopefrompoints1to2==slopefrompoints2to3):
        notcoillinear=False
        break
  if notcoillinear==False:
    count=count+1
  if notcoillinear:
    x=random.uniform(0,1)
    if(x%0.25==0):
      if(x==1):
        x=x-random.uniform(0,0.125)
      else:
        x=x+random.uniform(0,0.125)
    points=[joint1,joint2,joint3,joint4,joint5]
    pentagon=Polygon(points)
    sides = pentagon.exterior.coords
    list_sides=list(sides)
    segment1start=random.randint(0,4)
    segment2start=segment1start
    while(segment2start==segment1start):
      segment2start=random.randint(0,4)
    line1start=list_sides[segment1start]
    line1end=list_sides[segment1start+1]
    line2start=list_sides[segment2start]
    line2end=list_sides[segment2start+1]
    if(line1end[0]!=line1start[0]):
      slope1=(line1end[1]-line1start[1])/(line1end[0]-line1start[0])
      intercept1=line1start[1]-line1start[0]*slope1
      plugx=random.uniform(line1start[0]+0.0001,line1end[0]-0.0001)
      plugy=slope1*plugx+intercept1
      joint6=[plugx,plugy]
    else:
      plugx=line1end[0]
      plugy=random.uniform(line1start[1]+0.0001,line1end[1]-0.0001)
      joint6=[plugx,plugy]
    if(line2end[0]!=line2start[0]):
      slope2=(line2end[1]-line2start[1])/(line2end[0]-line2start[0])
      intercept2=line2start[1]-line2start[0]*slope2
      plugx=random.uniform(line2start[0]+0.0001,line2end[0]-0.0001)
      plugy=slope2*plugx+intercept2
      joint7=[plugx,plugy]
    else:
      plugx=line2end[0]
      plugy=random.uniform(line2start[1]+0.0001,line2end[1]-0.0001)
      joint7=[plugx,plugy]
    print("("+str(joint1[0])+","+str(joint1[1])+"),"+" ("+str(joint2[0])+","+str(joint2[1])+"),"+"("+str(joint3[0])+","+str(joint3[1])+"),"+"("+str(joint4[0])+","+str(joint4[1])+"),"+"("+str(joint5[0])+","+str(joint5[1])+"),"+"("+str(joint6[0])+","+str(joint6[1])+"),"+"("+str(joint7[0])+","+str(joint7[1])+")\n"     )
    f.write("("+str(joint1[0])+","+str(joint1[1])+"),"+" ("+str(joint2[0])+","+str(joint2[1])+"),"+"("+str(joint3[0])+","+str(joint3[1])+"),"+"("+str(joint4[0])+","+str(joint4[1])+"),"+"("+str(joint5[0])+","+str(joint5[1])+"),"+"("+str(joint6[0])+","+str(joint6[1])+"),"+"("+str(joint7[0])+","+str(joint7[1])+")\n"   )
print("This was the number of invalid cases")
print(count)
    
    
