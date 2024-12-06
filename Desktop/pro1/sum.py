# class Solution(object):
#     def twoSum(self, nums, target):
#         inde_of_two_num = []
        
#         for i in range(len(nums)):
#             second_num = target - nums[i]
#             if second_num in nums:
#                 first_num_index = nums.index(nums[i])
#                 second_num_index = nums.index(second_num)
#                 inde_of_two_num.append(first_num_index)
#                 if second_num_index in inde_of_two_num:
#                     return 
#                 else:
#                     inde_of_two_num.append(second_num_index)
#                     return inde_of_two_num
        
    

# object1 = Solution()
# print(object1.twoSum([3,2,4] , 6));
# class Solution(object):
#     def twoSum(self, nums, target):
#         inde_of_two_num = []
        
#         for i in range(len(nums)):
#             second_num = target - nums[i]
#             if second_num in nums[i+1:]:  # Check in the remaining part of the list
#                 first_num_index = i
#                 second_num_index = nums.index(second_num, i + 1)  # Find the second number starting from the next index
                
#                 inde_of_two_num.append(first_num_index)
#                 inde_of_two_num.append(second_num_index)
#                 return inde_of_two_num
        
#         return "There is no number that can be added to reach that target."

# object1 = Solution()
# print(object1.twoSum([3, 2, 4], 6))  # Output should be [1, 2]




# class Solution(object):

#     def addTwoNumbers(self, l1, l2):
#       remainder = 0;
#       list_of_sum = []
#       for i in range(len(l1)):
#         s1 = l1[i] + l2[i]
#         if s1>9:
#             strsum = str(s1)
#             remainder = int(strsum[0])
#             list_of_sum.append(int(strsum[1] ))
#         else:
#             list_of_sum.append(s1+remainder)
#             remainder = 0;
#       list_of_sum.reverse()
#       return list_of_sum
      
# object1 = Solution()
# print(object1.addTwoNumbers([2, 4, 3], [5,6,4])) 
arr = [5, 3, 8, 4, 2]

for j in range(1, len(arr)):
        key = arr[j]           # Current element to be positioned
        i = j - 1               # Start comparing with the element just before it
        
        # Move elements of arr[0...j-1] that are greater than key
        # to one position ahead of their current position
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]  # Shift element to the right
            i -= 1
            print(f'this is while running {arr}')
        # Place key at its correct position
        arr[i + 1] = key
        print(arr)
print(f'this is the last array {arr}')