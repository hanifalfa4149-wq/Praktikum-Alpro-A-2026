"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# IF
a = 33
b = 200
if b > a:
    print("b is greater than a")

print()
# ELIF
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

print()
# ELSE
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print()
# SHORT HAND IF
a = 2
b = 330
if a < b:
    print("a is less than b")

print()
# SHORT HAND IF ELSE
a = 2
b = 330
print("A") if a > b else print("B")

print()
# AND
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

print()
# OR
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

print()
# NESTED IF
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

print()
# PASS STATEMENT
a = 33
b = 200
if b > a:
    pass
