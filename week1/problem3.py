s = input("Enter a string with lowercase characters: ")
longest = s[0]
string = s[0]

for letter in s[1:]:
    if letter >= string[-1]:
        string += letter
        if len(string) > len(longest):
            longest = string
    else:
        if len(string) > len(longest):
            longest = string
        string = letter

print(longest)
