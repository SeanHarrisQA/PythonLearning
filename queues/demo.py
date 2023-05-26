from Queue import Queue
import time
import threading

# Food ordering exercise

order_queue = Queue()

new_orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(orders):
    for order in orders:
        print("Placing order for:", order)
        order_queue.enqueue(order)
        time.sleep(0.5)


def serve_order():
    while not order_queue.is_empty():
        print("Now Serving:", order_queue.dequeue())
        time.sleep(2)

producer_thread = threading.Thread(target=place_order, args=(new_orders,))
consumer_thread = threading.Thread(target=serve_order)

producer_thread.start()
time.sleep(1)
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

# Binary exercise

def print_binary(count):
    binary_numbers = Queue()
    binary_numbers.enqueue("1")
    while count > 0 :
        binary_numbers.enqueue(binary_numbers.front() + "0")
        binary_numbers.enqueue(binary_numbers.front() + "1")
        print(binary_numbers.dequeue())
        count-=2
    for x in range(binary_numbers.size() + count - 1):
        print(binary_numbers.dequeue())


print_binary(10)