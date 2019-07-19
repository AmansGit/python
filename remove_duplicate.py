# Remove the 2nd item of duplicate numbers from the list

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniq = []
for number in numbers:
    if number not in uniq:
        uniq.append(number)
print(uniq)
