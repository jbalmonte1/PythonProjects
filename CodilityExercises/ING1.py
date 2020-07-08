def solution(N):
    return int(''.join(sorted(str(N), reverse = True)))

if __name__ == "__main__":
    N = 22011
    print(solution(N))