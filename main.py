nums = [7,5,6,8,3]
nums.sort()
a = nums[-1]
b = nums[0]
while b:
    a, b = b , a % b
print(a)