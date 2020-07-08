def solution(A):
    
    if not A:
        return 0
    
    minAkey, minAval = min(enumerate(A), key = lambda x:x[1])
    maxAval = max(A[minAkey:])
    
    gain = maxAval - minAval
    if gain <= 0:
        return 0
    else:
        return gain
    
if __name__ == "__main__":
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    B = [100000, 1000, 100001]
    print(solution(B))