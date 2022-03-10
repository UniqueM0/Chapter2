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
# # list_of_numbers.append(100)
# # list_of_numbers.append(100)
# # print(list_of_numbers)

# # list_of_numbers2 = [3, 100, 5]
# # list_of_numbers.extend(list_of_numbers2)
# # print(list_of_numbers)

# # l1 = [1, 32, 4]
# # l2 = [100, 200, 300]
# # l3 = l1 +l2 
# # print(l3)

# # words = ["Spam", "wink", "Hi"]
# # words.insert(1, "Hello")

# # print("Words======>", words)

# ## Calculate average of grades
# grades = [] # create the variable grades and assign it the empty list 
# num = float(input("Enter the first grade: "))
# grades.append(num)
# # num = float(input("Enter the second grade: "))
# # grades.append(num)
# # num = float(input("Enter the third grade: "))
# # grades.append(num)
# # num = float(input("Enter the fourth grade: "))
# # grades.append(num)
# # num = float(input("Enter the fifth grade: "))
# # grades.append(num)

# # minimum_grade = min(grades)
# # grades.remove(minimum_grade)
# # minimum_grade = min(grades)
# # grades.remove(minimum_grade)
# # average = sum(grades) / len(grades)
# # print("Average Grade: {0: .2f}".format(average))

# # grades = []
# # grades.append(1)
# # grades.append(2)
# # grades.append(4)
# # grades.append(9)

# # print("Grades", grades)

# # length = len(grades)
# # print("length", length)
# # print("sliced:", grades[0:2])

# print("a,b,c".split(','))
# print("a**b**c".split('**'))
# print("a\nb\nc".split())
# print("a b c".split())

# str1 = "a,b,c"
# parts = str1.split(",")
# # # parts = "a,b,c".split(",")   #can do either one
# # print("parts: ", parts)

# # lines = ["To", "be", "or", "not", "to", "be"]

# # print("Line before join: ", lines)

# # joined = " ".join(lines)   # Depending on what is put in "" that will be the sperator 

# # print("joined: ", joined)

# #open up the Data.txt file in read mode
# # infile = open("Data.txt", 'r')

# # print("infile", infile)
# # names = []
# # for line in infile: 
# #     names.append(line.rstrip)
# #     # print("line: ", line)
# #     # print("line after striping the right side: ", line.rstrip())

# # #close the Data.tx file to preserve memory
# # infile = open
# # names_using_list_comprehension = [line.rstrip() for line in infile]
# # # print("names_using_list_comprehension: ", names_using_list_comprehension)
# # infile.close()


# infile = open("Grades.txt", "r")
# for line in infile:
#     print("line: ", line.rstrip())
# infile.close()

# infile = open("Grades.txt", "r")
# list_of_numbers = [eval(line) for line in infile]
# infile.close()


# list_of_names = ("Lucas", "John", ["A", (1, 2, 3), "C"])
# print("list_of_names", list_of_names[2][1][-1])

list1 = ["A", "B", "C"]
list2 = list(list1)
list2.append("D")
print(list1)