from doctest import master
from tabnanny import check
import sanity_funcs as sf
a=[1, 1, 2, 2, 3, 3]
b=[1, 2, 3, 1, 4, 3]
list=[]
#list=sf.check_perms([a],list)
"""
if b not in list and sf.check_diff2(a,b,4):
    list=sf.check_perms([a,b],list)
i=1
print(len(list))
for l in list:
    print(f"{i}\t {l}")
    i+=1"""
aiv=[]
for i in range(0,1440):
    aiv.append(i)
"""
print(len(aiv))
ii=0
for a in aiv:
    for b in aiv:
        for c in aiv:
            for d in aiv:
                ii+=1
                print(f"ii: {ii:,}",end="\r")

#print(f"{ii:,}")

"""
a=[4, 1, 1, 4, 3, 2]

yolo=sf.check_perms([a])
#for yo in yolo:
#    print(yo)
"""
check=[]
for i in range(1,50):
    check.append(i)

print(len(check))
print(check)

for i in check:
    a=i*2
    check.remove(a)
    print(i)

print(len(check))

"""

"""
prime=[1,2,3,4]
master_list=[]
flag23=0
for a in prime:
    for b in prime:
        for c in prime:
            for d in prime:
                for e in prime:
                    for f in prime:
                        yo=[a,b,c,d,e,f]
                        flag23+=1
                        #print(yo)
                        flag=sf.multiplicity_check(yo,2)
                        if flag==0:
                            master_list.append(yo)
                        i+=1

#print(i)
#print(len(master_list))
print(f"The total possible scenarios are {flag23:,}, but it comes down to this after multiplicity check")
print(f"Length of master list: {len(master_list)}")

for yo in master_list:
    yolist=sf.check_perms([yo])
    for yol in yolist:
        if yol in master_list:
            master_list.remove(yol)
            print(len(master_list))

for m in master_list:
    print(m)"""


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


#a=[[1, 1, 2, 2, 3, 3], [1, 3, 3, 4, 4, 2], [3, 2, 1, 1, 2, 4], [3, 4, 4, 3, 1, 1]]
a=[[1, 3, 3, 4, 4, 2], [1, 1, 2, 2, 3, 3], [3, 4, 4, 3, 1, 1], [3, 2, 1, 1, 2, 4]]
def rotations(a,layer_list):
    lay_list=[]  # [3, 2, 1, 0]
    for layer in layer_list:
        app=[a[layer[0]],a[layer[1]],a[layer[2]],a[layer[3]]]
        lay_list.append(app)



    return lay_list

yoloooo=rotations(a,layer_list)
print(len(yoloooo))
for a in yoloooo:
    print(a)
