def solution(A):
    N = len(A)
    target = set(range(1, N+1))
    current = set(A)
    
    print(target)
    print(current)
    
    diff = target.symmetric_difference(current)

    if len(diff) == 0:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    A = [1,3]
    print(solution(A))