#1. The data we need to retrieve 
#2. The total no of votes cast
#3. A complete list of candidates who received votes
#4. The percentage of votes each candidate won
#5. The total number of votes each candidate won
#6. The winner of election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)   

# Print each row in the CSV file.
    #for row in file_reader:
        #print(row)     

 # Print the file object.
     #print(election_data)   

# Print the header row.
    headers = next(file_reader)
    print(headers)     

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the with statement open the file as a text file.
#outfile = open(file_to_save,"w")     
# Write some data to the file.
#outfile.write("Hello World!")
# Close the file
#outfile.close()
# the above code worked for writing in our file with open() and close ()

# To make the above code cleaner we will write it using with

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open (file_to_save,"w") as txt_file:

 # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")   

  # Write three counties to the file method 2
     #txt_file.write("Arapahoe, Denver, Jefferson")     

   # Write three counties to the file.
     txt_file.write("Counties in the election\n------------------------------------\nArapahoe\nDenver\nJefferson")     