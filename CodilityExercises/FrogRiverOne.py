
def solution(X, A):
    completed = set(range(1,X+1))
    progress = set()
    
    for i in range(len(A)):
        progress.add(A[i])
        if completed == progress:
            return i
    else:
        return -1

if __name__ == "__main__":
    A = [100000, 3, 1, 4, 2, 3, 5, 4]+[0]*100000
    X = 5000
    print(solution(X, A))