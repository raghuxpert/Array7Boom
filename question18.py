#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re

def check_length(pswd):
    if len(pswd) >= 6 and len(pswd) <= 12:
        return True
    return False

def check_lowercase(pswd):
    if re.search("[a-z]",pswd):
        return True
    return False

def check_uppercase(pswd):
    if re.search("[A-Z]", pswd):
        return True
    return False


def check_number(pswd):
    if re.search("[0-9]", pswd):
        return True
    return False


def check_special_char(pswd):
    if re.search("[$#@]", pswd):
        return True
    return False


def password_check(pswd):
    if check_length(pswd) and check_lowercase(pswd) and check_uppercase(pswd) and check_number(pswd) and check_special_char(pswd):
        return True
    return False

password = input("write comma seperated asswords : ").split(",")
Good_Password = list(filter(password_check, password))
print(Good_Password)