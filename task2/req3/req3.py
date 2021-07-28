# Purpose of the Script
##################################################################################################################################################

# This script designed To  merge of two 2 csv files
# Create a csv file with 5 columns
# Create a copy of that csv file
# Create another csv file with 2 column
# Now,merge the copy file and new file that should be write in first original file
# Output data will be storted in output file
# Then rename file output file to first created file name

####################################################################################################################################################################
# Below points can be considered in the Scripts
#################################################################################################################################################################################

# 1.Created a csv file inserted 5 columns and created a copy of that file

# 2.Created a another csv inserted 2 columns

# 3.A log file has been created for date and time , message specifed at requirement.

# 4.Merged the copy file and new file data

# 5.Merged data written in Output file

# 6.Renamed Output file to first created file name

################################################################################################################################################################################################

# imported csv for work on csv files
# imported pandas for merge the csv files
# imported logging for log the date and time , message specified
# imported os module for rename the files
import csv
import pandas as pd
import logging
import os

logging.basicConfig(
    filename="req3.log",
    filemode="w",
    format=("%(asctime)s :: %(message)s"),
    level=logging.INFO,
)

# Written  5 rows in the csv file and a header
with open("a.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(
        [["names"], ["naveen"], ["kumar"], ["nithin"], ["dhoni"], ["naveena"]]
    )
    logging.info("created 5 rows in a.csv file")

# Written copy of a.csv to b.csv
with open("b.csv", "w") as f:
    with open("a.csv", "r") as f1:
        data = csv.reader(f1)
        rows = [i for i in data]
        writer = csv.writer(f)
        writer.writerows(rows)
        logging.info("created a copy of a.csv named as b.csv")

# Written 2 rows in 3.csv
with open("3.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows([["names"], ["naveen"], ["kum"]])
    logging.info("created two rows in new csv file  named as 3.csv")

# Read b.csv file
data1 = pd.read_csv("b.csv")
# Read c.csvfile
data2 = pd.read_csv("3.csv")
# merge the two csv file using pandas.merge
merge = pd.merge(data1, data2, how="outer")
logging.info("merged two csv files b.csv and 3.csv")
# merged data converted to List data structure
merge = merge.names.to_list()
logging.info("merged data converted to list")

# Output merged data was written in output.csv file
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    for i in merge:
        writer.writerow([i])
    logging.info("written output data to output.csv ")

# Output file renaming to a.csv
os.rename("output.csv", "a.csv")
logging.info("renamed output.csv to a.csv")
