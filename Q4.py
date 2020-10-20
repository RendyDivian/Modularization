def is_member(val, list):
    if list.count(val) >= 1:
        return True
    else:
        return False


print(is_member(2, [1, 2, 3, 4]))
