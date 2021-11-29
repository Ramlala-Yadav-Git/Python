# converting one data type to another data type

# Implicit type conversion done by python itself
print("Implicit")
print(5/2)  # integer to float

print("ram" + "syam")  # concatination but not data conversion

# print("ram" + 1)  error will be shown


# Explicit type conversion
print("explicit")
n = 10
print(int(n))
print(float(n))
print(complex(n))
print(str(n))
# print(list(n))  error n is not iterable
# print(tuple(n))  error n is not iterable
print(bin(n))
print(oct(n))
print(hex(n))
