# nums = [1,2,3,4,5,6,7,8]
# step = 1
# subsets = []
# while len(nums) != 0:
#     if len(nums) >= step:
#         subsets.append(nums[0:step])
#         nums = nums[step:]
#         step += 1
#     else:
#         print(False)
# print(subsets)

# Using tuples as keys for coordinates
data_dict = {(0, 0): 100, (1, 2): 200, (2, 1): 300}
coordinates = (1, 2)
value = data_dict[coordinates] # value will be 200