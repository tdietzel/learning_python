# Warm up

# class TwoSum(object):
#   def solution(nums, target):
#     x = 0
#     for num in nums:
#       i = x
#       while i < len(nums):
#         num2 = nums[i + 1]
#         if num + num2 == target:
#           print('Number 1: ' + nums[x], 'Number 2:' + nums[i + 1])
#         i += 1
#       x += 1
#   nums = input('Enter a list of numbers separated by commas.. (1,2,3): ').split()
#   target = input('Enter a target number: ')
#   solution(nums, target)

class TwoSum(object):
  def solution(nums, target):
    nums = [int(num) for num in nums]
    finalIndex = []
    finalNums = []
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          finalIndex.append([i, j])
          finalNums.append([nums[i], nums[j]])
    return { 'Index location': finalIndex, 'Numbers found': finalNums }

  nums = input('Enter a list of numbers separated by commas.. (1,2,3): ').split(',')
  target = int(input('Enter a target number: '))
  print("~---~---~---~---~---~---~---~---~")
  print("Your Target Number: ", target)
  print(solution(nums, target))
  print("~---~---~---~---~---~---~---~---~")