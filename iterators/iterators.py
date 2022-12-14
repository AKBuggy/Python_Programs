class RemoteControl:
    def __init__(self):
        self.channel = [7.9, 5.4, 9.75, 10]
        # self.channel = ["HBO", "CNN", "abc", "espn"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channel):
            raise StopIteration

        return self.channel[self.index]


r = RemoteControl()

# Method 1 to iterate through list using iter

# itr = iter(r)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# Method 2 to iterate through list

# r.__iter__()
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())

# Method 3 to iterate through list using for loop

r.__iter__()
for i in range(0, len(r.channel)):
    print(r.__next__())
