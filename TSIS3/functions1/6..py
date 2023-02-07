def reverse(s1):
    words = s1.split(' ')
    joined_str = ' '.join(reversed(words)) #Reverse the created list using 
    #the reversed() function and add them to a new string using the join() string function.
    return joined_str

s2 = str(input())
print(reverse(s2))