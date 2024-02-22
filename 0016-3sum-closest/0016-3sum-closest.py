class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if abs(total_sum - target) < abs(closest_sum - target):
                    closest_sum = total_sum

                if total_sum < target:
                    left += 1
                elif total_sum > target:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
