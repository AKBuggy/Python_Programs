from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            exit()

        return self.buffer.pop()

    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)





def binary_number(n):
    queue_for_binary = Queue()
    queue_for_binary.enqueue("1")

    for i in range(n):
        front = queue_for_binary.front()
        print("   ", front)
        queue_for_binary.enqueue(front + "0")
        queue_for_binary.enqueue(front + "1")

        queue_for_binary.dequeue()


if __name__ == '__main__':
    binary_number(10)



