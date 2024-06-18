# Task 1
lst = [1, 2, 3, 4, 5]
print("Task 1:",lst[0], lst[2], lst[:3])

# Task 2
city_list = ["Ростов", "+", "на", "-", "Дону"]
city_list[1] = "-"
print("Task 2:","City name:", city_list[0], city_list[1], city_list[2], city_list[3], city_list[4])

# Task 3
list = ["a", "s", "1", "a", "32", "23"]
letters_list = [char for char in list if char.isalpha()]
numbers_list = [char for char in list if char.isdigit()]
print("Task 3:","Letters list:", letters_list)
print("Task 3:","Numbers list:", numbers_list)

# Task 4
letters_list.pop()
letters_list.reverse()
print("Task 4:","Modified letters list:", letters_list)

# Task 5
set_list = set(list)
print("Task 5:","Set from the list:", set_list)

