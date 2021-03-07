from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    i, j = 0, len(nums) - 1 # O(1)
    data = sorted(nums)  # O(n*log(n))
    while i < j:  # O(n)
        value = data[i] + data[j] # O(1)
        if value > target: # O(1)
            j -= 1  # O(1)
        if value < target: # O(1)
            i += 1 # O(1)
        if value == target: # O(1)
            break
    idx1 = nums.index(data[i])  # n
    if data[i] == data[j]: # O(1)
        idx2 = nums.index(data[j], idx1+1)  # n
    else:
        idx2 = nums.index(data[j])  # n
    return idx1, idx2  # n < n*(log(n)) < n^2
# O(nlog(n))
# O(1)

if __name__ == "__main__":
    target = 18
    nums = [11, 2, 15, 2, 7]
    print(two_sum(nums, target))
