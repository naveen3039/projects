# Purpose of the Script
############################################################################################################################

# This script is designed Create for same row a csv file
# Create a csv file containing 10 lines solaris and redhat,
# 10 lines on hypervisor,10 lines without hypervisor,solaris and redhat
# Read input from csv file
# Output should written in 3 files unix.txt,hypervisor.txt,other.txt
# The output should written line containg solaris and red hat in unix.txt
# The output should written line containg hypervisor in hypervisor.txt
# others lines written in others.txt

#################################################################################################################################################
# Below points has been consider in the Scripts
###################################################################################################################################################################

# 1.Created a csv file containing 10 lines solaris and redhat,

# 2.Read input from input csvfile

# 3.A log file created for date , time ,message specifically for required condition

# 4.Output was written in 3 text files
# line containing solaris and redhat in one file
# line containing hypervisor in one file
# remaining lines  in one file

###################################################################################################################################

# imported csv module to work on csv files
# imported logging module  for date, time, message specified of the script
import csv
import logging

logging.basicConfig(
    filename="req2.log",
    filemode="w",
    format=("%(asctime)s :: %(message)s"),
    level=logging.INFO,
)

# Read input from csv file
with open("req2.csv") as f:
    logging.info("Read input from input file")
    data = csv.reader(f)
    # Looping the input data
    for i in data:
        logging.info("Checking lines")

        # Checking each in line 'solaris' and 'redhat' are containing or not
        if "solaris" and "redhat" in i:
            # Written line containing 'solaris' and 'redhat' output in unix.txt
            with open("unix.txt", "a+") as f:
                for j in i:
                    print(j, file=f, end=" ")
                print(file=f)
            logging.info(
                'Written line containing "solaris" and "redhat" in output file'
            )

        # Checking each in line hypervisor are containing or not
        elif "hypervisor" in i:
            # Written line containing 'hypervisor' output in hypervisor.txt
            with open("hypervisor.txt", "a+") as f:
                for j in i:
                    print(j, file=f, end=" ")
                print(file=f)
            logging.info('Written line containing "hypervisor" in output file')

        else:
            # Written other lines output in other.txt
            with open("other.txt", "a+") as f:
                for j in i:
                    print(j, file=f, end=" ")
                print(file=f)
            logging.info("Written other lines in output file")
