# Creating variable to store the number of words in IF
number_of_words_IF = 0

path2 = '/home/data'

# Open text file in read only mode
with open("/home/data/IF.txt",'r') as file:

    # Read content of the file and store it in a new variable
    data = file.read()

    # Split the data into separate lines
    lines = data.split()

    # Add length of the lines in our number_of_words_ IF variable
    number_of_words_IF += len(lines)

# Create variable to store the number of words in Limerick
number_of_words_Limerick = 0

# Open text file in read only mode
with open('/home/data/Limerick.txt','r') as file:

    # Read content of the file and store it in a new variable
    data = file.read()

    # Split the data into separate lines
    lines = data.split()

    # Add length of the lines in our number_of_words_ Limerick variable
    number_of_words_Limerick += len(lines)

grand_total = number_of_words_IF + number_of_words_Limerick

# Find the k most frequent words from IF.txt file
from collections import Counter

with open('/home/data/IF.txt','r') as file:

    # Read content of the file and store it in a new variable
    data = file.read()

    # Split the data into separate lines
    split_it = data.split()

    # Pass the split_it list to instance of Counter class
    Counter = Counter(split_it)

    # most_common() produces k frequently encountered input values and their respective counts
    most_occur = Counter.most_common(3)

# Find text files inside directory
import glob
import os

os.chdir(r'/home/data')
text_files = glob.glob('*.txt')

# Find IP address of my machine
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Print information inside results.txt at location: /home/output/
path = '/home/output/results.txt'
results = open(path, "a")
print("The text files at location: /home/data are: ", text_files, file = results)
print("The total number of words in the IF.text file is: ", number_of_words_IF, file = results)
print("The total number of words in the Limerick.text file is: ", number_of_words_Limerick, file = results)
print("The total number of words in both files is: ", grand_total, file = results)
print("The top 3 words with maximum nuber of counts in IF.txt is: ", most_occur, file = results)
print("Your computer IP Address is: ", IPAddr, file = results)
results.close()


print("The text files at location: /home/data are: ", text_files)
print("The total number of words in the IF.text file is: ", number_of_words_IF)
print("The total number of words in the Limerick.text file is: ", number_of_words_Limerick)
print("The total number of words in both files is: ", grand_total)
print("The top 3 words with maximum nuber of counts in IF.txt is: ", most_occur)
print("Your computer IP Address is: ", IPAddr)

