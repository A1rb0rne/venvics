import datetime
import csv
import calendar
import datetime


##########
## 
##  Written by David Brendlinger in June of 2023
##  Secu Calender for Server Opperations team patching
##
##########


## Set Timezones. This is to un-messup the time to align the patches by correct hour
#tz="America/New_York"
tz="America/Halifax"
#tz="America/Chicago"

## Set the ouput file name for my created .ics
ical_file_name = f"./outputicsfiles/Patches.ics"

## also note I am going to use the day prior for the DTSTAMP.  I know I need to use zulu time. 


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


##########
## 
## GPTChat:
## Write a python function to read a file. the file uses a csv with headers.  
## I want the following values:  PTOFFSET: MILTIME: SUMMARY:  DESCRIPTION:.  
## Name my file patches.csv
## Also give me an example of the patches.csv 
##
## read_file_patches2()
##
## I need to output patch times from offset, miltime, year and month.   
##
##########


def read_file_patches2():
    data = []
    with open('patches.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({
                'PTOFFSET': row['PTOFFSET'],
                'MILTIME': row['MILTIME'],
                'MILTIMEEND': row['MILTIMEEND'],
                'SUMMARY': row['SUMMARY'],
                'DESCRIPTION': row['DESCRIPTION'],
                'ORGANIZER': row['ORGANIZER'],
            })
    return data


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

##########
## 
## I am trying to create an .ical file in python.  
## Can you open a file  with the name of {year},{month}date.ical and add three lines of example text it in.  
## The date would be the date given by python in the simplest ymdhs format  
##
## create_ical_file()
##
##########



def create_ical_file():

    # Open the file in write mode
    with open( ical_file_name, 'w') as file:
        # Write the example text to the file
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        file.write("PRODID:-//Example//Calendar//EN\n")


##########
##    
##  Starting coding db230606    
## 
##########   

# Call the function to create the .ical file
create_ical_file()
year = ask_year()
numbers_list = get_and_display_months()
venvent_array = []



for num in numbers_list:
        patch_tuesday = get_patch_tuesdays(year,num)
        #print( "pt",patch_tuesday, "year",year,"month",num)
        patches_data = read_file_patches2()
        for patch in patches_data:
             # print(patch)
             pt_offset = patch['PTOFFSET']
             mil_time = patch['MILTIME']
             mil_timeend = patch['MILTIMEEND']
             organizer = patch['ORGANIZER']
             summary = patch['SUMMARY']
             description = patch['DESCRIPTION']
             realday=int(patch_tuesday)+int(pt_offset)
             realdtstamp=int(patch_tuesday)+int(pt_offset)-int(1)
             #print( f"year {year}, month {num}, day {patch_tuesday}, ptoffset {pt_offset}, realday {realday} miltime {mil_time} summary {summary} discription {description} realdtstamp {realdtstamp}   "   )
             venventline01 = "BEGIN:VEVENT\n"
             venventline02 = "UID:uid1@ncsecu.com\n"
             venventline03 = "DTSTAMP:{}{:02d}{:02d}T190000Z\n".format(year, num, realdtstamp)
             venventline04 = "ORGANIZER;CN={}:mailto:x@y.com\n".format(organizer)
             venventline05 = "DTSTART;TZID={}:{:04d}{:02d}{:02d}T{}\n".format(tz, year, num, realday, mil_time)
             venventline06 = "DTEND;TZID={}:{:04d}{:02d}{:02d}T{}\n".format(tz, year, num, realday, mil_timeend)
             venventline07 = "SUMMARY:{}\n".format(summary)
             venventline08 = "DESCRIPTION:{}\n".format(description)
             venventline09 = "LOCATION:VT \n"
             venventline10 = "END:VEVENT\n"
             
             with open(ical_file_name, 'a') as f:
                 f.write(venventline01)
                 f.write(venventline02)
                 f.write(venventline03)
                 f.write(venventline04)
                 f.write(venventline05)
                 f.write(venventline06)
                 f.write(venventline07)
                 f.write(venventline08)
                 f.write(venventline09)
                 f.write(venventline10)
                 
with open(ical_file_name, 'a') as f:
    f.write("END:VCALENDAR")
                 
                 
            
             
             

                               


   
   