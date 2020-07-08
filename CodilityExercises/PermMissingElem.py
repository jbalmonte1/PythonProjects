
def solution(A):
    if A:
        keyset = set(list(range(1, len(A)+1)))
        valueset = set(A)
        
        print(keyset)
        print(valueset)
        
        item = keyset.difference(valueset)
        if not item:
            return len(A)+1
        else:
            return item.pop()
    else:
        return 1

if __name__ == "__main__":
    #A = list(range(1,999999))+[1000000]
    A = [1]
    print(solution(A))