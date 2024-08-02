# reverse the string

str1 = "Learning python is easy"
result = " "
for ele in str1:
    result = ele + result

print(result)

# reverse each word in string

s1 = "learning python is very easy"
l = s1.split()
l1 = []
for ch in l:
    l1.append(ch[::-1])
output = ' '.join(l1)
print(output)
