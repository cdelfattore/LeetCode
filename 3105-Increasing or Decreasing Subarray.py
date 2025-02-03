nums = [1,10,10]

i = 1
d = 1
m = 1
for n in range(1, len(nums)):
    # print(nums[n])
    if nums[n - 1] > nums[n]:
        i = 1
        d += 1
        m = max(m, d)
        print("Decreasing")
    elif nums[n - 1] < nums[n]:
        i += 1
        d = 1
        m = max(m, i)
        print("Increasing")
    else:
        i = 1
        d = 1
        print("equal")
    print(m)