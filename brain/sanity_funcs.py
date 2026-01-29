import time, csv,json
import  logging.config
#import numpy as np

def set_logger(parent_dir,ver_name):
    """This sets up the logging module!"""

    log_dir = parent_dir / "logs" / ver_name
    log_dir.mkdir(parents=True, exist_ok=True)

    config_file = parent_dir / "logs" / "log_config.json"
    log_file= log_dir /f"{ver_name}_logs.log"


    with open(config_file, "r") as f:
        logging_config = json.load(f)

    logging_config["handlers"]["file"]["filename"]=log_file
    logging.config.dictConfig(config=logging_config)
    logger = logging.getLogger("test")
    return logger

def index_combined(a:int,b:int):
    #return str(f"{a:03}{b:03}")
    return str(f"{a:05}{b:05}")

def multiplicity_check(a:list,num:int =2):#a=[1,1,2,2,3,3]
    ''' This function checks how many times a number is repeated in a list, input-->list, accepted repeatance number'''
    flag=0  
    for x in a:
        if a.count(x)>num:
            flag+=1
    return flag

def multiplicity_check_list(a:list):#a=[1,1,2,2,3,3]
    ''' This function checks how many times a number is repeated in a list, input-->list and returns the max repeated element in the list,
    For example y=[a,a,a,b,c,d], this func returns 3'''
    flag=0  
    set_a=set(a)
    flag_a=set()
    for x in set_a:
        flag_a.add(a.count(x))

    return max(flag_a)

def check_diff(*args: list,num=4, x=1, y=5):
    '''This function takes in the lists and we check the uniqeness and returns true if all of them are unique,
    if needed it can be refined to check
    for all faces of the cube be setting x=0, y=6'''
    flag=0
    for i in range(x, y):
        sample_set = {arg[i] for arg in args}
        if len(sample_set) != len(args):
            break
        flag += 1
    return flag==num

def rotations(a,layer_list):
    lay_list=[]  # [3, 2, 1, 0]
    for layer in layer_list:
        app=[a[layer[0]],a[layer[1]],a[layer[2]],a[layer[3]]]
        lay_list.append(app)
    return lay_list

def var_check(a,var_dict,layer_list):
    for layer in layer_list:
        app=[a[layer[0]],a[layer[1]],a[layer[2]],a[layer[3]]]
        #ythough=[comb[0](a), comb[1](b), comb[2](c), comb[3](d)]
        var_dict[tuple(app)]=1
    #return var_dict

def final_check(yo,rotation_list):
    a,b,c,d=yo
    flag=0
    #check=0
    #check1=0
    i=0
    for comb in rotation_list:
        #flag += check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=6)
        #i+=1
        finalee=check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d))
        if finalee==True:
            flag+=1
        """
        if flag>1:
            #check1+=1
            break
        """
    #return flag==1
    return flag

def master_check(cook, rotation_list, master_list, compatible_blocks):
    # cook=[0,23,4343,53434]
    a,b,c,d = cook
    # a = master_list[w]
    # b = master_list[x]
    # c = master_list[y]
    # d = master_list[z]

    flag = 0
    index_map = {tuple(v): i for i, v in enumerate(master_list)}
    for comb in rotation_list:
        a1, b1, c1, d1 = comb[0](a), comb[1](b), comb[2](c), comb[3](d)
        w1 = index_map[tuple(a1)]
        x1 = index_map[tuple(b1)]
        y1 = index_map[tuple(c1)]
        z1 = index_map[tuple(d1)]


    # for comb in rotation_list:
    #     a1,b1,c1,d1=comb[0](a), comb[1](b), comb[2](c), comb[3](d)
    #     w1,x1,y1,z1 = master_list.index(a1), master_list.index(b1), master_list.index(c1), master_list.index(d1)

        if  {w1,x1} in compatible_blocks and     \
            {w1, y1} in compatible_blocks and   \
            {w1, z1} in compatible_blocks and \
            {x1, y1} in compatible_blocks and \
            {x1, z1} in compatible_blocks and \
            {y1, z1} in compatible_blocks:
            # print(f"{a1}\n{b1}\n{c1}\n{d1}")
            # print(f"{check_diff(a1,b1,c1,d1)}")
            flag+=1

        if flag>4:
            break

    return flag

def final_check_v9(yo,rotation_list,strangleness):
    a,b,c,d=yo
    flag=0
    #check=0
    #check1=0
    i=0
    lower_limit=0 if strangleness==1 else 1
    upper_limit=6 if strangleness==1 else 5
    num_check=6 if strangleness==1 else 4
    for comb in rotation_list:
        #flag += check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=6)
        #i+=1
        finalee=check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=num_check,x=lower_limit,y=upper_limit)
        if finalee==True:
            flag+=1
        if flag>4:
            break

    return flag

def final_check_v10(yo,rotation_list,layer_list):
    a1,b1,c1,d1=yo
    flag=0
    #check=0
    #check1=0
    i=0
    for lay in layer_list:
        a, b, c, d = (yo[i] for i in lay)
        for comb in rotation_list:
            #flag += check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=6)
            #i+=1
            #finalee=check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=6,x=0,y=6)
            finalee = check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d))
            if finalee==True:
                flag+=1
            # if flag>4:
            #     break

    return flag

def final_check_v11(yo,rotation_list):
    a,b,c,d=yo
    flag=0
    #check=0
    #check1=0
    i=0
    for comb in rotation_list:
        #flag += check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d),num=6)
        #i+=1
        #finalee=check_diff(comb[0](a), comb[1](b), comb[2](c), comb[3](d))#,num=6,x=0,y=6)
        sum_ish=np.array(comb[0](a))+ np.array(comb[1](b))+ np.array(comb[2](c))+ np.array(comb[3](d)) - [100,10,10,10,10,100]
        if np.all(sum_ish[1:5]==0):
            flag+=1

        # if finalee==True:
        #     flag+=1
        if flag>4:
            break

    return flag

def u1(a:list)->list:
    #0 1 2 3 4 5 address
    #1 2 3 4 5 6 initial
    #1 3 4 5 2 6 final
    a=[a[0],a[2],a[3],a[4],a[1],a[5]]
    return a

def u2(a):
    a_new=u1(u1(a))
    return a_new

def u3(a):
    a=u1(u2(a))
    return a

def l1(a):
    #0 1 2 3 4 5
    #1 2 3 4 5 6 
    #4 1 3 6 5 2
    a=[a[3],a[0],a[2],a[5],a[4],a[1]]
    return a 

def l2(a):
    a=l1(l1(a))
    return a

def l3(a):
    a=l1(l2(a))
    return a 

def m0(a):
    return a 

def check_perms(check_list:list):
    perm_list=[]
    rotation=[u1,u2,u3,l1,l2,l3]
    #rotation=[m0,u1,u2,u3,l1,l2,l3]
    for rot in rotation:
        for fax in check_list:
        #print(rot)
            perm_list.append(rot(fax))
    return perm_list
