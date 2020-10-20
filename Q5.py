def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if lst1.count(j) >= 1:
                return True
            elif lst2.count(i) >= 1:
                return True
            else:
                return False


print(overlapping([1, 2, 3], [4, 5, 6]))
