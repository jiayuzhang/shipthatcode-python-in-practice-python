from __future__ import annotations
from collections import defaultdict
import csv
import io

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

# text = input()
# tokens = text.split(" ")
# counter = {}
# for token in tokens:
#     counter[token] = counter.get(token, 0) + 1
# for key, value in counter.items():
#     print(key, value)


# n = int(input())
# grades = defaultdict(list)
# for i in range(n):
#     text = input()  # Alice A
#     name, grade = text.split(" ")
#     grades[grade].append(name)

# for key, value in grades.items():
#     print(key + ":", ", ".join(value))

# line1 = input()
# line2 = input()
# nums1 = {int(x) for x in line1.split(" ")}
# nums2 = {int(x) for x in line2.split(" ")}
# intersection = sorted(nums1 & nums2)
# print(" ".join(map(str, intersection)))


# def is_palindrome(sentence: str) -> bool:
#     sentence = sentence.lower().replace(" ", "").strip()
#     return sentence == sentence[::-1]


# sentence = input()
# if is_palindrome(sentence):
#     print("yes")
# else:
#     print("no")


# n = int(input())
# nums = [float(input()) for _ in range(n)]


# def average(*nums):
#     avg = sum(nums) / len(nums)
#     print(f"{avg:.2f}")


# average(*nums)

# n = int(input())
# lst = []
# for _ in range(n):
#     text = input()
#     name, score = text.split(" ")
#     score = int(score)
#     lst.append((name, score))

# lst.sort(key=lambda x: -x[1])
# for name, _ in lst:
#     print(name)

# num1 = input()
# num2 = input()
# try:
#     result = int(num1) / int(num2)
#     print(round(result, 2))
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("invalid input")

# n = int(input())

# def validate_age(years):
#     if years < 0:
#         raise ValueError("age must be non-negative")
#     if years > 150:
#         raise ValueError("age too large")
#     return years


# try:
#     validate_age(n)
#     print("age ok")
# except ValueError as e:
#     print(e)

lines = []
input()  # headers
n = int(input())
for _ in range(n):
    lines.append(input())
csv_data = "\n".join(lines)
reader = csv.reader(io.StringIO(csv_data))
tot = 0
for row in reader:
    # print(row)
    tot += float(row[-1])
print(f"{tot / n:.2f}")
