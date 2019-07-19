#   Remove the 1st item of duplicate numbers from the list 



numbers = [2, 2, 4, 6, 3, 4, 6, 1]

for items in numbers:
    a = numbers.count(items)
    if a > 1:
        numbers.remove(items)
print(numbers)  

