import datetime
import csv
import calendar


##########
## 
##  Written by David Brendlinger in June of 2023
##  Secu Calender for Server Opperations team patching
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
    
    return numbers_list  
    # Iterate over the list and display each number
 ##   for num in numbers_list:
 ##       print(num)


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


def read_file_patches2():
    data = []
    with open('patches.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({
                'PTOFFSET': row['PTOFFSET'],
                'MILTIME': row['MILTIME'],
                'SUMMARY': row['SUMMARY'],
                'DESCRIPTION': row['DESCRIPTION'],
            })
    return data

## patches_data = read_file_patches2()
## for patch in patches_data:
##     print(patch)






##########
## 
## GPTChat:
## Write a python function to get the year and month passed to it and it will return a list of patch tuesdays ( second tuesday of the month ) 
##
## How to call function: 
## patch_tuesday = get_patch_tuesdays(2034, 7)
## print(f" Patch Tuesday falls on {patch_tuesday}.")
##
##########

def get_patch_tuesdays(year, month):
    # Get the matrix representing the month's calendar
    month_calendar = calendar.monthcalendar(year, month)

    # Tuesdays are the 2nd index (starting from 0) in each week
    # If the first day of the month is a Wednesday or later, the second Tuesday will be in the second week.
    # Otherwise, it'll be in the third week.
    patch_tuesday = month_calendar[1][1] if month_calendar[0][1] else month_calendar[2][1]

    return patch_tuesday

## patch_tuesday = get_patch_tuesdays(2034, 7)
## print(f"Patch Tuesday falls on {patch_tuesday}.")

##########
##    
##  Starting coding db230606    
## 
##########   



year = ask_year()
numbers_list = get_and_display_months()

for num in numbers_list:
        patch_tuesday = get_patch_tuesdays(year,num)
        print( "pt",patch_tuesday, "year",year,"month",num)
        patches_data = read_file_patches2()
        for patch in patches_data:
             # print(patch)
             pt_offset = patch['PTOFFSET']
             mil_time = patch['MILTIME']
             summary = patch['SUMMARY']
             description = patch['DESCRIPTION']
             print(f"PTOFFSET: {pt_offset}")
             print(f"MILTIME: {mil_time}")
             print(f"SUMMARY: {summary}")
             print(f"DESCRIPTION: {description}")
             print("--- End of patch ---")





   
   