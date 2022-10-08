# Given an array of sorted integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# ex.1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# ex. 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# def whichNums(nums, target):
#     for n in nums:
#         other_int = target - n
#         if other_int == n:
#             continue
#         elif other_int in nums:
#             return [nums.index(n),nums.index(other_int)]
# 
# print(whichNums([2,7,11,15],13))
# print(whichNums([3,2,0,4],6))

# # Dictionary Approach
# def twoSum(nums, target):
#     d = {} #value : index
#     for i in range(len(nums)):
#         pair = target - nums[i]
#         if pair in d:
#             return [d[pair], i]
#         d[nums[i]] = i
#     return

# # Two Pointer Approach
# def twopoint(List, target):
#     l = 0
#     r = len(nums) - 1
#     while l <= r:
#         if nums[l] + nums[r] == target:
#             return [l, r]
        
#         elif nums[l] + nums[r] < target:
#             # i need to find a bigger number
#             # so, move left
#             l += 1
#         else:
#             # i need to find smaller number
#             # move right
#             r -= 1
#     return "Your target is not possible to create with the numbers we have"



# import re
# 
# with open('names.txt') as file:
#     data = file.readlines()
#     for line in data:
#         try:
#             twitter = (re.search(r'\B@[a-zA-Z0-9]+', line)).group()
#             first = (re.search('\s(?P<first>[A-Z][a-z]+)', line)).group('first')
#             last = (re.search('[A-Z][a-z]+', line)).group()
#             f_l_t = f'{first} {last} / {twitter}\n'
#             print(f_l_t)
#         except:
#             continue



"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""

import re

with open('regex_test.txt') as file:
    data = file.readlines()
    for line in data:
        try:
            names = (re.search('[A-Z][a-z]+( [A-Z][a-z]*)? [A-Z][a-z]+', line)).group()
            print(names)
        except:
            print(None)