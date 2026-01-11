#from test import A


yolo=[
{
"Soln_rank": 1,
"List0": [1,1,2,2,3,3],
"List1": [2,4,1,3,4,1],
"List2": [3,3,4,4,2,2],
"List3": [4,2,3,1,1,4],
"Flags": 5,
"Position": [0,165,234,294]
},
{
"Soln_rank": 6,
"List0": [1,1,2,3,4,2],
"List1": [2,3,1,4,2,3],
"List2": [3,4,4,2,1,1],
"List3": [4,2,3,1,3,4],
"Flags": 4,
"Position": [8,148,250,295]
},
{
"Soln_rank": 27,
"List0": [1,2,2,3,4,3],
"List1": [2,1,3,1,2,4],
"List2": [3,4,4,2,1,1],
"List3": [4,3,1,4,3,2],
"Flags": 4,
"Position": [57,111,250,314]
},
{
"Soln_rank": 32,
"List0": [1,2,2,3,4,3],
"List1": [2,3,1,4,2,4],
"List2": [3,1,4,1,3,2],
"List3": [4,4,3,2,1,1],
"Flags": 2,
"Position": [57,149,201,328]
},
{
"Soln_rank": 36,
"List0": [1,2,2,3,4,4],
"List1": [2,1,3,1,2,3],
"List2": [3,4,4,2,1,1],
"List3": [4,3,1,4,3,2],
"Flags": 2,
"Position": [58,110,250,314]
},
{
"Soln_rank": 50,
"List0": [1,2,3,3,4,4],
"List1": [2,1,4,1,2,3],
"List2": [3,4,2,2,1,1],
"List3": [4,3,1,4,3,2],
"Flags": 2,
"Position": [67,123,240,314]
}
]
sos=2
'''print(f"len before: {len(yolo)}")
for a in yolo:
    #print(a)
    print(a['Flags'])
    if a["Flags"]!=sos:
        loc=yolo.index(a)
        #yolo.pop(loc)
        yolo.remove(loc)


for a in yolo:
    print(a)

print(f"len after: {len(yolo)}")

'''
'''
print(f"len before: {len(yolo)}")
yolo = [a for a in yolo if a["Flags"] <= sos]

print(f"len after: {len(yolo)}")
for a in yolo:
    print(a)
print(f"len after: {len(yolo)}")

'''

'''
a={313, 65, 0}
b={123,45,313,32343,65,12,23,212,0,3434}

if a&b==a:
    print(True)

'''    
def multiplicity_check(a:list,num:int =2):#a=[1,1,2,2,3,3]
    ''' This function checks how many times a number is repeated in a list, input-->list, accepted repeatance number'''
    flag=0  
    a_set=set(a)
    for x in a_set:
        if a.count(x)==num:
            flag+=1
    return flag
#import sanity_funcs as sf
a=[1,1,2,4,3,15,1,4,4,4,4,]
print(multiplicity_check(a,3))