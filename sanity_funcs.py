import time, csv,json

def multiplicity_check(a,num=2):#a=[1,1,2,2,3,3]
    flag=0  
    for x in a:
        if a.count(x)>num:
            flag+=1
    return flag

def check_diff(*args,num=4, x=1, y=5):
    flag = 0
    for i in range(x, y):
        sample_set = {arg[i] for arg in args}
        if len(sample_set) == len(args):
            flag += 1
            continue
        else:
            break
    return flag == num

def time_diff(a):
    end_time=time.time()
    diff=(end_time-a)/60

    if diff<1:
        return diff*60
    else:
        return diff

def rotations(a,layer_list):
    lay_list=[]  # [3, 2, 1, 0]
    for layer in layer_list:
        app=[a[layer[0]],a[layer[1]],a[layer[2]],a[layer[3]]]
        lay_list.append(app)
    return lay_list

def var_check(a,var_list,layer_list):
    for layer in layer_list:
        app=[a[layer[0]],a[layer[1]],a[layer[2]],a[layer[3]]]
        #ythough=[comb[0](a), comb[1](b), comb[2](c), comb[3](d)]
        var_list.append(app)
    return var_list

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
    
"""
    if flag==0:
        check+=1    

    if flag==1:
        return True,check,check1 
    else:
        return False,check,check1

"""

def u1(a:list)->list:
    #0 1 2 3 4 5
    #1 2 3 4 5 6 
    #1 3 4 5 2 6
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

def write2file(yolist,name):
    """#for csv
    with open(f'{name}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(yolist)  # Write all the rows at once
        writer.writerow([])

    """
    #for json
    with open(f'{name}.json', "w") as file:
        json.dump(yolist, file)

    
def check_perms(check_list):
    perm_list=[]
    rotation=[u1,u2,u3,l1,l2,l3]
    #rotation=[m0,u1,u2,u3,l1,l2,l3]
    for rot in rotation:
        for fax in check_list:
        #print(rot)
            perm_list.append(rot(fax))
    return perm_list


"""   

def check_diff2(a,b,num=3,x=1,y=5):
    flag=0
    for i in range(x,y):
        sample_set={a[i],b[i]}
        if len(sample_set)==2:
            flag+=1
            continue
        else:
            break
    return flag==num

def check_diff3(a,b,c,num=3,x=1,y=5):
    flag=0
    for i in range(x,y):
        sample_set={a[i],b[i],c[i]}
        if len(sample_set)==3:
            flag+=1
            continue
        else:
            break
    return flag==num

def check_diff4(a,b,c,d,num=3,x=1,y=5):
    flag=0
    for i in range(x,y):
        sample_set={a[i],b[i],c[i],d[i]}
        if len(sample_set)==4:
            flag+=1
            continue
        else:
            break
    return flag==num


def check_diff_finale(a,b,c,d):
    flag=0
    element_check=[1,2,3,4]
    for i in element_check:
        sample_set={a[i],b[i],c[i],d[i]}
        if len(sample_set)==4:
            flag+=1
            continue
        else:
            break
    if flag==6:
        return 1
    else:
        return 0

"""