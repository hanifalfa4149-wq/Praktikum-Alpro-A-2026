thislist = ["apple", "banana", "cherry"]
print(thislist)

print()
# Access List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print()
# Change Item Values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print()
# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print()
# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "banana" in thislist:
    print("Yes, 'banana' is in the fruits list")

print()
# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print()
# Add Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print()
# Remove Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print()
# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print()
# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print()
# List Methods
thislist = ["apple", "banana", "cherry"]
thislist.sort()
print(thislist)

print()
# List Comprehension
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)

print()
# Nested Lists
mylist = [["apple", "banana", "cherry"], [1, 2, 3, 4, 5]]
print(mylist[1][2])

print()
# List Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print()
# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print()
# Delete the List
thislist = ["apple", "banana", "cherry"]
del thislist
try:
    print(thislist)
except NameError:
    print("The list has been deleted and is no longer defined.")

# Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)
