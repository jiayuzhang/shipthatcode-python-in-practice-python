n = int(input())
nums = [int(input()) for _ in range(n)]
# # Find and print the second largest unique value

# nums = list(set(nums))
# nums.sort()
# print(nums[-2])

res = [x * 2 for x in nums if x % 2 == 0]
for n in res:
    print(n)
