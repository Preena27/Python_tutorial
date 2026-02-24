def steps(number):
    if number <= 0 :
        raise ValueError("Only positive integers are allowed")
    count = 0 
    cur = number
    while cur != 1:
        if cur % 2 == 0:
            cur = cur // 2
        else:
            cur = 3* cur+1 
        count += 1 
    return count