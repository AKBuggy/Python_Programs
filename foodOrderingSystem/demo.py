import threading
from collections import deque
from time import sleep


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty!!")
            exit()

        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_order_queue = Queue()


def place_order(orders):
    for order in orders:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        sleep(0.5)


def serve_order():
    sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving:", order)
        sleep(2)


if __name__ == '__main__':
    orders_of_user = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_order, args=(orders_of_user,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()
