s = input("Enter the string: ")
max_char = s[0]
max_count = 0
for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_char = i
print("Highest occurring character:", max_char)
print("Occurrence count:", max_count)
