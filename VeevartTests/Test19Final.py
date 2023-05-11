"""Second attempt of Test 19, where an iterative structure was applied
that, through comparisons, manages to get the best value for each case"""

import random

maxcapacity = random.randint(15, 20)
# Create elements list
elements = []

# Iterate to randomly add new elements to the list
for i in range(random.randint(4, 8)):
    randomnum = random.randint(1, 10)
    # Create element with random weight and profit, respectively
    element = (randomnum, randomnum + 1)
    elements.append(element)

    # Rearrange items from largest to smallest
    elements.sort(reverse=True)


# w_max = backpack's maximum capacity
# i = current iteration
# elements = items grouped in a list
# v = acumulated weight value
# backpack = backpack with the final result
def process(w_max, i, elements, v, backpack):
    # Guarantee that items are still existing on the process
    if i >= len(elements):
        return backpack, v
    else:
        # Check if there's still space in the backpack by substracting current item to the available
        if w_max - elements[i][0] < 0:
            return process(w_max, i + 1, elements, v, backpack)
        else:
            # Apply two scenarios: packaging the item or not.
            answer1 = process(w_max, i + 1, elements, v, backpack)
            answer2 = process(
                w_max - elements[i][0],
                i + 1,
                elements,
                v + elements[i][1],
                backpack + [elements[i]],
            )
            # Check which one is the current best option in current scenario
            if answer1[1] > answer2[1]:
                return answer1
            else:
                return answer2


print("🛒 Elements:", elements)
print("🎒 Max capacity:", maxcapacity)
print("👇 Backpack and total price respectively")
print(process(maxcapacity, 0, elements, 0, []))
