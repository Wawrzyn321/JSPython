"""
80
Napisz  skrypt  python obliczający  sumę, wartość średnią
i  medianę podanych z klawiatury liczb całkowitych.
"""

def suma(nums):
    s = 0
    for i in nums:
        s += i
    return s

def srednia(nums):
    return suma(nums) / len(nums)

def mediana(nums):
    numsSorted = sorted(nums)
    if len(numsSorted) % 2 == 0:
        return (numsSorted[int(len(numsSorted)/2)] +
                numsSorted[int(len(numsSorted)/2)+1])/2
    else:
        return numsSorted[int(len(numsSorted)/2)]

print("wprowadzaj liczby lub zakończ 'q'")
nums = []
while True:
    v = input()
    if v == 'q':
        break
    nums.append(int(v))

print(suma(nums))
print(srednia(nums))
print(mediana(nums))
