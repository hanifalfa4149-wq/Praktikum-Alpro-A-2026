sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2

print(sum1)
print(sum2)
print(sum3)

print()
# Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x**y)
print(x // y)

print()
# Assignment Operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print()
# Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print()
# Logical Operators
x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not (x > 3 and x < 10))

print()
# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print()
# Membership Operators
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

print()
# Bitwise Operators
print(6 | 3)

print()
# Operator Precedence
print(100 + 5 * 3)
