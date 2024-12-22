# Pattern format

pattern = int(input("Enter the size of the pattern: "))
j = pattern
while j:
    for i in range(pattern):
        print("*", end="")
    print()
    j -= 1