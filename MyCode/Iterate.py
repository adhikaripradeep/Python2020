num = [7,8,9,5]

print(num[3])
print('--------------')

for i in num:
    print(i)
print('--------------')

it = iter(num)
print(it.__next__())

print(next(it))

print('____________-')

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

print(values.__next__())

for i in values:
    print(i)