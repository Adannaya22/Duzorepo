# Program to write to text file using write() function
with  open("txt.py", "w") as file:
         content = "Hello World"
         file.write(content)
         file.close()


# Program to read the entire file (absolute path) using read() function
with  open("c:/Users/nwauz/Documents/txt.py", "r") as file:
         content = file.read()
         print (content)
         file.close()


def word_count(str):
    # Create an empty dictionary
    counts = dict()
    words = str.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# get input from user
string = input("Please enter sentence: ")

# Print the number of occurrences of word
print( word_count(string))
