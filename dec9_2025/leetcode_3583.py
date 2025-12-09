from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        modulo=10**9 + 7

        n = len(nums)
        if n < 3:
            return 0

        # Special case for length 3
        if n == 3:
            return 1 if nums[0] == nums[1] * 2 and nums[2] == nums[1] * 2 else 0

        # Build index list for each value
        positions_dict = defaultdict(list)
        for i, val in enumerate(nums):
            positions_dict[val].append(i)

        result = 0

        # For each possible middle index
        for j in range(1, n - 1):
            target = nums[j] * 2
            pos_list = positions_dict.get(target)
            if not pos_list:
                continue

            # Count how many indices < j
            left_count = bisect_left(pos_list, j)

            # Count how many indices > j
            right_count = len(pos_list) - bisect_right(pos_list, j)

            # Triplets formed = left_count * right_count
            result += left_count * right_count

        return result%modulo