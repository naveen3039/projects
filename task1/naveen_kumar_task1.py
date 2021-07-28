# Purpose of the Script
#################################################################################################################################
# This script has been designed to read data from a text file for count and sum of bytes.
# Write the output count and sum greater than 5000 of bytes.

#######################################################################################################################################################
# Below points has been consider in the Scripts
###########################################################################################################################################################################

# 1.Read from input file row wise and written output based on condition.

# 2.A log file created with the current date time along with message specified.

# 3.Script has been Written to exit out for errorneous Condition.

########################################################################################################################################################################################

# importing sys module for exit and logging for log the file
import sys
import logging

logging.basicConfig(
    filename="new.log",
    format="%(asctime)s :: %(message)s",
    filemode="w",
    level=logging.INFO,
)

# Using try-except block for error handling
try:
    with open("input.txt", "r") as f:
        # Reading input file data
        data = f.read()
        logging.info("Read the file and to the data variable")
    count_lines = data.split("\n")
    logging.info("All lines splited and collected to a  list")

    # Checking the no. of lines less than to 2*pow(10,5)
    if len(count_lines) < 2 * pow(10, 5):
        count = 0
        sum = 0
        logging.info("intialising count and sum as a 0 ")

        # Looping the lines in which are present in input data
        for i in count_lines:
            s = i.split()
            # Converting byte value to integer
            byte = int(s[len(s) - 1])

            # Checking byte is greater than 5000 or not
            if byte > 5000:
                count += 1
                sum += byte
                logging.info(
                    f"Byte is greater than 5000 so count = {count},sum ={sum} "
                )

        # Checking sum of the Bytes greater than pow(10,12)
        if sum > pow(10, 12):
            logging.info("sum is greater than pow(10,12) so it is exited")
            raise Exception
        else:
            # Writing required to the output file
            with open("output.txt", "w") as f:
                print(f"count of records greater than 5000:{count}", file=f)
                print(f"sum of records greater than 5000:{sum}", file=f)
            logging.info("Written output to output file")
    else:
        logging.info("The no. of lines in input file in greater than 2 * pow(10, 5)")
        raise Exception
except:
    # Handling the errorneous condition
    logging.info("You are exited")
    sys.exit()
