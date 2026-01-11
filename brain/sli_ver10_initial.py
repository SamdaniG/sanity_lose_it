import logging.config
import json
import time
import brain.sanity_funcs as sf
import os
from functools import cache, wraps
from tqdm import tqdm

logger = sf.set_logger()

"""Adding the time decorator, later will move it to sanity_funcs"""


def time_taken(func):
    @wraps(func)
    def wrapper(*args):
        start = time.time()
        #print(f"Started the timer!")
        results = func(*args)
        end = time.time()
        logger.debug(f"\t\tTime taken to run the {func.__name__}: {end - start:.4f}s")
        return results

    return wrapper


"""Initialising the parameters needed"""
prime = [1, 2, 3, 4]

#xyz = int(input("What should the multiplicity check number be: "))
logger.info("----------------Starting calcs----------------")
#logger.info(f"The multiplicity is set to {xyz}.")

#creating the rotation list
rotation = [sf.m0, sf.u1, sf.u2, sf.u3, sf.l1, sf.l2, sf.l3]


@time_taken
def creating_rotation_list():
    arr = []
    for func_a in rotation:
        for func_b in rotation:
            for func_c in rotation:
                for func_d in rotation:
                    if sf.multiplicity_check([func_a, func_b, func_c, func_d],
                                             3) == 0:  #this effectively removes all same values in the list ie a,a,a,a etc
                        arr.append([func_a, func_b, func_c, func_d])

    return arr


rotation_list = creating_rotation_list()

"""This should be added to ensure that the combination 
that enters also gets checked
Have to sleep on this thought"""
rotation_list.append([sf.m0, sf.m0, sf.m0, sf.m0])

"""Not sure if we need this"""
#creating the layer list
rots = [0, 1, 2, 3]


@time_taken
def creating_layer_list():
    arr = []
    rots = [0, 1, 2, 3]
    for u in rots:
        for v in rots:
            for x in rots:
                for y in rots:
                    counter = sf.multiplicity_check([u, v, x, y], 1)
                    if counter == 0:
                        arr.append([u, v, x, y])
    return arr


layer_list = creating_layer_list()
"""If anything, this needn't be activated."""


#layer_list.remove([0,1,2,3])

@time_taken
def creating_the_block():
    i = 0
    flag = 0
    arr = []
    for a in prime:
        for b in prime:
            for c in prime:
                for d in prime:
                    for e in prime:
                        for f in prime:
                            yo = [a, b, c, d, e, f]
                            check={a,b,c,d,e,f}
                            flag += 1
                            counter = sf.multiplicity_check_list(yo)

                            """Keeping this check at xyz, keeps only the same number of repetitions, 
                            but for actual solution we might have to keep it <="""
                            """Bruh, I don't need xyz, i just need to ensure that 1,2,3,4 must occur atleast once..."""
                            #if counter==xyz:
                            #print(xyz)
                            if len(check)==4 and counter==2:
                                arr.append(yo)
                            i+=1

    logger.info(f"The total possible scenarios are {flag:,}, "
                f"but it comes down to this after duplicity check, {len(arr)}")
    return arr


master_list = creating_the_block()


@time_taken
def creation_of_compatible_blocks():
    sets = {}
    for w, a in enumerate(master_list):
        for x, b in enumerate(master_list):
            if x <= w:
                continue
            #if sf.check_diff(a, b):
            if sf.check_diff(a,b,num=6,x=0,y=6):
                if w not in sets:
                    sets[w] = set()
                if x not in sets:
                    sets[x] = set()

                sets[w].add(x)
                sets[x].add(w)
    return sets


sets = creation_of_compatible_blocks()

#print(sets)


@time_taken
def final_cook():
    arr=[]
    flag0,flag1=0,0
    permflag={'w':0,'x':0,'y':0}
    print(f"No\t\t\tFlag0\t\t\tFlag1\t\t\tPermFlag")
    for w,a in enumerate(master_list):
        perm_list_w=sf.check_perms([a])
        for x,b in enumerate(master_list):

            if x <= w:
                continue
            if b in perm_list_w:
                permflag['w']+=1
                continue
            if x not in sets[w]:
                continue
            if w not in sets[x]:
                continue

            ##Finding y
            perm_list_x=perm_list_w+sf.check_perms([b])
            y_all = sets[w] & sets[x]

            for y in y_all:
                c=master_list[y]
                flag0+=1
                if y <= x:
                    continue
                if c in perm_list_x:
                    permflag['x'] += 1
                    continue

                if w in sets[y] and x in sets[y]:
                    flag1+=1
                    z_all = sets[w] & sets[x] & sets[y]
                    perm_list_y=perm_list_x+sf.check_perms([master_list[y]])
                    # if len(z_all) > 1:
                    #     flag = True

                    for z in z_all:
                        d=master_list[z]
                        if z <= y:
                            continue
                        if d in perm_list_y:
                            permflag['y'] += 1
                            continue
                        #c=master_list[y]
                        #d=master_list[z]
                        #arr.append([a,b,c,d])
                        arr.append([w,x,y,z])
                else:
                    continue
        print(f"{w:0>8,d}\t\t{flag0:0>8,d}\t\t{flag1:0>8,d}\t\t{len(arr):0>9,d}\t\t{permflag}",end="\r")

        #For debugging
        # if w > 20:
        #     break
    print("\n")
    return arr


final_solution = final_cook()

fname=f"final_cook_{time.strftime("%d%b%Y_%H%M%S")}.txt"
with open(fname, "w") as f:
    for row in final_solution:
        f.write(f"{row}\n")


@time_taken
def sort():
    sos_list=[]
    least_sos=[]
    sos1=3
    for cook in final_solution:
        w,x,y,z=cook
        a=master_list[w]
        b=master_list[x]
        c=master_list[y]
        d=master_list[z]
        sos = sf.final_check_v9([a, b, c, d], rotation_list)
        # for json
        dict1 = {"List0": a, "List1": b, "List2": c, "List3": d,
                 "Flags": sos, "Position": [w, x, y, z]}
        sos_list.append(dict1)


        if sos <= sos1:
            sos1 = sos
            dict2 = {"List0": a, "List1": b, "List2": c, "List3": d,
                     "Flags": sos, "Position": [w, x, y, z]}
            least_sos.append(dict2)

        print(f"{w:04} {x:04} {y:04} {z:04} {sos}  {sos1}  {len(least_sos)= }" ,end="\r")

    least_sos = [a for a in least_sos if a["Flags"] <= sos1]
    print("\n")
    return  sos_list,least_sos


sos,least_sos=sort()
logger.info(f"Sorting is done!")



file_name=f'ver10_{time.strftime("%d%b%Y_%H%M%S")}.json'
file_name1=f'ver10_least_sos_{time.strftime("%d%b%Y_%H%M%S")}.json'

with open(file_name, "w") as file:
    json_string = json.dumps(sos, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)

with open(file_name1, "w") as file:
    json_string = json.dumps(least_sos, indent=4, separators=(",", ": "), ensure_ascii=False)
    json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
    file.write(json_string)

logger.info(f"\n\nThe file has finally finished running and the file names are {file_name} and {file_name1}\a")
tally = False

