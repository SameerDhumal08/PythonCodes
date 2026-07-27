# Create an empty stack
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Peek (top element)
print("Top element:", stack[-1])

# Pop element
removed = stack.pop()
print("Popped element:", removed)

print("Stack after pop:", stack)

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
