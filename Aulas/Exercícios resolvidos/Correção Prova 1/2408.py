comp1, comp2, comp3 = input().split()

comp1 = int(comp1)
comp2 = int(comp2)
comp3 = int(comp3)

if comp1 > comp2 and comp2 > comp3:
    print(comp2)
elif comp3 > comp2 and comp2 > comp1:
    print(comp2)
elif comp2 > comp1 and comp1 > comp3:
    print(comp1)
elif comp3 > comp1 and comp1 > comp2:
    print(comp1)
elif comp2 > comp3 and comp3 > comp1:
    print(comp3)
elif comp1 > comp3 and comp3 > comp2:
    print(comp3)