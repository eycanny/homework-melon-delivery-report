def generate_sales_report(day, file):
    """Print a line-by-line sales report based on desired day's file.

    Print the day of the report.
    Print individual lines containing the amount delivered, what was delivered, and total amount.
    """
    print(f"Day {day}") #print message with day passed in as an argument
    the_file = open(file) #opens file passed in as an argument
    for line in the_file: #iterates thru each line in the file defined above
        line = line.rstrip() #removes whitespace from the right
        words = line.split('|') #use | as a delimiter when tokenizing line

        melon = words[0] #grabs first value of list and assign it to variable
        count = words[1] #grabs second value of list and assign it to variable
        amount = words[2] #grabs third value of list and assign it to variable

        print(f"Delivered {count} {melon}s for total of ${amount}") #print a message with f-string formatting with the above defined variables
    the_file.close() #closes file