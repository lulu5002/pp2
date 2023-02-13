def solve(numheads, numlegs):
    error="No solution"
    chicken_num=0
    rabbit_num=0
    if(numheads>=numlegs):
        print(error)
    elif(numlegs%2!=0):
        print(error)
    else:
        rabbit_num=(numlegs-2*numheads)/2
        chicken_num=numheads-rabbit_num
    print(int(chicken_num), int(rabbit_num))
solve(35, 94)

