# print("Hello_There")

# print("{0:10d}".format(12345678))
# print("{0:10,d}".format(12345678))
# print("{0:10.2f}".format(1234.5678))
# print("{0:10,.2f}".format(1234.5678))
# print("{0:10,.3f}".format(1234.5678))
# print("{0:10.2%}".format(12.345678))
# print("{0:10,.3%}".format(12.34569))

# print("The area of {0:s} is {1:,d} square miles.".format("Texas",268820))
# str1 = "The population of {0:s} is {1:.2%} of the U.S. Population."
# print(str1.format("Texas", 2)) 

# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3
# # print ("Sum is {}".format(sum_of_all_numbers))
# print("Sum is {0:n}".format(sum_of_all_numbers))

# # list_of_numbers = [1, 10,1000]
# # print(sum(list_of_numbers))

# # list_of_numbers =[1,23,56,78]
# # print(list_of_numbers.count(23))

# # list_of_numbers = [1, 10, 1000]
# # print(list_of_numbers)
# # list_of_numbers.clear()
# # print(list_of_numbers)
# # list_of_numbers.append(100)
# # print(list_of_numbers)

# list_of_numbers = [1, 10, 1000]
# print(list_of_numbers)
# list_of_numbers.clear()
# print(list_of_numbers)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# print(list_of_numbers)

# list_of_numbers2 = [3, 100, 5]
# list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers)

# l1 = [1, 32, 4]
# l2 = [100, 200, 300]
# l3 = l1 +l2 
# print(l3)

# words = ["Spam", "wink", "Hi"]
# words.insert(1, "Hello")

# print("Words======>", words)

## Calculate average of grades
grades = [] # create the variable grades and assign it the empty list 
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)

minimum_grade = min(grades)
grades.remove(minimum_grade)
minimum_grade = min(grades)
grades.remove(minimum_grade)
average = sum(grades) / len(grades)
print("Average Grade: {0: .2f}".format(average))