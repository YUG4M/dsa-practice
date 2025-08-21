def has_repeating_pattern(lst):
    n = len(lst)
    for i in range(1, n // 2 + 1):
        pattern = lst[:i]
        if pattern * (n // i) == lst:
            return True
    return False

print(has_repeating_pattern([1, 2, 3, 1, 2, 3]))  # True
print(has_repeating_pattern([1, 2, 3, 4]))        # False