def solve(numheads, numlegs):
    error = "No solution"
    
    if(numheads >= numlegs):
        print(error)
    elif(numlegs % 2 != 0):
        print(error)
    else:
        rabbit = (numlegs - 2 * numheads) / 2
        chicken = numheads - rabbit
        print(int(rabbit), int(chicken))

a = int(input())
b = int(input())
solve(a, b)