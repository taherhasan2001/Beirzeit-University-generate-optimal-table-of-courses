
import json
class Course:
    def __init__(self, course_label, section, instructor, days, time_display,place=None,numOfStudents=None):
        self.course_label = course_label
        self.time_display = time_display # 8:00-9:15
        self.section = section  # 0,1,2,3,...
        self.instructor = instructor  # name
        self.days = days  # "S,M,T,W,R" capital letters with comma
        self.place = place # "O.Abdulhadi052"
        self.numOfStudents = numOfStudents # 54 / 120
    def time_start(self): # return string
        return self.time_display.split("-")[0]
    def time_end(self): # return string
        return self.time_display.split("-")[1]

    def collision(self, other): # other is another Course object
        # return True if self and other have collision
        flag_days = True # keep True if no days in common

        for day in self.days.split(","):
            if day in other.days.split(","):
                flag_days = False
        if flag_days: # no days in common

            return False
        if float(self.time_start().replace(":", ".")) >= float(other.time_end().replace(":", ".")):
            # print(other.time_end())
            return False
        if float(self.time_end().replace(":", ".")) <= float(other.time_start().replace(":", ".")):
            return False
        return True


    def __str__(self):
        return f"{self.course_label}-{self.section}-{self.instructor}-{self.days}-{self.time_start()} -> {self.time_end()}"
    def __repr__(self):
        return f"{self.course_label}-{self.section}-{self.instructor}-{self.days}-{self.time_start()} -> {self.time_end()}"



# ------------------ 0 ------------------

def search_courses(course_name, preName): # ex : preName = 'ACCT'
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

# ------------------ 0 ------------------
arab1 = Course("CS101", 0, "Dr. John", "M,W", "8:00-9:15")
arab2 = Course("CS101", 1, "Dr. John", "T,F", "7:30-10:45")
arab3 = Course("CS101", 2, "Dr. John", "F", "9:30-10:45")

eng1 = Course("CS102", 0, "Dr. Abbas", "T,F", "8:00-9:15")
eng2 = Course("CS102", 1, "Dr. Abbas", "T,W", "7:30-10:45")
eng3 = Course("CS102", 2, "Dr. Abbas", "T,W", "9:30-10:45")

listACCT = search_courses("ACCT230", "ACCT")
listCOMP = search_courses("COMP233", "COMP")
listCOMP2 = search_courses("COMP122", "COMP")
listENCS = search_courses("ENCS4300", "ENCS")

courses = [[arab1,arab2,arab3],[eng1,eng2,eng3],listACCT , listCOMP, listCOMP2]

# ------------------ 1 ------------------
minDays = None
dec = {}

def print_combinations(ArraySec, index=0, current_combination=[]):
    global minDays

    if minDays != None and len(current_combination) > minDays:
        return
    if index == len(ArraySec):
        chosenSections = []
        for sec in range(len(current_combination)): # making list of chosen sections
            chosenSections.append(courses[sec][current_combination[sec]])
            #example : chosenSections =  [<__main__.Course object at 0x000002B2EF867FD0>, <__main__.Course object at 0x000002B2EF867D90>]
        numberOfDays = []
        # check if there is a collision between chosen sections
        # current_combination = [0, 0] -> chosenSections = [arab1, eng1]
        # current_combination = [0, 1] -> chosenSections = [arab1, eng2]

        for i in range(len(chosenSections)):
            for day in  chosenSections[i].days.split(',') : # check the days of each section
                if day not in numberOfDays:
                    numberOfDays.append(day)
            for j in range(i+1, len(chosenSections)):
                if chosenSections[i].collision(chosenSections[j]):
                    # print(f"Collision between: {chosenSections[i]} and {chosenSections[j]}")
                    return
        if minDays != None and len(numberOfDays) > minDays:
            # print('yes')
            return

        minDays = len(numberOfDays)
        # print("minDays: ", minDays)



        chosenSectionsTuple = tuple(chosenSections)

        dec[chosenSectionsTuple] = numberOfDays
        return

    max_number = len(ArraySec[index]) - 1
    for i in range(max_number + 1):
        current_combination.append(i)
        print_combinations(ArraySec, index + 1, current_combination)
        current_combination.pop()

print_combinations(courses)





# ------------------ reduce the days ------------------
# to reduce the days of each combination to the minimum
deleted = []
for key in dec:
    # if s[0] != min:
    if len(dec[key]) != minDays:
        deleted.append(key)
    # print("*************")
for key in deleted:
    dec.pop(key)
# ------------------ reduce the days ------------------




for key in dec:
    for k in key :
        print(k)
    print(dec[key])
    print("*************")
