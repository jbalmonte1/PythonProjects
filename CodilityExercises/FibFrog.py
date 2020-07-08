def generateFib(N):
    fib = [0, 1]
    for i in range(2, N+1):
        fib += [fib[i - 2] + fib[i - 1]]
        if fib[-1] >= N:
            break
        
    return fib

def solution(A):
    A.append(1)
    target = len(A)

    fib = generateFib(target)
    fib.reverse()
    fib.pop()
    
    count = 0
    h = 0
    
    print(fib)
    print(A)

    while h != target:
        #print(h, target)
        for i in fib:
            #check if hoppable
            #print("Checking {} and {} against {}".format(i, h, target))
            if (h + i <= target):
                if A[h+i-1] == 1:
                    #make the jump
                    count += 1
                    h += i
                    print(i)
                    break
        else:
            return -1
        
    return count

if __name__ == "__main__":
    A = [1]*100
    print(solution(A))