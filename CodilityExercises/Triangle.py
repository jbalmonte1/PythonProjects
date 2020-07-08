
def solution(A):
    if len(A) < 3: return 0
    A.sort()  
    return max([1 if A[i] + A[i+1] > A[i+2] else 0 for i in range(0, len(A)-2)])

if __name__ == "__main__":
    A = [10, 2, 5, 1, 8, 20]
    print(solution(A))