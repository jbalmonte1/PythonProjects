from collections import Counter

def solution(A):
    countdict = dict(Counter(A))
    countdictvalues = list(countdict.values())
    
    if not A:
        return -1
    
    print(countdict)
    print(countdictvalues)
    
    maxkey, maxval = max(enumerate(countdictvalues), key = lambda x:x[1])
    print(maxkey, maxval)
    countdictkeys = list(countdict.keys())
    
    #check if there are two maxvals
    if Counter(countdictvalues)[maxval] > 1:
        return -1
    elif maxval <= len(A)/2:
        return -1
    else:
        return A.index(countdictkeys[maxkey])
           

if __name__ == "__main__":
    A = [-5023, 123, 123]
    print(solution(A))