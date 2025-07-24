def find_pairs_with_sum(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

nums = [1, 2, 3, 4, 5]
target = 5
print(find_pairs_with_sum(nums, target))
