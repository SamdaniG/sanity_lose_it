import time
import sanity_funcs as sf

prime=[1,2,3,4]
master_list=[]  
possible_solution=[]
element_check=[0,1,2,3,4,5]

#print(master_list)

i=0

for a in prime:
    for b in prime:
        for c in prime:
            for d in prime:
                for e in prime:
                    for f in prime:
                        yo=[a,b,c,d,e,f]
                        #print(yo)
                        flag=sf.multiplicity_check(yo,2)
                        if flag==0:
                            master_list.append(yo)
                        i+=1

#print(i)
#print(len(master_list))
print(f"Length of master list: {len(master_list)}")
#print(master_list)
"""
for a in master_list:
    print(a)

"""
block1=[]
block2=[]
block3=[]
block4=[]

#separated the blocks by position in a[1]
for a in master_list:
    if a[1]==1:
        block1.append(a)
        
    elif a[1]==2:
        block2.append(a)
        
    elif a[1]==3:
        block3.append(a)
        
    else:
        block4.append(a)

print(f"Length of a single block: {len(block1)}")


flag1=0
flag2=0
flag3=0
flag4=0

start_time=time.time()

with open('numbers.csv', 'w') as file:
        file.truncate()


for a in block1:
     for b in block2:
          if sf.check_diff2(a,b)==False:
               flag1+=1
               continue
          else:
               for c in block3:
                    if sf.check_diff3(a,b,c) == False:
                         flag2+=1
                         continue
                    else:
                         for d in block4:
                              if sf.check_diff4(a,b,c,d)==False:
                                   flag3+=1
                                   continue
                              else:
                                   flag4+=1

                                   #if sf.final_check([a,b,c,d]):

                                   possible_solution.append([a,b,c,d])
                                   sf.write2file([a,b,c,d])
                                   time_di=sf.time_diff(start_time)
                                   #print(f"[a,b,c,d]:{[a,b,c,d]}",end="\r")
                                   #print("\n")
                                   print(f"Time:{time_di:0.2f}\tFlag1:{flag1:,}\tFlag2:{flag2:,}\t\tFlag3:{flag3:,}\t\tFlag4:{flag4}\t\tPossible solutions: {len(possible_solution):,}", end="\r")

print(len(possible_solution))

with open("final solution.txt", "w") as file:
    for item in possible_solution:
        file.write(f"{item}\n")

print(f"The file has finally finished running\a")