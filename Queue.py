from queue import Queue

# Create a Queue
q = Queue()

# Enqueue (Insert)
q.put(10)
q.put(20)
q.put(30)

print("Queue size:", q.qsize())

# Display front element
print("Front element:", q.queue[0])

# Dequeue (Remove)
print("Removed:", q.get())

# Display remaining elements
print("Queue after dequeue:", list(q.queue))

# Check if queue is empty
print("Is queue empty?", q.empty())
