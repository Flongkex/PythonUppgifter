def flippblipp(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return True
    if n % 3 == 0:
        return "flipp"
    if n % 5 == 0:
        return "blipp"
    else:
        return str(n)
    
current_number = 1
alive = True

print(' '*6, flippblipp(current_number))
current_number += 1
while alive:
    player_guess = input("Nästa: ")

    if player_guess != flippblipp(current_number):
        print(f"Fel -  {flippblipp(current_number)}")
        print("Game Over")
        alive = False
    
    current_number += 1
