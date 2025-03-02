import sanity_funcs as sf
#from sanity_lose_it_ver4 import layer_list

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