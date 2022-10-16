list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_element = list_numbers[0]
index = 0
for current_number in range(0, len(list_numbers)):
    if list_numbers[current_number] > max_element:
        max_element = list_numbers[current_number]
        index = current_number

a = list_numbers[-1]
list_numbers[-1] = max_element
list_numbers[index] = a

print(list_numbers)
