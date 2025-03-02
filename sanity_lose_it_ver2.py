import time
import csv
import os
import sanity_funcs as sf


prime=[1,2,3,4]
complete_list=[1,2,3,4,5,6]
master_list=[]
possible_solution=[]


###Extracting the last name of the file ie sanity_lose_it_xxx
ver_name = os.path.splitext(__file__)[0]
ver_name=ver_name.split('_')[-1]




i=0

flag23=0

for a in prime:
    for b in prime:
        for c in prime:
            for d in prime:
                        yo=[a,b,c,d]
                        flag23+=1
                        #print(yo)
                        flag=sf.multiplicity_check(yo,2)
                        if flag==0:
                            master_list.append(yo)
                        i+=1

#print(i)
print(f"The total possible scenarios are {flag23:,}, but it comes down to this after multiplicity check")
print(f"Length of master list: {len(master_list)}")

"""
#for printing master_list
for x in master_list:
     print(x)
"""
"""
block1=master_list
block2=master_list
block3=master_list
block4=master_list

"""#print(f"{block1} '\n' {block2} '\n' {block3}'\n'{block4}")

block1=[]
block2=[]
block3=[]
block4=[]



for a in master_list:
    if a[0]==1:
        block1.append(a)
        
    elif a[0]==2:
        block2.append(a)
        
    elif a[0]==3:
        block3.append(a)
        
    else:
        block4.append(a)

print(f"Length of a single block: {len(block1)}")

start_time=time.time()

flag1=0
flag2=0
flag3=0
flag4=0

with open(f'{ver_name}.csv', 'w') as file:
        file.truncate()


for a in block1:
     for b in block2:
          if sf.check_diff2(a,b,4,0,4)==False:
               flag1+=1
               continue
          else:
               for c in block3:
                    if sf.check_diff3(a,b,c,4,0,4) == False:
                         flag2+=1
                         continue
                    else:
                         for d in block4:
                              if sf.check_diff4(a,b,c,d,4,0,4)==False:
                                   flag3+=1
                                   continue
                              else:
                                   possible_solution.append([a,b,c,d])
                                   sf.write2file([a,b,c,d],ver_name)
                                   time_di=sf.time_diff(start_time)
                                   print(f"Time taken:{time_di:0.5f} minutes\tFlag1:{flag1:,}\tFlag2:{flag2:,}\tFlag3:{flag3:,}\t\tPossible slns: {len(possible_solution):,}", end="\r")

#print(f"flag1={flag1}\t flag2={flag2} \t flag3={flag3}")
print("\n")
print(len(possible_solution),"\a")
#print(possible_solution)

#sf.write2file(possible_solution)