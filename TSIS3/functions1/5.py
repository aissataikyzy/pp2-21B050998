def permutation(string, i = 0):

    # if we've gotten to the end, print the permutation
    if i == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for j in range(i, len(string)):

        # copy the string (store as array)
        copy = [character for character in string]

        # swap the current index with the step
        copy[i], copy[j] = copy[j], copy[i]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutation(copy, i + 1)

print(permutation(str(input())))