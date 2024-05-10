inp = int(input("number:"))


row = 1
blank_spaces = 0


while row <= (inp - 1):
           #so the number we're on is the number of *s we print
    if row == 1:
        print("*")
    elif row == 2:
        print("**")
    elif row > 2: 
        print("*", end = '')
        blank_saces = row -2
        while blank_saces > 0:
            print("_", end = '')
            blank_saces -= 1
        print("*")
    row += 1

print("*" * inp)