##remember to call all functions in order for them to run
##remember to INDENT.. (WHITE SPACES MATTER)

## A function named hello() that prints a greeting to the user, 
## This function should accept no arguments and returns nothing.

def hello():
    print("Hey, What's Up!!")

hello()



## A function named pack() that accepts three arguments, and returns a single list with the 
#three arguments inside as list elements
def pack(first_name, last_name, birthdate, age ):
    return [first_name, last_name, birthdate, age]

print(pack("Austi", "Belaire", "Oct 7", 28))




## A function called eat_lunch(). This function should accept a list of any length and print out a series of strongs 
## that say "First I eat__"(1st element of the list)
## and "Next I eat __" (following elements of the list).
## If the list is empty, print "My lunchbox is empty!". Function should not return anything
