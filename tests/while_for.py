numbers = [3, 17, 5, 42, 8, 1, 99, 23, 11]

current_max = numbers[0]
for num in numbers:
    if num > current_max:
        current_max = num

print(f"Максимум: {current_max}")