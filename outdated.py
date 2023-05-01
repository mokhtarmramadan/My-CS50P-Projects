# A dict with all of the anno domini months, thier order as key value pairs
months = {"January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"}

# While forever untill the user inputs the date in the right format either in (MM/DD/YYYY) or in Month day, year
while True:
    try:
        date = input("Date: ")
    except:
        continue
    # If the date is in the (MM/DD/YYYY) format we'll try to split it into three parts at a time and if
    # it meets the valid date requirments then print it in (DD-MM-YYYY) format and break else keep 
    # reprompting
    if "/" in date:
        try:
            month, day, year = date.split("/")
            if int(day) <= 31 and int(month) <= 12:
                print(f"{year.strip()}-{int(month.strip()):02}-{int(day.strip()):02}")
                break

        # if we have any exception keep reprompting    
        except:
            continue
    
    # If date has "," in it try to split the date base on it two values
    elif "," in date:
        
        try:
            month_and_day, year = date.split(",")

            # Split the month_and_day string to two strings base on the space between them
            month, day = month_and_day.split(" ")

            # Validate the date and if it's in a valid format print it in (DD-MM-YYYY) format and break
            if int(day) <= 31 and month in months:
                print(f"{year.strip()}-{months[month.strip()]}-{int(day.strip()):02}")
                break

        # if we have have any exceptions reprompt 
        except:
            continue
        
        # If the date doesn't have neither "," nor "/" keep reprompting
        else:
            continue