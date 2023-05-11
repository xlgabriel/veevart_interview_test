import random

# Create elements list
elements = []

# Iterate to randomly add new elements to the list
for i in range(random.randint(2, 16)):
    # Append a random number betweeen 1 and 99 in the elements list
    elements.append(random.randint(1, 99))
    # Rearrange items from largest to smallest
    # elements.sort(reverse=True)

print("Elements:", elements)


# This function adds to the final array each element of the split arrays,
# always starting from the smallest number
def combine(arr2_1, arr2_2, n):
    finalarray = []
    i1 = i2 = 0

    # Iterate n times, being n the elements length
    for i in range(n):
        # Check if the length
        if i1 >= len(arr2_1) or i2 >= len(arr2_2):
            if i1 >= len(arr2_1):
                finalarray.append(arr2_2[i2])
                i2 = i2 + 1
            else:
                finalarray.append(arr2_1[i1])
                i1 = i1 + 1
        else:
            if arr2_1[i1] < arr2_2[i2]:
                finalarray.append(arr2_1[i1])
                i1 = i1 + 1
            else:
                finalarray.append(arr2_2[i2])
                i2 = i2 + 1

    print("sorting:", finalarray)
    return finalarray


def mergesort(elements):
    if len(elements) > 1:
        mid = len(elements) // 2
        s_arr2_1 = elements[:mid]
        s_arr2_2 = elements[mid:]
        print(s_arr2_1, s_arr2_2)

        sorted_sarr1 = mergesort(s_arr2_1)
        sorted_sarr2 = mergesort(s_arr2_2)
        return combine(sorted_sarr1, sorted_sarr2, len(elements))
    return elements


mergesort(elements=elements)
