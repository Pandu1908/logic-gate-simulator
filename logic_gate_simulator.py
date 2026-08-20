def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a

a = int(input("Enter A (0/1): "))
b = int(input("Enter B (0/1): "))

print("AND =", AND(a, b))
print("OR  =", OR(a, b))
print("NOT A =", NOT(a))
print("NOT B =", NOT(b))
