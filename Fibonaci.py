def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for i in nums:
        yield i**2

s = square(fibonacci_numbers(5))

for i in s:
    print(i)
