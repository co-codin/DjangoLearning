numbers = [2,2,3,4,5,5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)