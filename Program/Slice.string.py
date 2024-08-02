# using slice operator

s = input("Enter some string to reversed")

reversestring = s[::-1]
print("The string is:", reversestring)

# reverse string by using while loop

s = "Software"
output = ''
i = len(s)-1
while i >= 0:
    output = output + s[i]
    i=i-1
print(output)
