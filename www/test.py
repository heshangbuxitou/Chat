# from __future__ import print_function
# while 1:
# 	a=[]  
# 	s = raw_input()
# 	# raw_input()里面不要有任何提示信息
# 	if s != "":
# 		for x in s.split():  
# 		    a.append(int(x))  
		   
# 		print sum_list(a)
# 	else:
# 		break

import functools
array = [1,9,5,4,8,7,6,2,1,5]
def defineCmp(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0
key = functools.cmp_to_key(defineCmp)        
print(sorted(array,key=key))
print(array)