# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
    
if __name__ == "__main__":
    a = [4, 3, 1, 4, -1, 2, 1, 5, 7]
    b = [""]*len(a)

    for i, j in enumerate(a):
        c = [""]*len(a)
        for k, l in enumerate(a):
            print("Comparing {} with {} at index {} and {}".format(j, l, i, k))
            if j < l:
                c[k] = abs(i-k)
            else:
                c[k] = 0
        print(c)
        c = [x for x in c if x != 0]
        if not c:
            b[i] = 0
        else:
            b[i] = min(c)
    
    print(b)