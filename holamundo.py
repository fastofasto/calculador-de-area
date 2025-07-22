a =10
b = 0
try:
    c = a/b
    print (c)
except ZeroDivisionError:
    c = 0
    print(c)
print(c)