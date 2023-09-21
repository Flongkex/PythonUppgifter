def flippblipp(n):
    if (n%3==0) and (n%5==0):
        return "flippblipp"
    if n%3 == 0:
        return "flipp"
    if n%5 == 0:
        return "blipp"
    else:
        return str(n)
    
    
for i in range(1,40):
    print(flippblipp(i))
    