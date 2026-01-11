import sanity_funcs as sf
#from sanity_lose_it_ver4 import layer_list
"""
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

var_list=[]
a=[0,83,207,252]
var_list=sf.var_check(a,var_list,layer_list)
for b in var_list:
    print(b)

print(len(var_list))

yo=[1,2,3,4]
dict={}
dict[tuple(yo)]=0

print(dict[tuple(yo)])

yo1=[1,2,3,45]
dict[tuple(yo1)]=1

print(dict)

if dict[(1,2,3,4)]==0 in dict:
    print(True)

"""
"""
rotation=[sf.m0,sf.u1,sf.u2,sf.u3,sf.l1,sf.l2,sf.l3]
rotation=[1,2,3,4,5,6,7]
rotation_list=[]
for func_a in rotation:
    for func_b in rotation:
        for func_c in rotation:
            for func_d in rotation:
                if sf.multiplicity_check([func_a, func_b, func_c, func_d],3)==0:
                    rotation_list.append([func_a, func_b, func_c, func_d])

print(len(rotation_list))

for f in rotation_list:
    print(f)

b=[4,2,3,1,1,4]
a=[5,4,2,3,8,1]
ho=sf.check_diff(a,b,num=6,x=0,y=6)
print(ho)

"""

'''
meh_list=[]

for i in range (0,331):
    meh_list.append(i)

print(len(meh_list))

i=0
for a in meh_list:
    for b in meh_list:
        if b<=a:
            continue
        i+=1
        print(f"a:{a:03}  b:{b:03}   {i:12}")

#print(i)

'''

'''
a={1,65,34,21}
b={34,64}

if b in a:
    print(True)
else:
    print(False)


'''    

a=5
b=1

#c=int(str(f"{a:03}")+str(f"{b:03}"))
c=int(f"{a:03}{b:03}")
print(c)
print(type(c))