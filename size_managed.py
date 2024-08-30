import sys
a=1000000000000000001023837689087654678976578.5
b=100000000000000000000002222222222220000000000000
print(sys.getsizeof(a))
print(sys.getsizeof(b))

c=a+b
d = 'sandeep123'
e="i"
print(sys.getsizeof(c))
print(type(e))
print(c)
print(type(a))

print(type(d))
print(sys.__doc__)