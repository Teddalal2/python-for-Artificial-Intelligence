# 🚀 Comprehensions in Python (Create Great One-Liners
var = 'A' if condition else 'B'

# 1️⃣ If Statement Comprehension
toggle = False
if toggle:
    word = 'Enabled'
else:
    word = 'Disabled'

word = 'Enabled' if toggle else 'Disabled'
print(word)

# 2️⃣ List Comprehensions

items = ['item1', 'item2', 'item3']

upper_items = []
for item in items:
    upper_items.append(item.upper())
print(upper_items)
# The same
upper_items = [item.upper() for item in items]
print(upper_items)
