n = int(input())
nums = [int(input()) for _ in range(n)]
# Find and print the second largest unique value

nums = list(set(nums))
nums.sort()
print(nums[-2])
