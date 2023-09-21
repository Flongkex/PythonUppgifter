def flippblipp(n):
    if (n%3==0) and (n%5==0):
        return True
    if n%3 == 0:
        return "flipp"
    if n%5 == 0:
        return "blipp"
    else:
        return str(n)
    
alive = True

while alive:

    
