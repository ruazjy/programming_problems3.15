def num_of_1(n):
    ret=0
    while n:
        ret+=1
        n=n&n-1
    return ret