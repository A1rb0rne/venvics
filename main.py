import datetime
import csv


##########
## 
##
##
##
##########

##########
## 
## Magic to push to github:
## git add <name> 
## git commit -m "functions added year and months"
## git push -u origin main
##
##########


##########
## 
##  GPChat:  In python, write a function that suggests the current year but asks for the year.  
##  year = ask_year()
##  
##########

def ask_year():
    current_year = datetime.datetime.now().year
    year = input(f"Enter a year (Press enter to default to current year {current_year}): ")
    if not year:
        year = current_year
    else:
        # Make sure the input is a valid year
        try:
            year = int(year)
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            return ask_year()
    return year


##########
## 
##  GPTchat: Write a function that asks for a series of numbers seperated by commas.  Save the info as a list but iterate the list showing each value 
##  get_and_display_months()
##
##  This may be the magic for all this code
##  for num in numbers_list:
##      print(num)
##
##########

def get_and_display_months():
    # Ask for numbers
    numbers_str = input("Enter a series of numbers separated by commas: ")
    
    # Split the input string into a list of strings
    numbers_str_list = numbers_str.split(',')
    
    # Convert the list of strings into a list of integers
    numbers_list = [int(num_str) for num_str in numbers_str_list]
    
    # Iterate over the list and display each number
    for num in numbers_list:
        print(num)


##########
## 
## GPTChat:
## Write a python function to read a file. the file uses a csv with headers.  
## I want the following values:  PTOFFSET: MILTIME: SUMMARY:  DESCRIPTION:.  
## Name my file patches.csv
## Also give me an example of the patches.csv 
##
## read_file_patches()
##
## I need to output patch times from offset, miltime, year and month.   
##
##########

def read_file_patches():
    with open('patches.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            pt_offset = row['PTOFFSET']
            mil_time = row['MILTIME']
            summary = row['SUMMARY']
            description = row['DESCRIPTION']
            print(f"PTOFFSET: {pt_offset}, MILTIME: {mil_time}, SUMMARY: {summary}, DESCRIPTION: {description}")




## test   

Dave was here !!



## note to self, patch tuesday finder !!