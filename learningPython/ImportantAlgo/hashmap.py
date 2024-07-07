class Hashmap:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # to set a value in hashmap

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[idx] = (key, val)
        else:
            bucket.append((key, val))

    # to get the value from the hashmap

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No records found"

    # to delete an item from hashtable

    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(idx)
            # the reason we are returning here is that sometimes user way try to delete the key which is not present.
        return

    # to print the object nice format we can make use of __str__ or __repr__ which are called magic methods.
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    # implement __repr__ for extra info
    def __repr__(self):
        output = [[0]] * self.size
        for item in self.hash_table:
            output.append(item)
        return "".join(str(output))


hash_table = Hashmap(10)
hash_table.set_val("0", "Ankit")

# hash_table.del_val("0")
# print(hash_table)

hash_table.set_val("1", "Jalaja")
# print(hash_table)
#
# print(hash_table.get_val("1"))

hash_table.set_val("2", "Prakash")
hash_table.set_val("3", "Aniket")
print(repr(hash_table))

