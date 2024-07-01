"""
Author : Michael Shepherd M
Date   : 01 Jul 2024
"""

from typing import List

def permute_recursive(nums: List[int]) -> List[List[int]]:
    """
    Return all permutations.

    >>> permute_recursive([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result: List[List[int]] = []
    if len(nums) == 0:
        return [[]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_recursive(nums)
        for perm in permutations:
            perm.insert(0, n)  # Insert element at the beginning
        result.extend(permutations)
        nums.append(n)
    return result

def permute_backtrack(nums: List[int]) -> List[List[int]]:
    """
    Return all permutations of the given list.

    >>> permute_backtrack([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    def backtrack(start: int) -> None:
        if start == len(nums) - 1:
            output.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack

    output: List[List[int]] = []
    backtrack(0)
    return output

if __name__ == "__main__":
    import doctest

    res = permute_backtrack([1, 2, 3])
    print(res)
    doctest.testmod()
