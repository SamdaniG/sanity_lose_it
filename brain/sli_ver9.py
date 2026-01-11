import  logging.config
import json
import time
import sanity_funcs as sf
import os
from functools import cache,wraps
from tqdm import tqdm
from pathlib import Path

PARENT_FILE=Path(__file__).resolve().parent.parent
VER_NAME=Path(__file__).stem.split("_")[-1]
logger=sf.set_logger(PARENT_FILE, VER_NAME)

"""Adding the time decorator, later will movie it to sanity_funcs"""
def time_taken(func):
    @wraps(func)
    def wrapper(*args):
        start=time.time()
        #print(f"Started the timer!")
        results=func(*args)
        end=time.time()
        logger.debug(f"\t\tTime taken to run the {func.__name__}: {end-start:.4f}s")
        return results
    return wrapper

"""Initialising the parameters needed"""
prime=[1,2,3,4]

xyz=int(input("What should the multiplicity check number be: "))
logger.info("----------------Starting calcs----------------")
logger.info(f"The multiplicity is set to {xyz}.")

#creating the rotation list
rotation=[sf.m0,sf.u1,sf.u2,sf.u3,sf.l1,sf.l2,sf.l3]

@time_taken
def creating_rotation_list():
    arr=[]
    for func_a in rotation:
        for func_b in rotation:
            for func_c in rotation:
                for func_d in rotation:
                    if sf.multiplicity_check([func_a, func_b, func_c, func_d],3)==0:    #this effectively removes all same values in the list ie a,a,a,a etc
                        arr.append([func_a, func_b, func_c, func_d])

    return  arr

rotation_list=creating_rotation_list()

"""This should be added to ensure that the combination 
that enters also gets checked
Have to sleep on this thought"""
rotation_list.append([sf.m0,sf.m0,sf.m0,sf.m0])

"""Not sure if we need this"""
#creating the layer list
rots=[0,1,2,3]

@time_taken
def creating_layer_list():
    arr=[]
    rots = [0, 1, 2, 3]
    for u in rots:
        for v in rots:
            for x in rots:
                for y in rots:
                    counter=sf.multiplicity_check([u, v, x, y], 1)
                    if counter==0:
                        arr.append([u,v,x,y])
    return arr

layer_list=creating_layer_list()
"""If anything, this needn't be activated."""
#layer_list.remove([0,1,2,3])

@time_taken
def creating_the_block():
    i=0
    flag=0
    arr=[]
    for a in prime:
        for b in prime:
            for c in prime:
                for d in prime:
                    for e in prime:
                        for f in prime:
                            i+=1
                            yo = [a, b, c, d, e, f]

                            flag = sf.multiplicity_check_list(yo)
                            if flag == xyz:
                                arr.append(yo)
                            i += 1

    logger.info(f"The total possible scenarios are {i:,}, "
                f"but it comes down to this after duplicity check, {len(arr)}")
    return arr
master_list=creating_the_block()

@time_taken
def creation_of_compatible_blocks():
    comp=set()
    incomp=set()
    if_flag,elif_flag,else_flag,permlist_flag=0,0,0,0
    print(f"if_flag\t\t\telif_flag\t\tpermlist_flag\t\telse_flag")
    for w,a in enumerate(master_list):
        for x,b in enumerate(master_list):

            if if_flag%1000==0:
                print(f"{if_flag:<15,d}\t\t{elif_flag:<15,d}\t\t{permlist_flag:<15,d}\t\t{else_flag:<15,d}",end="\r")
                pass
            if x<=w:
                if_flag+=1
                continue
            ab_combined_permlist= sf.check_perms([a]) + sf.check_perms([b])
            if a in ab_combined_permlist or b in ab_combined_permlist:
                meh=(w,x)
                incomp.add(meh)
                permlist_flag+=1
            elif not sf.check_diff(a, b):
            #elif sf.check_diff(a,b,num=6,x=0,y=6)==False:
                meh = (w, x)
                incomp.add(meh)
                elif_flag+=1
            else:
                meh = sf.index_combined(w, x)
                #meh=str(f"{w:05}{x:05}")
                meh = (w, x)
                comp.add(meh)
                else_flag+=1

    print("\n")
    logger.info(f"{if_flag=:<15,d}{elif_flag=:<15,d}{permlist_flag=:<15,d}{else_flag=:<15,d}")
    return comp,incomp

compatible_blocks,incompatible_blocks=creation_of_compatible_blocks()
logger.info(f"The length of comp block: {len(compatible_blocks):,d} and incomp block: {len(incompatible_blocks):,d}.")

"""
#This is for if elif else and repeat and set check
@time_taken
def final_cook():
    #Creating the counters
    flag4=0
    flag0=0
    arr=[]
    arr_least=[]
    sos1 = 100

    for w,a in enumerate(master_list):
        #flag here?
        flag0+=1
        for x,b in enumerate(master_list):
            if x<=w:
                continue
            elif sf.index_combined(w, x) in compatible_blocks:
                for y,c in enumerate(master_list):
                    if y <= x:
                        continue
                    elif sf.index_combined(w, y) in compatible_blocks and sf.index_combined(x, y) in compatible_blocks:
                        for z,d in enumerate(master_list):
                            if z <= y:
                                continue
                            elif (sf.index_combined(w, z) in compatible_blocks and
                                  sf.index_combined(x, z) in compatible_blocks and
                                  sf.index_combined(y, z) in compatible_blocks):

                                flag4+=1
                                sos = sf.final_check([a, b, c, d], rotation_list)
                                # for json
                                dict1 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d, "Flags": sos,
                                         "Position": [w, x, y, z]}
                                arr.append(dict1)

                                if sos <= sos1:
                                    sos1 = sos
                                    dict2 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d,
                                             "Flags": sos, "Position": [w, x, y, z]}
                                    arr_least.append(dict2)

                                print(
                                    f"{flag0:0>10,d}\t\t{flag4:0>10,d}\t\t{w :05} {x :05} {y :05} {z :05} {sos :04} {flag0 / len(master_list) * 100:04.1f}%",
                                    end="\r")
                            else:
                                continue
                    else:
                        continue
            else:
                continue

    return arr,arr_least
"""

"""
@time_taken
#This has if if else repeat and sf diff check.
def final_cook():
    #Creating the counters
    flag4=0
    flag0=0
    flag1=0
    flag2=0
    flag3=0
    arr=[]
    arr_least=[]
    sos1 = 100
    print(f"Flag0\tFlag1\t\tFlag2\t\tFlag3\t\tFlag4\t\tPossible solutions")
    for w,a in enumerate(master_list):
        flag0 += 1
        for x,b in enumerate(master_list):
            if x<=w:
                continue
            if not sf.check_diff(a, b):
                flag1 += 1
                continue
            else:
                for y,c in enumerate(master_list):
                    if y<=x:
                        continue
                    if not sf.check_diff(a, b, c):
                        flag2 += 1
                        continue
                    else:
                        for z,d in enumerate(master_list):
                            if z<=y:
                                continue
                            # if sf.check_diff(a,b,c,d,num=6,x=0,y=6)==False:     #trying to find out a completely unique solution with different numbers
                            if not sf.check_diff(a, b, c, d):
                                flag3 += 1
                                continue
                            else:
                                flag4 += 1
                                sos = sf.final_check([a, b, c, d], rotation_list)
                                # for json
                                dict1 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d,
                                         "Flags": sos, "Position": [w, x, y, z]}
                                arr.append(dict1)


                                if sos <= sos1:
                                    sos1 = sos
                                    dict2 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d,
                                             "Flags": sos, "Position": [w, x, y, z]}
                                    arr_least.append(dict2)

                                print(
                                    f"{flag0:0>5,d}\t{flag1:0.1e}\t\t{flag2:0.1e}\t\t{flag3:0.1e}\t\t{flag4:0>6,d}\t\t"
                                    f"{w :05} {x :05} {y :05} {z :05} {sos :03} {flag0 / len(master_list) * 100:04.1f}%",
                                    end="\r")
    return arr,arr_least
"""

@time_taken
#This has if if else repeat and set check.
def final_cook():
    #Creating the counters
    flag4=0
    flag0=0
    flag1=0
    flag2=0
    flag3=0
    perm_flag=0

    arr=[]
    #arr_least=[]
    sos1 = 100
    print(f"Flag0\tFlag1\t\tFlag2\t\tFlag3\t\tFlag4\t\tPerm_flag\t\tPossible solutions")
    for w,a in enumerate(master_list):
        flag0 += 1
        perm_list=sf.check_perms([a])
        for x,b in enumerate(master_list):
            if x<=w:
                continue

            if b in perm_list:
                perm_flag+=1
                continue

            if not (w, x) in compatible_blocks:
                flag1 += 1
                continue
            else:
                perm_list += sf.check_perms([b])
                for y,c in enumerate(master_list):
                    if y<=x:
                        continue
                    if c in perm_list:
                        perm_flag += 1
                        continue
                    if not (w, y) in compatible_blocks:
                        flag2 += 1
                        continue
                    if not (x, y) in compatible_blocks:
                        flag2 += 1
                        continue
                    else:
                        perm_list+=sf.check_perms([c])
                        for z,d in enumerate(master_list):
                            if z<=y:
                                continue
                            # if sf.check_diff(a,b,c,d,num=6,x=0,y=6)==False:     #trying to find out a completely unique solution with different numbers
                            if not (w, z) in compatible_blocks:
                                flag3 += 1
                                continue
                            if not (x, z) in compatible_blocks:
                                flag3 += 1
                                continue
                            if not (y, z) in compatible_blocks:
                                flag3 += 1
                                continue
                            if d in perm_list:
                                perm_flag += 1
                                continue
                            else:
                                flag4 += 1
                                arr.append([a,b,c,d])
                                # sos = sf.final_check_v9([a, b, c, d], rotation_list)
                                # # for json
                                # dict1 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d,
                                #          "Flags": sos, "Position": [w, x, y, z]}
                                # arr.append(dict1)
                                #
                                #
                                # if sos <= sos1:
                                #     sos1 = sos
                                #     dict2 = {"Soln_rank": flag4, "List0": a, "List1": b, "List2": c, "List3": d,
                                #              "Flags": sos, "Position": [w, x, y, z]}
                                #     arr_least.append(dict2)

                                if flag4%1000==0:
                                    print(
                                    f"{flag0:0>5,d}\t{flag1:0.1e}\t\t{flag2:0.1e}\t\t{flag3:0.1e}\t\t{flag4:0>8,d}\t{perm_flag}\t\t"
                                    f"{w :05} {x :05} {y :05} {z :05} {sos1 :03} {flag0 / len(master_list) * 100:04.1f}%",
                                    end="\r")
                                    pass
    return arr


final_solution=final_cook()

print(f"{len(final_solution)=}")

tally = False
# while tally:
#     file_name="ver9.json"
#     file_name1="ver9_least_sos.json"
#
#     with open(file_name, "w") as file:
#         json_string = json.dumps(possible_sol, indent=4, separators=(",", ": "), ensure_ascii=False)
#         json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
#         file.write(json_string)
#
#     with open(file_name1, "w") as file:
#         json_string = json.dumps(possible_sol_least_sos, indent=4, separators=(",", ": "), ensure_ascii=False)
#         json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]", "]").replace("    ","")
#         file.write(json_string)
#
