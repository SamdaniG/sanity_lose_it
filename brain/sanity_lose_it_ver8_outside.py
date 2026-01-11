#from math import perm

import time
import brain.sanity_funcs as sf
import os
import json


time_check=time.time()

prime=[1,2,3,4]

master_list=[]  
possible_solution=[]
element_check=[0,1,2,3,4,5]
possible_solution_least_sos=[]

###Extracting the last name of the file ie sanity_lose_it_xxx
ver_name = os.path.splitext(__file__)[0]
ver_name=ver_name.split('_')[-1]
name_of_file=input("What should be the name of the file: ")
strangle_search=input("Do you want to strangle the search? y or n: ")


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
                        flag=sf.multiplicity_check_list(yo)
                        if flag==xyz:
                            master_list.append(yo)
                        i+=1

print(f"The total possible scenarios are {flag23:,}, but it comes down to this after multiplicity check, {len(master_list)}")
#print(f"Length of master list: {len(master_list)}")


#this removes the different orientations of the same block ie l1,l2,l3,u1,u2,u3 from the master_list
for yo in master_list:
    yolist=sf.check_perms([yo])
    for yol in yolist:
        if yol in master_list:
            master_list.remove(yol)
            #print(len(master_list))

print(f"Length of master list after removing similar blocks: {len(master_list)}")


block1=master_list
block2=master_list
block3=master_list
block4=master_list

#print(f"Length of a single block: {len(block1)} {len(block2)} {len(block3)} {len(block4)} ")

#Trying something new
compatible_blocks=[]        #set()
incompatible_blocks=[]      #set()
sets={}
start_time1=time.time()
for a in block1:
    for b in block2:
        w,x=master_list.index(a),master_list.index(b) #,master_list.index(c),master_list.index(d)
        if block2.index(b)<=block1.index(a):
            continue
        elif strangle_search=='y' and sf.check_diff(a,b,num=6,x=0,y=6)==False:
            #meh=str(f"{w:03}{x:03}")
            meh={w,x}
            incompatible_blocks.append(meh)
            continue      

        elif strangle_search=='n' and sf.check_diff(a,b)==False:
        #elif sf.check_diff(a,b,num=6,x=0,y=6)==False:
            #meh=str(f"{w:03}{x:03}")
            meh={w,x}
            incompatible_blocks.append(meh)
            continue        
        else:
            #meh=str(f"{w:03}{x:03}")
            meh={w,x}
            #f"set_w"+={x}
            #set(f"set_w").add(x)
            #set(f"set_x").add(w)
            if w not in sets:
                sets[w]=set()
            if x not in sets:
                sets[x]=set()
            
            sets[w].add(x)
            sets[x].add(w)
            compatible_blocks.append(meh)

time_di=sf.time_diff(start_time1)
print(f"It took {time_di:02.2f} seconds to generate the compatible and incompatible blocks!\nThe length of them being {len(compatible_blocks)} and {len(incompatible_blocks)} respectively.")


start_time=time.time()

print(f"\nTime\t\tFlag0\t\tPossible solutions")


sos1=100
flag4=0

for y in range(len(block1)):
    for z in range(len(block1)):
        if z<=y:
            continue

        if z not in sets[y]:
            continue
        if y not in sets[z]:
            continue

        ##Finding x
        x=sets[y] & sets[z]

        for x1 in x:
            #print(x1,y,z)
            #print(x1&y&z)
            #w_check={x1&y&z}
            if x1<=z:
                continue
            for w in range(len(block1)):
                if w<=x1:
                    continue
                if sets[w] & {x1,y,z} == {x1,y,z}:
                    #possible_solution.append([w,x1,y,z])
                    a=block1[x1]
                    b=block1[y]
                    c=block1[z]
                    d=block1[w]

                    flag4+=1          
                    sos=sf.final_check([a,b,c,d],rotation_list)
                    #for json                      
                    dict1={"Soln_rank": flag4,"List0":a, "List1":b,"List2":c, "List3":d,"Flags":sos,"Position":[y,z,x1,w]}
                    possible_solution.append(dict1)
        

                    if sos<=sos1:
                        sos1=sos
                        dict2={"Soln_rank": flag4,"List0":a, "List1":b,"List2":c, "List3":d,"Flags":sos,"Position":[y,z,x1,w]}
                        possible_solution_least_sos.append(dict2)

                    time_di=sf.time_diff(start_time)
                    print(f"{time_di:06.2f}\t\t{flag4:06,d}\t\t{y :03} {z :03} {x1 :03} {w:03} {sos :02}", end="\r")
                        

time_di=sf.time_diff(start_time)
print(f"\nThe total time taken for the final calc is {time_di}.")
print("\n")
print(f"The least number of sos calls are: {sos1}")

print(f"The number of solutions are: {len(possible_solution)}\nThe number of least sos solutions are: {len(possible_solution_least_sos)}")

possible_solution_least_sos=[a for a in possible_solution_least_sos if a["Flags"] <= sos1]
'''
for a in possible_solution_least_sos:   
    for u in a:
        print(f"{u}:{a[u]}")
    print("\n")

'''
#for json

if strangle_search=="y":
    file_name=f"{ver_name}_{name_of_file}_strangled_{xyz}.json"
    file_name1=f"{ver_name}_{name_of_file}_strangled_{xyz}_least_flags.json"
else:
    file_name=f"{ver_name}_{name_of_file}_{xyz}.json"
    file_name1=f"{ver_name}_{name_of_file}_{xyz}_least_flags.json"

with open(file_name, "w") as file:
    json_string = json.dumps(possible_solution, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)

with open(file_name1, "w") as file:
    json_string = json.dumps(possible_solution_least_sos, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)



end_time=sf.time_diff(time_check)
print(f"\n\nThe file has finally finished running, it ran for {end_time:0.2f} and the file names are {file_name} and {file_name1}\a")
