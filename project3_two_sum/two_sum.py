class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers we've already seen
        # Key   -> number from nums
        # Value -> index of that number
        seen = {}

        # Loop through the list with both index and value
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num

            # Check if we have already seen the complement
            if complement in seen:
                # If yes, return the index of the complement
                # and the current index
                return [seen[complement], i]

            # If not found, store the current number
            # with its index for future checks
            seen[num] = i