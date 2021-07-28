# Purpose of script
#########################################################################

# This scrpit has designed to read first column of csv file
# create a csv file and inserted 4 column and 10 rows
# Read Input from a csv file
# Write the output only first column in output file

###############################################################################################################3
# Below points has been consider in the Scripts
###########################################################################################

# 1.created a csv file and inserted 4 column and 10 rows

# 2.A log file created with the current date time along with message specified.

# 3.Read a csv file for header and rows

# 4.Written the first column of csv file in output file

############################################################################

# imported csv  module for work on csv file
# imported logging module for date, time, message specified of the script
import csv
import logging

logging.basicConfig(
    filename="req1.log",
    filemode="w",
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)

# Written a csv file for and inserted 4 columns and 10 rows
with open("req1.csv", "w") as f:
    logging.info("Created a req1.csv file for input data")
    header = ["model", "company", "launched_year", "price"]
    # Use csv.Dictwriter for construction of header
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    # Written rows by using writerow
    writer.writerow(
        {"model": "x2", "company": "realme", "launched_year": 2019, "price": 20000}
    )
    writer.writerow(
        {"model": "xt", "company": "realme", "launched_year": 2019, "price": 18000}
    )
    writer.writerow(
        {"model": "x3", "company": "realme", "launched_year": 2020, "price": 20000}
    )
    writer.writerow(
        {"model": "x7", "company": "realme", "launched_year": 2021, "price": 21000}
    )
    writer.writerow(
        {"model": "x2pro", "company": "realme", "launched_year": 2019, "price": 30000}
    )
    writer.writerow(
        {"model": "x3pro", "company": "realme", "launched_year": 2020, "price": 25000}
    )
    writer.writerow(
        {"model": "x50pro", "company": "realme", "launched_year": 2020, "price": 34000}
    )
    writer.writerow(
        {"model": "x60pro", "company": "realme", "launched_year": 2021, "price": 38000}
    )
    writer.writerow(
        {"model": "x", "company": "realme", "launched_year": 2018, "price": 20000}
    )
    writer.writerow(
        {"model": "x50", "company": "realme", "launched_year": 2020, "price": 30000}
    )
    logging.info("input data has written in req1.csv")


# Read a csv file a store the header
with open("req1.csv") as f:
    # Looping rows in List data structure
    logging.info("Read csv file for header")
    for row in csv.reader(f):
        header = row
        # After collecting first row or Header stopped the loop
        break

# Read a csv file for read the all rows
with open("req1.csv") as f:
    logging.info("Read csv file for row")
    # Looping rows in Dictionary data structure
    for row in csv.DictReader(f):
        # Accessing the first Column
        with open("output.txt", "a+") as f:
            print(row[header[0]], file=f)
    logging.info("Output has written in output.txt")
