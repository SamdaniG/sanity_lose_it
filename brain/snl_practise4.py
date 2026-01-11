#import sanity_funcs as sf
a=[1,2,3,1,2,2]


def multiplicity_check_list(a:list):#a=[1,1,2,2,3,3]
    ''' This function checks how many times a number is repeated in a list, input-->list and returns the max repeated element in the list,
    For example y=[a,a,a,b,c,d], this func returns 3'''
    flag=0  
    set_a=set(a)
    flag_a=set()
    for x in set_a:
        flag_a.add(a.count(x))

    return max(flag_a)


print(multiplicity_check_list(a))

if multiplicity_check_list(a)==3:
    print(True)