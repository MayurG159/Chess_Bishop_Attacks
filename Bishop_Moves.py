def No_places_to_attack(row, col):
    attacks = 0

    # Topright
    r, c = row, col
    while r < 8 and c < 8:
        r += 1
        c += 1
        attacks += 1

    # Topleft
    r, c = row, col
    while r < 8 and c > 1:
        r += 1
        c -= 1
        attacks += 1

    # Lowerleft
    r, c = row, col
    while r > 1 and c > 1:
        r -= 1
        c -= 1
        attacks += 1

    # Lowerright
    r, c = row, col
    while r > 1 and c < 8:
        r -= 1
        c += 1
        attacks += 1

    print("\nNumber of places the bishop can attack:", attacks)


row = int(input("Enter the row (1-8) of the bishop's position: "))
col = int(input("\nEnter the column (1-8) of the bishop's position: "))

if row < 1 or row > 8 or col < 1 or col > 8:
    print("\nInvalid input! Row and column numbers must be between 1 and 8.")
else:
    No_places_to_attack(row, col)

input("Press Enter to exit")


