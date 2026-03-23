def commands(binary_str):
    map = ["wink", "double blink", "close your eyes", "jump"]
    a = []
    for i in range(4):
        if binary_str[4-i] == "1":
            a.append(map[i])
    if binary_str[0] == "1":
        a.reverse() 
    return a