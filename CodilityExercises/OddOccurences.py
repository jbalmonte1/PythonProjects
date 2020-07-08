from collections import deque

def solution(A):
    arraydeque = deque(A)
    while len(arraydeque) != 1:
        item = arraydeque.popleft()
        try:
            arraydeque.remove(item)
        except ValueError:
            return item

    return arraydeque[0]

if __name__ == '__main__':
    A = [1000000000]*999998+[999999999999]
    print(len(A))
    print(solution(A))