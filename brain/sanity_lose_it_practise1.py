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

def check_diff_finale(a,b,c,d):
    flag=0
    element_check=[0,1,2,3,4,5]
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



def final_check(yo):
    a,b,c,d=yo
    #print(f"a={a},b={b},c={c},d={d}")
    rotation=[u1,u2,u3,m0,l1,l2,l3]
    rotation_list=[]
    for func_a in rotation:
        for func_b in rotation:
            for func_c in rotation:
                for func_d in rotation:
                    rotation_list.append([func_a, func_b, func_c, func_d])

    flag=0
    i=0
    for comb in rotation_list:
        """
        print(f"{comb}")
        print(a,b,c,d)
        print(comb[0](a), comb[1](b), comb[2](c), comb[3](d))
        print("\n")

        """
        flag += check_diff_finale(comb[0](a), comb[1](b), comb[2](c), comb[3](d))
        i+=1
        

    return flag==1

         



yo=[[1, 1, 2, 2, 3, 3], [2, 2, 1, 1, 4, 3], [3, 3, 4, 6, 1, 4], [6, 4, 3, 5, 2, 6]]
#yo=[[1, 1,1, 1, 1, 1], [2, 2, 2,2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]]

a,b,c,d=yo
#print(a)
#print(u1(a))
t=final_check(yo)

#print(t)

"""
comb=[u1,u1,u1,u1]
print(comb)
print(comb[0](a),comb[1](b),comb[2](c),comb[3](d))
"""
"""
a=[1,2,3,4,5,6]
b=[11,12,13,14,15,16]
c=[21,22,23,24,25,26]
d=[31,32,33,34,35,36]

#print(check_diff_finale(a,b,c,d))


import csv

import sanity_funcs as sf

yoloo = [[[1, 4, 4, 3], [2, 3, 3, 4], [3, 2, 1, 2], [4, 1, 2, 1]],[[1, 4, 4, 3], [2, 2, 1, 4], [3, 3, 2, 2], [4, 1, 3, 1]]]
#print(yoloo)

aa=[1,	1,	2,	2,	1,	3]
bb=[1,	2,	1,	3,	3,	3]
cc=[1,	3,	3,	4,	1,	2]
dd=[1,	4,	4,	1,	2,	2]

print(aa,bb,cc,dd)

print(sf.check_diff2(aa,bb,4))
print(sf.check_diff3(aa,bb,cc,4))
print(sf.check_diff4(aa,bb,cc,dd,4))

for i in range(1,5):
    print(i)

import os

# Get the name of the current file
current_file = os.path.splitext(__file__)[0]
current_file=current_file.split('_')[-1]

print(f"The current file being executed is: {current_file}")


def apply_carriage_returns(lines):
    for line in lines:
        # Print the line with a carriage return
        print(line, end='\r')
        # Adding a newline to actually see each output on a new line
        print()

# Example usage
lines = ["Line 1", "Line 2", "Line 3"]
apply_carriage_returns(lines)

"""
import sanity_funcs as sf
x=[]
alist=[1,1,2,2,3,3]
blist=[1,2,4,1,2,3]
sf.check_perms(alist,x)

print(x)

#blist=[1,2,3,1,2,3]

if blist in x:
    print(True)
else:
    print(False)


print(f"check_diff={sf.check_diff2(alist,blist,4)}")
if blist in x & sf.check_diff2(alist,blist,4)==False:
    print("nuh uh")
else:
    print("nope")

a=[1, 1, 2, 2, 3, 3]
list=[]
sf.check_perms([a],list)
print(list)