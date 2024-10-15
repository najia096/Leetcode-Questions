'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

leetcode link: https://leetcode.com/problems/two-sum/description/
'''

'''
Time Complexity = O(n)
Space Complexity = O(n)
'''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #this hashmap seen will store the indices of each num

        for i, num in enumerate(nums):
            dif = target - num
            if dif in seen:
                return [seen[dif], i]
            seen[num] = i

        
