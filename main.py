from __future__ import annotations

# n = int(input())
# nums = [int(input()) for _ in range(n)]
# # Find and print the second largest unique value

# nums = list(set(nums))
# nums.sort()
# print(nums[-2])

# res = [x * 2 for x in nums if x % 2 == 0]
# for n in res:
#     print(n)


# def min_max(numbers) -> tuple[int, int]:
#     return min(numbers), max(numbers)

# mn, mx = min_max(nums)
# print(mn)
# print(mx)

text = input()
tokens = text.split(" ")
counter = {}
for token in tokens:
    counter[token] = counter.get(token, 0) + 1
for key, value in counter.items():
    print(key, value)
