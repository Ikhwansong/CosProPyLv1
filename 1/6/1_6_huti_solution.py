#You may use import as below.
#import math
def solution(pos):
    # Write code here.
    y = [i for i in range(1,9)]
    x = ["A","B","C","D","E","F","G","H"]
    cy = int(pos[1])
    cx = pos[0]
    move1 = [2,-2]
    move2 = [1,-1]
    answer = 0
    for i in move1:
        for j in move2:
            try:
                if y[y.index(cy)+i] in y and x[x.index(cx)+j] in x and y.index(cy)+i >=0 and x.index(cx)+j >=0:
                    answer += 1
            except IndexError:
                answer += 0
            try:
                if y[y.index(cy)+j] in y and x[x.index(cx)+i] in x and y.index(cy)+j >=0 and x.index(cx)+i >=0:
                    answer += 1
            except IndexError:
                answer += 0
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")