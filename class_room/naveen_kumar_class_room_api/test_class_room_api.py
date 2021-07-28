#Location of this script
#/home/infinite/Documents/code/ubuntu/task/class_room/naveen_kumar_class_room_api/test_class_room_api.py

############# Script Details #################################################################

# Script Name            :  test_class_room_api.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  09-06-21
# last_modification_date :  14-06-21

#####################################################################################################
# Purpose of the Script
######################################################################################################

# This script is designed such that test on for the all the operations
# like GET, CREATE, DELETE, LIST of the information available for students present in class_room_api

#####################################################################################################
# Below points has been considered in the Script
###################################################################################################

# 1.fetching details a class_room api .

# 2.Given respective credentials and permissions to it.

# 3.Testing various testcases of delete ,list , create , get functions

# 4.A log file created with the current date time along with message specified.

##############################################################################################


# imported class_room_api for testing
from class_room_api import (
    create_invite,
    list_invitations,
    list_student,
    get_student,
    delete_student,
    alreadycreated,
)
import pytest
import os
import logging

pytest.main(args=["-sv", os.path.abspath(__file__)])


logger = logging.getLogger(__name__)
# testing the creating invitation
def test_create_invite():
    logging.info("Started testing positive cases")
    logger.info("testing create invite")
    user_name = "Naveen Kumar"
    names = create_invite(user_name)
    assert "Naveen Kumar" in names
    assert len(names) > 0
    assert "Naveen" not in names
    logging.info("test cases executed successfully for create_invite")


# testing list of invitations
def test_list_invitations():
    logger.info("testing list of invite")
    invite = list_invitations()
    assert len(invite) > 0
    assert invite["invitations"][0]["courseId"] == "360339604290"
    logging.info("test cases executed successfully for list_invite")


# testing list of students
def test_list_student():
    logger.info("testing list of students")
    list_students = list_student()
    assert len(list_students) != 0
    assert list_students["students"][0]["courseId"] == "360339604290"
    logging.info("test cases executed successfully for list of students")


# testing a student list
def test_get_student():
    logger.info("testing get student")
    student = get_student()
    assert student["userId"] == "114205514281092595614"
    assert student["userId"] != "14205514281092595614"
    logging.info("test cases executed successfully for get_student")


# testing delete student
def test_delete_student():
    logger.info("testing delete invite")
    userid = "112580249015376046981"
    student = delete_student(userid)
    assert "112580249015376046981" not in student
    assert len(userid) == 21
    logging.info("test cases executed successfully for delete student")


# testing creating invitations
def test_create_failure():
    logging.info("Started testing negative cases")
    logger.info("Execution started for test_create_failure")
    try:
        logger.info("testing create invite")
        user_name = "Naveen"
        names = create_invite(user_name)
    except:
        with pytest.raises(alreadycreated) as exc_info:
            user_name = "Naveen"
            create_invite(user_name)
        logger.info(str(exc_info.value))
        print(str(exc_info.value))


# testing list of invitations
def test_list_invitations_failure():
    logger.info("testing list of invite failure")
    with pytest.raises(AssertionError) as exc_info:
        invite = list_invitations()
        assert len(invite) < 0
        assert invite["invitations"][0]["courseId"] == "36033904290"
    logger.info(str(exc_info))
    print("assertion error")


# testing list of students
def test_list_student_failure():
    logger.info("testing list of students failure")
    with pytest.raises(AssertionError) as exc_info:
        list_students = list_student()
        assert len(list_students) == 0
        assert list_students["students"][0]["courseId"] != "360339604290"
    logger.info(str(exc_info))
    print("assertion error")


# testing a student list
def test_get_student_failure():
    logger.info("testing get student failure")
    with pytest.raises(AssertionError) as exc_info:
        student = get_student()
        assert student["userId"] != "114205514281092595614"
        assert student["userId"] == "14205514281092595614"
    logger.info(str(exc_info))
    print("assertion error")


# testing delete student
def test_delete_student_failure():
    logger.info("Execution started for test_delete_failure")
    with pytest.raises(AssertionError) as exc_info:
        logger.info("testing delete invite")
        userid = "112580249015376046981"
        student = delete_student(userid)
        assert "112580249015376046981" in student
        assert len(userid) == 20
    logger.info(str(exc_info))
    print("assertion error")
