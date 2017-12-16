"""
80, ale krócej.
"""

import statistics

print("wprowadzaj liczby lub zakończ 'q'")
nums = []
while True:
    v = input()
    if v == 'q':
        break
    nums.append(int(v))

print(sum(nums))
print(statistics.mean(nums))
print(statistics.median(nums))
