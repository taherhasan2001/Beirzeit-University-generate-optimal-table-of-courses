class Course:
    def __init__(self, course_label, section, instructor, days, time_display):
        self.course_label = course_label
        self.time_display = time_display # 8:00-9:15
        self.section = section  # 0,1,2,3,...
        self.instructor = instructor  # name
        self.days = days  # "S,M,T,W,R" capital letters with comma
    def time_start(self): # return string
        return self.time_display.split("-")[0]
    def time_end(self): # return string
        return self.time_display.split("-")[1]

    def collision(self, other): # other is another Course object
        # return True if self and other have collision
        flag_days = True # keep True if no days in common

        for day in self.days:
            if day in other.days:
                flag_days = False
        if flag_days: # no days in common

            return False
        if float(self.time_start().replace(":", ".")) >= float(other.time_end().replace(":", ".")):
            print(other.time_end())
            return False
        if float(self.time_end().replace(":", ".")) <= float(other.time_start().replace(":", ".")):
            return False
        return True


    def __str__(self):
        return f"Course: {self.course_label}, Section: {self.section}, Instructor: {self.instructor}, Days: {self.days}, Time: {self.time_display}"


# course_label, section, instructor, days, time_display
sec1 = Course("CS 101", 0, "Dr. John", "M,W,F", "8:00-9:15")
sec2 = Course("CS 101", 1, "Dr. John", "M,W,F", "7:30-10:45")
sec3 = Course("CS 101", 2, "Dr. John", "M,W,F", "9:30-10:45")
print(sec1.collision(sec3))

# ------------------ 1 ------------------

dec = {}

def print_combinations(ArraySec, ArraySize, index=0, current_combination=[]):
    if index == len(ArraySize):
        combination_tuple = tuple(current_combination)
        if sum(combination_tuple) == 5:
            dec[combination_tuple] = sum(combination_tuple)
        return

    max_number = ArraySize[index]
    for i in range(max_number + 1):
        current_combination.append(i)
        print_combinations(ArraySec, ArraySize, index + 1, current_combination)
        current_combination.pop()

ArraySec = [0, 0, 0, 0, 0]
ArraySize = [1, 2, 3, 4, 5]
print_combinations(ArraySec, ArraySize)
print(dec)
