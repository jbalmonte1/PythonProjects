
from collections import Counter

def flip(A, pattern):
    flips = 0
    
    for i in range(len(A)):
        if A[i] != pattern[i]:
            #flip and increment number of flips if binary digit is not according to pattern
            A[i] = pattern[i]
            flips += 1    

    return flips

def solution(A):
    #get both possible patterns of alternating 0 and 1 with same length as A
    pattern1 = [0 if i % 2 == 0 else 1 for i in range(len(A))]
    pattern2 = [1 if i % 2 == 0 else 0 for i in range(len(A))]
    
    #check the complexity of making the pattern from A by doing bitwise and operation and summarizing the needed flips (and operation resulting to 0)
    A1 = [x and y for x, y in zip(A, pattern1)]
    A2 = [x and y for x, y in zip(A, pattern2)]
    toFlipA1 = Counter(A1)[0]
    toFlipA2 = Counter(A2)[0]
    
    if toFlipA1 < toFlipA2:
        #using pattern1 as it is easier to make
        return flip(A, pattern1)
    elif toFlipA1 > toFlipA2:
        #using pattern2 as it is easier to make
        return flip(A, pattern2)
    else:
        #both patterns have the same complexity to make. choose 1
        return flip(A, pattern1)

if __name__ == "__main__":
    A = [0]
    print(solution(A))