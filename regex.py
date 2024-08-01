import re

t1 = "abc123"
t2 = "456xyz"
t3 = "a_b c!"
t4 = "789abcxyz"
t5 = "abc xyz"
t6 = "no_digits_here"

print("Sample text")
print(t1,t2,t3,t4,t5,t6)
print()

print("All digits in each sample text")
print(t1,":",re.findall(r'\d',t1))
print(t2,":",re.findall(r'\d',t2))
print(t3,":",re.findall(r'\d',t3))
print(t4,":",re.findall(r'\d',t4))
print(t5,":",re.findall(r'\d',t5))
print(t6,":",re.findall(r'\d',t6))
print()

print("All non digits in each sample text")
print(t1,":",re.findall(r'\D',t1))
print(t2,":",re.findall(r'\D',t2))
print(t3,":",re.findall(r'\D',t3))
print(t4,":",re.findall(r'\D',t4))
print(t5,":",re.findall(r'\D',t5))
print(t6,":",re.findall(r'\D',t6))
print()

print("All alphanumeric and underscores in each sample text")
print(t1,":",re.findall(r'\w',t1))
print(t2,":",re.findall(r'\w',t2))
print(t3,":",re.findall(r'\w',t3))
print(t4,":",re.findall(r'\w',t4))
print(t5,":",re.findall(r'\w',t5))
print(t6,":",re.findall(r'\w',t6))
print()

print("All non word characters in each sample text")
print(t1,":",re.findall(r'\W',t1))
print(t2,":",re.findall(r'\W',t2))
print(t3,":",re.findall(r'\W',t3))
print(t4,":",re.findall(r'\W',t4))
print(t5,":",re.findall(r'\W',t5))
print(t6,":",re.findall(r'\W',t6))
print()

print("All whitespace characters in each sample text")
print(t1,":",re.findall(r'\s',t1))
print(t2,":",re.findall(r'\s',t2))
print(t3,":",re.findall(r'\s',t3))
print(t4,":",re.findall(r'\s',t4))
print(t5,":",re.findall(r'\s',t5))
print(t6,":",re.findall(r'\s',t6))
print()

print("All non-whitespace characters in each sample text")
print(t1,":",re.findall(r'\S',t1))
print(t2,":",re.findall(r'\S',t2))
print(t3,":",re.findall(r'\S',t3))
print(t4,":",re.findall(r'\S',t4))
print(t5,":",re.findall(r'\S',t5))
print(t6,":",re.findall(r'\S',t6))
print()

print("All lines that start with \"abc\" in each sample text")
print(t1,":",re.findall(r'^abc',t1))
print(t2,":",re.findall(r'^abc',t2))
print(t3,":",re.findall(r'^abc',t3))
print(t4,":",re.findall(r'^abc',t4))
print(t5,":",re.findall(r'^abc',t5))
print(t6,":",re.findall(r'^abc',t6))
print()

print("All lines that end with \"xyz\" in each sample text")
print(t1,":",re.findall(r'xyz$',t1))
print(t2,":",re.findall(r'xyz$',t2))
print(t3,":",re.findall(r'xyz$',t3))
print(t4,":",re.findall(r'xyz$',t4))
print(t5,":",re.findall(r'xyz$',t5))
print(t6,":",re.findall(r'xyz$',t6))

