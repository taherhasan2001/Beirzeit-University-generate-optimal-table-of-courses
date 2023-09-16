import json
class Course:
    def __init__(self, course_label, section, instructor, days, time_display, place=None, numOfStudents=None):
        self.course_label = course_label
        self.time_display = time_display  # 8:00-9:15
        self.section = section  # 0,1,2,3,...
        self.instructor = instructor  # name
        self.days = days  # "S,M,T,W,R" capital letters with comma
        self.place = place  # "O.Abdulhadi052"
        self.numOfStudents = numOfStudents  # 54 / 120

    def time_start(self):  # return string
        return self.time_display.split("-")[0]

    def time_end(self):  # return string
        return self.time_display.split("-")[1]

    def collision(self, other):  # other is another Course object
        # return True if self and other have collision
        flag_days = True  # keep True if no days in common

        for day in self.days.split(","):
            if day in other.days.split(","):
                flag_days = False
        if flag_days:  # no days in common

            return False
        if float(self.time_start().replace(":", ".")) >= float(other.time_end().replace(":", ".")):
            # print(other.time_end())
            return False
        if float(self.time_end().replace(":", ".")) <= float(other.time_start().replace(":", ".")):
            return False
        return True

    def __str__(self):
        return f"{self.course_label}-{self.section}-{self.instructor}-{self.days}-{self.time_start()}-{self.time_end()}"

    def __repr__(self):
        return f"{self.course_label}-{self.section}-{self.instructor}-{self.days}-{self.time_start()}-{self.time_end()}"


# ------------------ Adding courses ------------------
def search_courses(course_name, preName):  # ex : preName = 'ACCT'
    found_courses = []
    flagWeGotOne = False
    with open(f'{preName}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        for course_data in data:
            if course_data["name of course"] == course_name:
                flagWeGotOne = True
                course = Course(
                    course_data["name of course"],
                    course_data["sec"],
                    course_data["name of instructor"],
                    course_data["days"].replace(" ", ""),
                    course_data["time"],
                    course_data["place"],
                    course_data["number of students"]
                )
                found_courses.append(course)
            elif flagWeGotOne:
                break
    return found_courses


listACCT = search_courses("ACCT230", "ACCT")
listCOMP = search_courses("COMP233", "COMP")
listCOMP2 = search_courses("COMP122", "COMP")
listENCS = search_courses("ENCS4300", "ENCS")

courses = [listACCT, listCOMP, listCOMP2]

# ------------------ preparing combinations ------------------
minDays = None
minStartTime = None
minEndTime = None
dec = {}


def combinations(ArraySec, index=0, current_combination=[]):
    global minDays
    global minStartTime
    global minEndTime
    if index == len(ArraySec):
        chosenSections = []
        for sec in range(len(current_combination)):  # making list of chosen sections
            chosenSections.append(courses[sec][current_combination[sec]])
            # example : chosenSections =  [<__main__.Course object at 0x000002B2EF867FD0>, <__main__.Course object at 0x000002B2EF867D90>]
        numberOfDays = []
        # check if there is a collision between chosen sections
        # current_combination = [0, 0] -> chosenSections = [arab1, eng1]
        # current_combination = [0, 1] -> chosenSections = [arab1, eng2]

        for i in range(len(chosenSections)):
            for day in chosenSections[i].days.split(','):  # check the days of each section
                if day not in numberOfDays:
                    numberOfDays.append(day)
            for j in range(i + 1, len(chosenSections)):
                if chosenSections[i].collision(chosenSections[j]):
                    # print(f"Collision between: {chosenSections[i]} and {chosenSections[j]}")
                    return

        if minDays == None or len(numberOfDays) < minDays:
            minDays = len(numberOfDays)
        if minStartTime == None or float(chosenSections[0].time_start().replace(":", ".")) < float(
                minStartTime.replace(":", ".")):
            minStartTime = chosenSections[0].time_start()
        startTime = None
        endTime = None
        for section in chosenSections:
            if startTime == None or float(section.time_start().replace(":", ".")) < float(startTime.replace(":", ".")):
                startTime = section.time_start()
            if endTime == None or float(section.time_end().replace(":", ".")) > float(endTime.replace(":", ".")):
                endTime = section.time_end()
        if minEndTime == None or float(endTime.replace(":", ".")) < float(minEndTime.replace(":", ".")):
            minEndTime = endTime

        chosenSectionsTuple = tuple(chosenSections)

        dec[chosenSectionsTuple] = {"numberOfDays": numberOfDays, "startTime": startTime, "endTime": endTime}
        return

    max_number = len(ArraySec[index]) - 1
    for i in range(max_number + 1):
        current_combination.append(i)
        combinations(ArraySec, index + 1, current_combination)
        current_combination.pop()


combinations(courses)


# ------------------ choices to select ------------------
def reduce_the_days():
    deleted = []
    for key in dec:
        # if s[0] != min:
        if len(dec[key]['numberOfDays']) != minDays:
            deleted.append(key)
        # print("*************")
    for key in deleted:
        dec.pop(key)


def reduce_the_startTime():
    deleted = []
    for key in dec:
        if dec[key]['startTime'] != minStartTime:
            deleted.append(key)
    for key in deleted:
        dec.pop(key)


def reduce_the_endTime():
    deleted = []
    for key in dec:
        if dec[key]['endTime'] != minEndTime:
            deleted.append(key)
    for key in deleted:
        dec.pop(key)


def print_dict():
    for key in dec:
        for k in key:
            print(k)
        print(dec[key])
        print("*************")
    print("minDays: ", minDays)
    print("minStartTime: ", minStartTime)
    print("minEndTime: ", minEndTime)

DectoUse = dec.copy()



from interface import *


display(dec)
