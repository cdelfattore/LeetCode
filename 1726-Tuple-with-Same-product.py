import math
# nums = [1,2,4,5,10]
# nums = [2,3,4,6]
nums = [2,3,4,6,8,12]

m = {}
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        product = nums[i] * nums[j]
        if product in m:
            m[product] += 1
        else:
            m[product] = 1

total = 0
for frequency in m.values():
    total += 8 * ((frequency - 1) * frequency // 2)

print(total)