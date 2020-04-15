#You may use import as below.
#import math
#[[1,2,3],[8,9,4],[7,5,6]]
#[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
def solution(n):
    # Write code here.
    li = [1]
    for i in range(1,n):
        if i%2 == 1:
            li.append(2*n*i-i**2)
        else:
            li.append((2*n*i)-(i**2-1))
    return sum(li)

#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 5
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")