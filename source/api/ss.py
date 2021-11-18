cl=3 
cr=0
ml=3
mr=0
boat=0;
print("CannibalLeft "+"MissionaryLeft "+"Boat "+"CannibalRight "+"MissionaryRight ")
print("Cannibals on the left are "+str(cl))
print("Missionary on the left are "+str(ml))
print("The boat position is "+str(boat))
print("Cannibals on the right are "+str(cr))
print("Missionary on the right are "+str(mr))
print("**********************************************")

if(cl==3 and ml==3 and boat==0):
    cl-=2
    cr+=2
    boat=1
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")
    # print("The boat position is "+str(boat),end=" ")

if(cl==1 and ml==3 and boat==1):
    cr-=1
    cl+=1
    boat=0
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==2 and ml==3 and boat==0):
    cl-=2
    cr+=2
    boat=1
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==0 and ml==3 and boat==1):
    cr-=1;
    cl+=1;
    boat=0;
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==1 and ml==3 and boat==0):
    ml-=2
    mr+=2
    boat=1
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

    
if(cl==1 and ml==1 and boat==1):
    mr-=1;
    ml+=1;
    cr-=1;
    cl+=1;
    boat=0;
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

    
if(cl==2 and ml==2 and boat==0):
    ml-=2
    mr+=2
    boat=1
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")
if(cl==2 and ml==0 and boat==1):
    cr-=1
    cl+=1
    boat=0
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==3 and ml==0 and boat==0):
    cl-=2;
    cr+=2;
    boat=1;
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==1 and ml==0 and boat==1):
    cr-=1
    cl+=1
    boat=0
    print("Cannibals on the left are "+str(cl),end=" ")
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")

if(cl==2 and ml==0 and boat==0):
    cl-=2;
    cr+=2;
    boat=1;
    print("Cannibals on the left are "+str(cl))
    print("Missionary on the left are "+str(ml))
    print("The boat position is "+str(boat))
    print("Cannibals on the right are "+str(cr))
    print("Missionary on the right are "+str(mr))
    print("**********************************************")
