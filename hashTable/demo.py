# Code of hashmap without collision management

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    ht = HashTable()
    # ht.add('march 6', 120)
    # print(ht.get('march 6'))
    ht['march 6'] = 120
    # del ht['march 6']
    print(ht['march 6'])


# same above code with collision management
# method 1: chaining
# todo

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    ht = HashTable()
    # ht.add('march 6', 120)
    # print(ht.get('march 6'))
    ht['march 6'] = 120
    ht['march 6'] = 78
    ht['march :'] = 45
    # del ht['march 6']
    # print(ht['march 6'])
    print(ht.arr)
