from collections import Counter

def solutionX(N, A):
    counters = [0]*N
    
    for j in A:
        maxcount = max(counters)
        if j > N:
            counters = [maxcount]*N
        else:
            counters[j-1] += 1
    
    return counters

def checkindex(N, A):
    maxcountop = N + 1
    if maxcountop in A:
        i = A.index(N+1)
    else:
        i = ""
    
    #print(i)
    return i

def solution(N, A):
    counters = [0]*N

    i = checkindex(N, A)
    while i != "":
        split = A[:i]
        A = A[i+1:]
    
        #print(A)
        summary = Counter(split)
        #print(summary)
        if summary != {}:
            for key, value in summary.items():
                counters[key-1] += value
            counters = [max(counters)]*N
        #print(counters)
        i = checkindex(N, A)
        #print("===========")
        
    summary = Counter(A)
    for key, value in summary.items():
        counters[key-1] += value
    
    return counters

if __name__ == "__main__":
    N = 100000
    A = [100001]*N
    #print(solution(N, A))
    print(solution(N, A))