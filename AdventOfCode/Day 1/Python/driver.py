                # Part 1 #

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them
# together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020;
# what do you get if you multiply them together?





# Read data in as STR
number = open('numbers.txt', 'r').read().split()

# print(type(number[0]))
# print(number)

# Convert to int
numbers = []
for i in range(0, len(number)):
    numbers.append(int(number[i]))
#
# print(type(numbers[0]))
# print(numbers)

target = 0
val1 = 0
val2 = 0

while (target != 2020):
    for x in numbers:
        for y in numbers:
            if (x + y == 2020):
                # print("Target hit!: ", x , " ", y)
                target = 2020
                val1 = x
                val2 = y

print("Two numbers added to make 2020 when multiplied equals: ", val1 * val2)



                    # Part 2 #
# Using the above example again, the three entries that sum to 2020 are 979, 366,
# and 675. Multiplying them together produces the answer, 241861950.

target = 0

val1 = 0
val2 = 0
val3 = 0

while (target != 2020):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if ((x + y + z) == 2020):
                    # print (x, " ", y, " ", z)
                    val1 = x
                    val2 = y
                    val3 = z
                    target = 2020
            if (target == 2020):
                break

print("Part 2 Answer: ", (val3 * val2 * val1))