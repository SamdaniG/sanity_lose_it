#from math import perm

import time
import sanity_funcs as sf
import os
import json
#import re

time_check=time.time()

prime=[1,2,3,4]
#prime=[1,2,3]
master_list=[]  
possible_solution=[]
element_check=[0,1,2,3,4,5]

###Extracting the last name of the file ie sanity_lose_it_xxx
ver_name = os.path.splitext(__file__)[0]
ver_name=ver_name.split('_')[-1]
name_of_file=input("What should be the name of the file: ")

"""#this doesn't matter anymore
with open(f'{ver_name}.csv', 'w') as file:
        file.truncate()

"""
#creating the rotation list
rotation=[sf.m0,sf.u1,sf.u2,sf.u3,sf.l1,sf.l2,sf.l3]
rotation_list=[]
for func_a in rotation:
    for func_b in rotation:
        for func_c in rotation:
            for func_d in rotation:
                if sf.multiplicity_check([func_a, func_b, func_c, func_d],3)==0:    #this effectively removes all same values in the list ie a,a,a,a etc
                    rotation_list.append([func_a, func_b, func_c, func_d])

#creating the layer list
rots=[0,1,2,3]
layer_list=[]
for u in rots:
    for v in rots:
        for x in rots:
            for y in rots:
                flag=sf.multiplicity_check([u,v,x,y],1)
                if flag==0:
                    layer_list.append([u,v,x,y])
layer_list.remove([0,1,2,3])

i=0
flag23=0

xyz=int(input("What should the multiplicity check number be: "))

for a in prime:
    for b in prime:
        for c in prime:
            for d in prime:
                for e in prime:
                    for f in prime:
                        yo=[a,b,c,d,e,f]
                        flag23+=1
                        #print(yo)
                        flag=sf.multiplicity_check(yo,xyz)
                        if flag==0:
                            master_list.append(yo)
                        i+=1

#print(i)
#print(len(master_list))
print(f"The total possible scenarios are {flag23:,}, but it comes down to this after multiplicity check")
print(f"Length of master list: {len(master_list)}")
#sf.write2file(master_list,ver_name)

#this removes the different orientations of the same block ie l1,l2,l3,u1,u2,u3
for yo in master_list:
    yolist=sf.check_perms([yo])
    for yol in yolist:
        if yol in master_list:
            master_list.remove(yol)
            #print(len(master_list))

print(f"Length of master list after removing the same blocks: {len(master_list)}")

"""#prints master_list
for a in master_list:
    print(a)

"""


block1=master_list
block2=master_list
block3=master_list
block4=master_list



"""
#separated the blocks by position in a[1]
 #this method separate the master list by a[1]
block1=[]
block2=[]
block3=[]
block4=[]

for a in master_list:
    if a[1]==1:
        block1.append(a)
        
    elif a[1]==2:
        block2.append(a)
        
    elif a[1]==3:
        block3.append(a)
        
    else:
        block4.append(a)
"""
print(f"Length of a single block: {len(block1)} {len(block2)} {len(block3)} {len(block4)} ")

flag1=0
flag2=0
flag3=0
flag4=0
flag0=0
remove_flag=0
sos1=100


start_time=time.time()

print(f"\nTime\tFlag0\tFlag1\t\tFlag2\t\tFlag3\t\tFlag4\t\tPossible solutions")

#var_list=[]         #this list is the variations of the 4 blocks, 0 1 2 3 , 3 2 1 0
var_dict={}         # #this dict is the variations of the 4 blocks, 0 1 2 3 , 3 2 1 0
var_list_fluctuations=[]

sos1=100

#final calcs
for a in block1:
    flag0+=1
    for b in block2:
        
        if block2.index(b)<=block1.index(a):
            continue
        
        if sf.check_diff(a,b)==False:
            flag1+=1
            continue
        else:
            for c in block3:
                
                if block3.index(c)<=block2.index(b):
                    continue
                
                if sf.check_diff(a,b,c) == False:
                    flag2+=1
                    continue
                else:
                    for d in block4:
                        w,x,y,z=master_list.index(a),master_list.index(b),master_list.index(c),master_list.index(d)
                        
                        if block4.index(d)<=block3.index(c):
                            continue
                        
                        
                        """                        
                        if [w,x,y,z] in var_list:
                            
                            var_list.remove([w,x,y,z])
                            remove_flag+=1
                            var_list_fluctuations.append(len(var_list))
                            continue
                        
                        """
                        """
                        if (w,x,y,z) in var_dict and var_dict[(w,x,y,z)]==1:
                            #print("Triggered")
                            continue
                        """
                        #if sf.check_diff(a,b,c,d,num=6,x=0,y=6)==False:     #trying to find out a completely unique solution with different numbers
                        if sf.check_diff(a,b,c,d)==False:
                            flag3+=1
                            #sf.var_check([w,x,y,z],var_list,layer_list)
                            continue
                        else:
                            flag4+=1          
                            sos=sf.final_check([a,b,c,d],rotation_list)
                            #for json                      
                            dict1={"Soln_rank": flag4,"List0":a, "List1":b,"List2":c, "List3":d,"Flags":sos,"Position":[w,x,y,z]}
                            possible_solution.append(dict1)
                            
                            """
                            #adding sos=2 in the possible_solution
                            if sos==2:
                                flag4+=1
                                dict1={"Soln_rank": flag4,"List0":a, "List1":b,"List2":c, "List3":d,"Flags":sos,"Position":[w,x,y,z]}
                                possible_solution.append(dict1)
                            """

                            #to find the one with the least sos values
                            #sos1=100
                            if sos<sos1:
                                sos1=sos

                            #sf.var_check([w,x,y,z],var_dict,layer_list)
                            
                            #possible_solution.append([a,b,c,d])
                            #sf.write2file([a,b,c,d],ver_name)
                            time_di=sf.time_diff(start_time)
                            print(f"{time_di:05.1f}\t{flag0:0>3,d}\t{flag1:0.1e}\t\t{flag2:0.1e}\t\t{flag3:0.1e}\t\t{flag4:0>6,d}\t\t{w :03} {x :03} {y :03} {z :03} {sos :02} {flag0/len(master_list)*100:04.1f}%", end="\r")

print("\n")
#print(len(possible_solution))
print(f"The least number of sos calls are: {sos1}")

#for json

with open(f"{ver_name}_{name_of_file}_{xyz}.json", "w") as file:
    json_string = json.dumps(possible_solution, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)

"""

import matplotlib.pyplot as plt

numbers = var_list_fluctuations
plt.plot(numbers, marker='o', linestyle='-', color='r')
plt.title('Line Plot (Indices Auto)')
plt.xlabel('Index (Auto)')
plt.ylabel('Value')
plt.show()

"""
#print(len(master_list))

end_time=sf.time_diff(time_check)
print(f"The file has finally finished running, it ran for {end_time:0.2f}\a")