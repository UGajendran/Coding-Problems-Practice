#array Subset
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#Convert two arrays into sets
set_a = set(a)
set_b = set(b)

#Check b is subset of a
check_is_subset = set_b.issubset(set_a)

#If yes Print "True"
if check_is_subset:
    print(True)
else:     #else "False"
    print(False)
