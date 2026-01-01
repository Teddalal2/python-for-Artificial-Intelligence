🚀 Comprehensions in Python (Create Great One-Liners
var = 'A' if condition else 'B'

1️⃣ If Statement Comprehension
toggle = False
if toggle:
    word = 'Enabled'
else:
    word = 'Disabled'

word = 'Enabled' if toggle else 'Disabled'
print(word)

2️⃣ List Comprehensions

items = ['item1', 'item2', 'item3']

upper_items = []
for item in items:
    upper_items.append(item.upper())
print(upper_items)
# The same
upper_items = [item.upper() for item in items]
print(upper_items)

3️⃣ List Comprehension with Conditions
items = ['item1', 'item2', 'item3', 'Wrong_data']

upper_items = []
for item in items:
    if 'item' in item:
        upper_items.append(item.upper())
print(upper_items)

upper_items = [item.upper() for item in items if 'item' in item]
pper_itemsl = [item.lower() for item in items if 'item' in item]
pper_itemsi = [item.isspace() for item in items if 'item' in item]
print(upper_items)
print(pper_itemsl)
print(pper_itemsi)

4️⃣ Exercise with List Comprehensions

numbers = [1,2,3,4,5]
num_sq =        [num**2 for num in numbers]
num_cube =      [num**3 for num in numbers]
num_cube_even = [num**3 for num in numbers if num%2 == 0]
print(num_sq)
print(num_cube)
print(num_cube_even)

mats = ['wood', 'steel', 'concrete', 'bricks', 'glass', 'plaster']

mats = [mat for mat in mats if 's' in mat]
print(mats)

5️⃣ Dict Comprehensions
mats        = ['wood', 'steel', 'concrete', 'bricks', 'glass', 'plaster']
dict_mats = {mat.lower():mat.upper() for mat in mats}
print(dict_mats)

