"""First test, I identified with the assistance of colleagues that exceptions
where this solution is not correct exists. It is left as part of the process
of the development of the test"""

import random

maxcapacity = random.randint(15, 20)
# Create elements list
elements = []

# Iterate to randomly add new elements to the list
for i in range(random.randint(4, 8)):
    randomnum = random.randint(1, 10)
    # Create element with random weight and profit, respectively
    element = (randomnum, randomnum * 1.5)
    elements.append(element)

    # Rearrange items from largest to smallest
    elements.sort(reverse=True)

print("Elements:", elements)


def backpackresult(elements, maxcapacity):
    backpack = []
    actualusage = 0

    # sortedelements = elements[0].sort()

    # Base case
    if elements[0][0] == 0 or elements[0][1] == 0:
        return 0

    for j in range(len(elements)):
        if actualusage + elements[j][0] <= maxcapacity:
            print(
                "capacity of",
                maxcapacity - actualusage,
                "with a total of",
                maxcapacity,
            )
            backpack.append(elements[j])
            print("Added to backpack:", elements[j])
            actualusage += elements[j][0]
            print(backpack)
            print("New capacity:", maxcapacity - actualusage)

    print("Final backpack:", backpack)


backpackresult(elements=elements, maxcapacity=maxcapacity)
