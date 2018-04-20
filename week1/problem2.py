s = input("Enter a string: ")
bob = 0

if "bob" in s:
    for n in range(len(s)):
        if s[n:n+3] == 'bob':
            bob += 1

print("Number of times bob occurs is:", bob)
