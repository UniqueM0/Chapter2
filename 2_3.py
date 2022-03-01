# print("chapter 2_3")

from os import sep


# print("one","two","three", sep=",")

# print("Hello", end=" ")
# print("World!")

# print("01234567890123456")
# print("a\tb\tc") #a     b      c
# print("a\tb\tc".expandtabs(5))  #a     b     c
# print("Nudge, \tnudge, \nwink, \twing.".expandtabs(11))  #11Spaces inbetween     
 
# print("012345678901234567")
# print("rank".ljust(5), "player".ljust(20), "HR".rjust(3), sep="")
# print('1'.center(5), "barry_bonds".ljust(20),"762".rjust(3),sep="")
# print('2'.center(5),"hank_aaron".ljust(20), "755".rjust(3), sep="")
# print('3'.center(5), "babe_ruth".ljust(20), "714".rjust(3), sep="")

# print("(0)".format(10))

# print("There are {0}% probability that the stock market will crash tomorrow".format(10))

# str1= "There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally"
# print (str1.format(10,50))

# print("{0:^5s} {1:20s} {2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n} {1:<20s} {2:>3n}".format(1,"Barry Bonds",762))

print("The area of {0:s} is {1: ,d} square miles.".format ("Texas", 268820))
str1 = "The population of  {0:s} is {1:.2%} of the U.S. population."
print(str1.format("Texas", 26448000 / 309000000))  