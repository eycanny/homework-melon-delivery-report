def generate_sales_report(day, file):
    """Print a line-by-line sales report based on desired day's file.

    Print the day of the report.
    Print individual lines containing the amount delivered, what was delivered, and total amount.
    """
    print(f"Day {day}")
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()