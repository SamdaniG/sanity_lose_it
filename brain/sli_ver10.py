import json
import time
import sanity_funcs as sf
from functools import wraps
from pathlib import Path

PARENT_FILE=Path(__file__).resolve().parent.parent
VER_NAME=Path(__file__).stem.split("_")[-1]

def time_taken(func):
    """This is a python decorator to calculate the time taken to run every function, gives us a useful metric to keep track"""
    @wraps(func)
    def wrapper(*args):
        start = time.time()
        #print(f"Started the timer!")
        results = func(*args)
        end = time.time()
        logger.debug(f"\t\tTime taken to run the {func.__name__}: {end - start:.4f}s")
        return results

    return wrapper

#@time_taken
def creating_rotation_list():
    """This function gives us a list of all rotations possible when the cubes are stacked!"""
    arr = []
    rotation = [sf.m0, sf.u1, sf.u2, sf.u3, sf.l1, sf.l2, sf.l3]
    for func_a in rotation:
        for func_b in rotation:
            for func_c in rotation:
                for func_d in rotation:
                    if sf.multiplicity_check([func_a, func_b, func_c, func_d],
                                             3) == 0:  #this effectively removes all same values in the list ie a,a,a,a etc
                        arr.append([func_a, func_b, func_c, func_d])

    """This should be added to ensure that the combination 
    that enters also gets checked
    Have to sleep on this thought"""
    arr.append([sf.m0, sf.m0, sf.m0, sf.m0])
    return arr

#@time_taken
def creating_layer_list():
    """This creates the layer's shuffle list, basically ensures that layers of the blocks are also shuffled,
    like block A<B<C<D can also be stacked as D<C<A<B"""
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


@time_taken
def creating_the_block():
    """This function here creates all possible colour combinations possible,
    6 faces and 4 Colours to fill with
    Output is a list of lists, ie list of all possible combinations"""
    prime = [1, 2, 3, 4]
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
                            #if len(check)==4 and counter==2:
                            if len(check) == 4 and counter <= 3:
                                arr.append(yo)
                            i+=1

    logger.info(f"The total possible scenarios are {flag:,}, "
                f"but it comes down to this after duplicity check, {len(arr)}")
    return arr

@time_taken
def creation_of_compatible_blocks(master_list):
    """Well this creates compatible blocks,
    meaning that for a block A what all other blocks
    exist so that there are no repetitive colours
    Input: Master List (Master list of all possible combinations of cube)
    Output: Dictionary of all compatible blocks"""
    sets = {}
    for w, a in enumerate(master_list):
        for x, b in enumerate(master_list):
            if x <= w:
                continue
            if sf.check_diff(a, b):
            #if sf.check_diff(a,b,num=6,x=0,y=6):
                if w not in sets:
                    sets[w] = set()
                if x not in sets:
                    sets[x] = set()

                sets[w].add(x)
                sets[x].add(w)
    return sets

@time_taken
def final_cook(master_list,sets):
    """In this one we take the masterlist and
    check for the repetitions of each colour
    for all possible permutations
    input: master list, sets
    output: list of all possible solution stacks"""
    arr=[]
    flag0,flag1=0,0
    permflag={'w':0,'x':0,'y':0}
    print(f"No\t\tFlag0\t\tFlag1\t\tPermFlag\t\tLen")
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
        print(f"{w:0>8,d}\t{flag0:0>8,d}\t{flag1:0>8,d}\t{len(arr):0>9,d}\t{permflag}\t{len(arr)}",end="\r")

        #For debugging
        # if w > 5:
        #     break
    print("\n")
    return arr

@time_taken
def sort(final_solution,master_list):
    """This is where the final sort happens and we find out how many unique solutions we have for each stack
    flag=1 denotes that only 1 particular combination has no repetitive colours, ie our solution
    input: final_solution, list of all possible stacks
    output: Checks if it's the actual solution or not"""

    #Creating the rotation list
    rotation_list = creating_rotation_list()
    layer_list=creating_layer_list()
    sos_list=[]
    least_sos=[]
    sos1=4
    for cook in final_solution:
        w,x,y,z=cook
        a=master_list[w]
        b=master_list[x]
        c=master_list[y]
        d=master_list[z]
        sos = sf.final_check_v9([a, b, c, d], rotation_list)#, layer_list)
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

@time_taken
def write_sos_to_file(sos, least_sos, parent_dir):
    """This function writes the solutions to a file!"""
    file_loc = parent_dir / "output" / "ver10"
    file_name = file_loc / f'{time.strftime("%d%b%Y_%H%M%S")}_ver10.json'
    file_name1 = file_loc / f'{time.strftime("%d%b%Y_%H%M%S")}_ver10_least_sos.json'

    with open(file_name, "w") as file:
        json_string = json.dumps(sos, indent=4, separators=(",", ": "), ensure_ascii=False)
        json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]",
                                                                                                    "]").replace("    ",
                                                                                                                 "")
        file.write(json_string)
    with open(file_name1, "w") as file:
        json_string = json.dumps(least_sos, indent=4, separators=(",", ": "), ensure_ascii=False)
        json_string = json_string.replace("\n        [", "[").replace("\n            ", "").replace("\n        ]",
                                                                                                    "]").replace("    ",
                                                                                                                 "")
        file.write(json_string)

    logger.info(f"The file has finally finished running and the file names are {file_name.relative_to(parent_dir)}"
                f" and {file_name1.relative_to(parent_dir)}\a")

@time_taken
def write_master_list_to_file(final_solution, parent_dir):
    """This function writes the final solution list to a file!"""
    file_loc= parent_dir / "output" / "ver10"
    fname = file_loc / f'{time.strftime("%d%b%Y_%H%M%S")}_ver10_final_cook.json'
    with open(fname, "w") as f:
        for row in final_solution:
            f.write(f"{row}\n")
    rel_file=fname.relative_to(parent_dir)
    logger.info(f"The master list has been written to {rel_file}")

@time_taken
def main():
    logger.info("----------------Starting calcs----------------")

    #Master list contains all the possible permutations and combinations possible for 4 colours to be placed on 6 faces
    master_list = creating_the_block()

    #This creates a list of compatible blocks for a particular block X, so when X and another block from the compatible blocks
    # are placed on top of each other, there would be no repetitive colout
    sets = creation_of_compatible_blocks(master_list)

    #This is the final cook, where we find out how many solutions each combination of block has
    final_solution = final_cook(master_list,sets)

    #This writes the results to a file
    write_master_list_to_file(final_solution, PARENT_FILE)

    #This segregates the solutions so that we finally have the list of the combinations of the block that will give us a unique solution
    sos, least_sos = sort(final_solution,master_list)
    logger.info(f"Sorting is done!")

    #Writing those to a file!
    write_sos_to_file(sos, least_sos,PARENT_FILE)
    logger.info(f"The logs can be found at logs/{VER_NAME}_logs.log")

if __name__=="__main__":
    logger = sf.set_logger(PARENT_FILE, VER_NAME)
    main()
