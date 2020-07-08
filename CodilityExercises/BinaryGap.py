# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def convertToBinary(N):
    return '{0:b}'.format(N)
    
def getBinaryGap(N):
    longest = 0
    splitted = N.split('1')
    if N[-1] == '0': splitted = splitted[0:-1]
    for count, i in enumerate(splitted):
        if i != "":
            if len(i) > longest: longest = len(i)
    
    return(longest)
    

def solution(N):
    # write your code in Python 3.6
    
    binB = (convertToBinary(N))
    print(binB)
    print(getBinaryGap(binB))
    
if __name__ == "__main__":
    solution(647)