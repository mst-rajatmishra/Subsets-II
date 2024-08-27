from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset path to the result
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include the current number in the subset
                path.append(nums[i])
                # Move on to the next number
                backtrack(i + 1, path)
                # Backtrack by removing the last number added
                path.pop()
        
        # Sort the array to handle duplicates
        nums.sort()
        result = []
        backtrack(0, [])
        return result

# Example usage:
sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(sol.subsetsWithDup([0]))        # Output: [[], [0]]
