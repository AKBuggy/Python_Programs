from collections import deque

# q = deque()
#
# q.appendleft(44)
# q.appendleft(23)
# q.appendleft(51)
#
# print(q.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'Company': 'Wall Mart',
    'Timestamp': '15 Apr 11.01 AM',
    'Price': 131.10
})

pq.enqueue({
    'Company': 'Wall Mart',
    'Timestamp': '15 Apr 11.02 AM',
    'Price': 132
})

pq.enqueue({
    'Company': 'Wall Mart',
    'Timestamp': '15 Apr 11.03 AM',
    'Price': 133
})

print(pq.buffer)
print(pq.size())
print(pq.dequeue())
print(pq.buffer)
print(pq.size())
