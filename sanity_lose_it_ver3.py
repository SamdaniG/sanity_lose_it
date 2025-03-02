#from math import perm
import time
import sanity_funcs as sf
import os
import json

prime=[1,2,3,4]
master_list=[]  
possible_solution=[]
element_check=[0,1,2,3,4,5]

###Extracting the last name of the file ie sanity_lose_it_xxx
ver_name = os.path.splitext(__file__)[0]
ver_name=ver_name.split('_')[-1]


with open(f'{ver_name}.csv', 'w') as file:
        file.truncate()

#creating the rotation list
rotation=[sf.m0,sf.u1,sf.u2,sf.u3,sf.l1,sf.l2,sf.l3]
rotation_list=[]
for func_a in rotation:
    for func_b in rotation:
        for func_c in rotation:
            for func_d in rotation:
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
3
xyz=input("What should the multiplicity check number be: ")

for a in prime:
    for b in prime:
        for c in prime:
            for d in prime:
                for e in prime:
                    for f in prime:
                        yo=[a,b,c,d,e,f]
                        flag23+=1
                        #print(yo)
                        flag=sf.multiplicity_check(yo,int(xyz))
                        if flag==0:
                            master_list.append(yo)
                        i+=1

#print(i)
#print(len(master_list))
print(f"The total possible scenarios are {flag23:,}, but it comes down to this after multiplicity check")
print(f"Length of master list: {len(master_list)}")
#sf.write2file(master_list,ver_name)

for yo in master_list:
    yolist=sf.check_perms([yo])
    for yol in yolist:
        if yol in master_list:
            master_list.remove(yol)
            #print(len(master_list))

print(f"Length of master list after removing the same blocks: {len(master_list)}")


#for m in master_list:
    #print(m)

#print(master_list)
"""#prints master_list
for a in master_list:
    print(a)

"""
block1=master_list
block2=master_list
block3=master_list
block4=master_list

""" #this method separate the master list by a[1]
block1=[]
block2=[]
block3=[]
block4=[]

#separated the blocks by position in a[1]
for a in master_list:
    if a[1]==1:
        block1.append(a)
        
    elif a[1]==2:
        block2.append(a)
        
    elif a[1]==3:
        block3.append(a)
        
    else:
        block4.append(a)

print(f"Length of a single block: {len(block1)} {len(block2)} {len(block3)} {len(block4)} ")

sf.write2file([block1,block2,block3,block4],ver_name)

"""
flag1=0
flag2=0
flag3=0
flag4=0
flag0=0

start_time=time.time()
#final calcs
#print(f"The check value tells us how many of them scenarios had flag=0, and check1 tells us how many of them had flags more than 1")
#print(f"\nTime\tFlag0\tFlag1\t\tFlag2\t\tFlag3\t\tFlag4\t\tCheck\tCheck1\tPossible solutions")
print(f"\nTime\tFlag0\tFlag1\t\tFlag2\t\tFlag3\t\tFlag4\t\tPossible solutions")


"""
for a in block1:
    for b in block2:
        if sf.check_diff(a,b):
            for c in block3:
                if sf.check_diff(a,b,c):
                    for d in block4:
                        if sf.check_diff(a,b,c,d):
                            flag4+=1
                            if sf.final_check([a,b,c,d],rotation_list):
                                possible_solution.append([a,b,c,d])
                                sf.write2file([a,b,c,d],ver_name)
                                time_di=sf.time_diff(start_time)
                                print(f"{time_di:0.2f}\t{flag1:0.2e}\t{flag2:0.2e}\t{flag3:0.2e}\t{flag4:0.2e}\t{len(possible_solution):,}", end="\r")
                        else:
                            flag3+=1
                            continue
                else:
                    flag2+=1
                    continue
        else:
            flag1+=1
            continue
"""        

variation_list=[]

#final calcs
for a in block1:
    flag0+=1
    for b in block2:
        if sf.check_diff(a,b)==False:
            flag1+=1
            continue
        else:
            for c in block3:
                    if sf.check_diff(a,b,c) == False:
                        flag2+=1
                        continue
                    else:
                        for d in block4:
                            """ 
                            variation_list+=sf.var_check([a,b,c,d],variation_list,layer_list)
                            if [a,b,c,d] in variation_list:
                                continue
                            """
                            """         
                                    a_i=master_list.index(a)
                                    b_i=master_list.index(b)
                                    c_i=master_list.index(c)
                                    d_i=master_list.index(d)

                                    variation_list+=sf.var_check([a_i,b_i,c_i,d_i],variation_list,rotation_list)
                            """
                            if sf.check_diff(a,b,c,d)==False:
                                flag3+=1
                                continue
                            else:
                                flag4+=1
                                #mayhaps,check,check1=sf.final_check([a,b,c,d],rotation_list)
                                #if sf.final_check([a,b,c,d],rotation_list):                                       
                                
                                #possible_solution.append([a,b,c,d])
                                
                                #creating a dict and adding
                                w,x,y,z=master_list.index(a),master_list.index(b),master_list.index(c),master_list.index(d)
                                dict1={"Soln_rank": flag4,"List0":a, "List1":b,"List2":c, "List3":d,"Position":[w,x,y,z],"SOS":0}
                                possible_solution.append(dict1)

                                #sf.write2file([a,b,c,d],ver_name)
                            time_di=sf.time_diff(start_time)
                            print(f"{time_di:0.1f}\t{flag0:,}\t{flag1:0.1e}\t\t{flag2:0.1e}\t\t{flag3:0.1e}\t\t{flag4:,}\t\t{len(possible_solution):,}", end="\r")
                            #print(f"{time_di:0.1f}\t{flag0:,}\t{flag1:0.1e}\t\t{flag2:0.1e}\t\t{flag3:0.1e}\t\t{flag4:0.1e}\t\t{check:,}\t{check1:,}\t{len(possible_solution):,}", end="\r")

print("\n")
print(len(possible_solution))
#sf.write2file(possible_solution,ver_name)

#for json

with open(f"{ver_name}.json", "w") as file:
    json_string = json.dumps(possible_solution, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)



"""
for poss in possible_solution:
    print(poss)
"""
"""
for yo in possible_solution:
    yo1=sf.rotations(yo,layer_list)
    for yo2 in yo1:
        possible_solution.remove(yo2) 
        flag=sf.final_check(yo2,rotation_list)
        yo2.append([flag])
        sf.write2file(yo2,ver_name)     

          """
"""
        if yo in master_list:
            master_list.remove(yol)
            #print(len(master_list))
"""

print(len(master_list))
print(f"The file has finally finished running\a")