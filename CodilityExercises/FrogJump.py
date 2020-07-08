import math

def solution(X, Y, D):
    return math.ceil((Y - X)/D)
    
    
if __name__ == "__main__":
    X = 1000000000
    Y = 1000000000
    D = 10000000000000000
    print(solution(X, Y, D))