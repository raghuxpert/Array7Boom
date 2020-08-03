n = 0
def methoda():
    global n
    n+=1
    return n

itr = iter(methoda,5)

print(itr)
print(next(itr))
####################################

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)
print(i)
print(next(i))
print(next(i))
print(next(i))