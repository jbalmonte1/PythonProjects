
def generatematt(x, y):
    conelen = int((x-1)/2)
    welcome = "WELCOME"
    
    #top pyramid
    for i in range(conelen):
        pattern = ".|."*((i*2)+1)
        dashpattern = "-"*(int((y-len(pattern))/2))
        print(dashpattern+pattern+dashpattern)
        
    #center
    dashpattern = "-"*(int((y-len(welcome))/2)) 
    print(dashpattern+welcome+dashpattern)
    
    #bottom pyramid
    for i in range(conelen):
        pattern = ".|."*((x-2) - (2*i))
        dashpattern = "-"*((int((y-len(pattern))/2)))
        print(dashpattern+pattern+dashpattern)

if __name__ == "__main__":
    inp = input()
    x, y = inp.strip().split(" ")
    generatematt(int(x), int(y))