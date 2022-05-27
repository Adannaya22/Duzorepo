str1 = "Pin"
str2 = "Nip"

# convert both the strings into lowercase
str1 = str1.lower()
str2 = str2.lower()

# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " true.")
    else:
        print(str1 + " and " + str2 + " false.")

else:
    print(str1 + " and " + str2 + " false.")