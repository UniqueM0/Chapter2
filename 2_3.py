# print("chapter 2_3")

from os import sep


# print("one","two","three", sep=",")

# print("Hello", end=" ")
# print("World!")

# print("01234567890123456")
# print("a\tb\tc") #a     b      c
# print("a\tb\tc".expandtabs(5))  #a     b     c
# print("Nudge, \tnudge, \nwink, \twing.".expandtabs(11))  #11Spaces inbetween     
 
print("012345678901234567")
print("rank".ljust(5), "player".ljust(20), "HR".rjust(3), sep="")
print('1'.center(5), "barry_bonds".ljust(20),"762".rjust(3),sep="")
print('2'.center(5),"hank_aaron".ljust(20), "755".rjust(3), sep="")
print('3'.center(5), "babe_ruth".ljust(20), "714".rjust(3), sep="")