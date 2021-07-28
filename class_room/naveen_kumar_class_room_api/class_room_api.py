#Location of this script  
#/home/infinite/Documents/code/ubuntu/task/class_room/naveen_kumar_class_room_api/class_room_api.py

############# Script Details #################################################################

# Script Name            :  class_room_api.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  09-06-21
# last_modification_date :  14-06-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that work on for the all the operations
# like GET, CREATE, DELETE, LIST of the information available for students present in class_room_api

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a class_room api .

# 2.Given respective credentials and permissions to it.

# 3.Created various method of delete ,list , create , get

# 4.A log file created with the current date time along with message specified.

# 5.Created Custom Exception for erroneous conditions

##############################################################################################
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="class_room.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)

logging.info("created custom exception for error handling")


class alreadycreated(Exception):
    pass


class empty_list(Exception):
    pass


class already_deleted(Exception):
    pass


# imported prequistes.quickstart for fetch class_room api
from prequistes.quick_start import service


# Creating course
def create_course():
    """In this function I am trying to create a course"""
    try:
        course = {
            "name": "coding",
            "section": "Period",
            "descriptionHeading": "Introduction to python",
            "description": "Learning about the basics of python",
            "room": "7",
            "ownerId": "me",
        }
        course = service.courses().create(body=course).execute()
        logging.info("course created successfully")
        logging.info(f'Course created : {course.get("name")} {course.get("id")} ')
    except:
        logging.info("error occured")
        raise alreadycreated("The course is already created")


# creating intivation for adding students to my course
def create_invite(name):
    """In this function  inviting students to my course"""
    try:
        info = {
            "userId": "k.lakshmipathi482@gmail.com",
            "courseId": "360339604290",
            "role": "STUDENT",
        }
        list_students = (
            service.courses()
            .students()
            .list(courseId="360339604290", pageSize=10)
            .execute()
        )
        logging.info("Fetching details of students")
        logging.info("creating a empty list data structure for store names of students")
        names = []
        # fetching details of students
        for course in list_students.items():
            for user in range(len(course[1])):
                names.append(course[1][user]["profile"]["name"]["fullName"])
        logging.info(names)
        logging.info(name)
        # checking student name not in students_list
        if name not in names:
            invite = service.invitations().create(body=info).execute()
            logging.info("sent a invitation to student email")
        return names
    except:
        logging.info("error occured")
        raise alreadycreated("The user is already exists")


# create_invite('Naveen Kumar')


# fetching list of invitations
def list_invitations():
    """In this function  fetching all invitations"""
    try:
        list_invite = service.invitations().list(courseId="360339604290").execute()
        logging.info("fetched all the details of invitation")
        return list_invite
    except:
        raise empty_list("No elements are present")


# list_invitations()


# fetching of list of students
def list_student():
    """In this function  fetching all the students"""
    try:
        list_students = (
            service.courses()
            .students()
            .list(courseId="360339604290", pageSize=10)
            .execute()
        )
        logging.info("fetched list of students")
        return list_students
    except:
        logging.info("error occured")
        raise empty_list("no elements are present")


# list_student()


# fetch student detail
def get_student():
    """In this function tring to fetch particular student detail with userid"""
    try:
        list_student = (
            service.courses()
            .students()
            .get(courseId="360339604290", userId="114205514281092595614")
            .execute()
        )
        logging.info("fetched particular data with userid")
        return list_student
    except:
        logging.info("error occured")
        raise empty_list("no elements are present")


# get_student()


# delete student from course
def delete_student(userid):
    """In this function trying to delete student with userid"""
    try:
        list_students = list_student()
        logging.info("Fetching details of students")
        logging.info(
            "creating a empty list data structure for store userid of students"
        )
        student = []
        # fetching details of students
        for course in list_students.items():
            for user in range(len(course[1])):
                student.append(course[1][user]["userId"])
        logging.info(userid)
        logging.info(student)
        # checking userid not in students_list
        if userid in student:
            delete_students = (
                service.courses()
                .students()
                .delete(courseId="360339604290", userId=userid)
                .execute()
            )
            logging.info("deleted particular userid containing student")
        return student
    except:
        logging.info("error occured")
        raise already_deleted("The student was already deleted")


# delete_student('113580249015376046991')
