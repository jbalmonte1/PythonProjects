from collections import Counter
import array

def getMin(sliced):
    reference = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        
    summarized = list(set(sliced))
    for key, value in enumerate(summarized):
        summarized[key] = reference[value]
    
    return min(summarized)

def solution(S, P, Q):
    reference = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    #check if all are same letter
    if len(set(S)) == 1:
        return [reference[S[0]]]*len(P)
    
    #slice S with P and Q      
    finalList = [getMin(S[P[i]:Q[i]+1]) for i in range(len(P))]
    
    return finalList

if __name__ == "__main__":
    S = "G"*100000
    P = [0]*50000
    Q = [6]*50000
    print(solution(S, P, Q))