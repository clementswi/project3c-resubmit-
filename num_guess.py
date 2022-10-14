n=int(input("Enter the integer for the player to guess:"))
x=int(input("Enter your guess:"))
if x == n:
    print("You guessed it.")
while x != n:
        if x > n:
            y = int(input("Too high - try again:"))
            if y > n:
                z = int(input("Too high - try again:"))
            if y < n:
                r = int(input("Too low - try again:"))
            if y == n or z == n or r == n:
                print("You guessed it.")
                break
        if x < n:
            q = int(input("Too low - try again:"))
            if q > n:
                v = int(input("Too high - try again:"))
            if q < n:
                w = int(input("Too low - try again:"))
            if q == n or v == n or w == n:
                print("You guessed it.")
                break
