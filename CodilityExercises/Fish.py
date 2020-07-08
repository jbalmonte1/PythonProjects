from collections import deque

def solution(A, B):
    D = list(zip(A, B))
    totalAlive = 0
    
    D = deque([i for i in D if i[0] != 0])
    
    for i in range(len(A)):
        if len(D) > 0:
            #lucky fish
            if D[0][1] == 0:
                D.popleft()
                totalAlive += 1
            elif D[0][1] == 1 and len(D) == 1:
                D.popleft()
                totalAlive += 1
                
            #encounter
            if len(D) > 1:
                if D[0][1] == 1 and D[1][1] == 0:
                    if D[0][0] > D[1][0]:
                        del D[1]
                    elif D[0][0] < D[1][0]:
                        del D[0]
                    else:
                        D[0], D[1] = D[1], D[0]
                    if len(D) == 0: break
    
    return totalAlive

if __name__ == "__main__":
    A = [1, 2]
    B = [0, 1]
    print(solution(A, B))