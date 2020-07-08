def solution(A):
    
    #remove negative integers
    #numpyA = numpy.array(A)
    #numpyA = numpyA[numpyA > 0]
    modA = [i for i in A if i > 0]
    setA = set(modA)
    setExpected = set(range(1, len(A)+2))
    
    diff = setA.symmetric_difference(setExpected)
    
    return min(list(diff))

if __name__ == "__main__":
    A = [0]
    print(solution(A))