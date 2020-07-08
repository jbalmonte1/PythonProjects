import math

def split(A):

    i = math.floor(len(A)/2)
    resultingList = []
    
    for j in range(i+1):
        a1 = A[:i]
        a2 = A[i:]
        suma1 = sum(a1)
        suma2 = sum(a2)
        diff = abs(suma1 - suma2)
        
        print(i)
        print("comparing {} and {}".format(a1, a2))
        print(diff)
        resultingList.append(diff)
        print("resulting list: {}".format(resultingList))
        
        if abs(suma1) > abs(suma2):
            i = i - math.floor(len(a1)/2)
        elif abs(suma1) < abs(suma2):
            i = i + math.floor(len(a2)/2)
        else:
            return [0] 
    
    return resultingList
    
def solution(A):
    resultingList = []
    for i in range(len(A)):
        a1 = A[:i]
        a2 = A[i:]
        suma1 = sum(a1)
        suma2 = sum(a2)
        diff = abs(suma1 - suma2)
        
        resultingList.append(diff)
    
    return min(resultingList)

def solutionC(A):
    left = A[0]
    right = sum(A[1::])
    diff = abs(left - right)

    for p in range(1, len(A)):
        ldiff = abs(left - right)
        if ldiff < diff:
            diff = ldiff
        print(A[p])
        left += A[p]
        right -= A[p]

    return diff
    
    
if __name__ == "__main__":
    A1 = [3, 1, 2, 4, 3]
    A2 = [3, 1, 2]
    A3 = [2, -1000, 3, 1000] + [1000]*50000
    print(solutionC(A1))