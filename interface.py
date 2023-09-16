from tkinter import ttk
import os
from tkinter import *
l=[]
lf = []

path = os.path.abspath("img")

class display():
    def __init__(self, DectoUse,flagReducedays,flagreduceTime,flagReduceStartTime,flagReduceEndTime,flagReduceTotalTime):
        self.pointer = 0
        self.minStartTime = None
        self.minEndTime = None
        self.minTime = None
        self.minDays = None
        self.Dec = DectoUse
        self.button_pointer = 0
        # ------------------ choices ------------------
        if flagReducedays:
            self.get_details()
            print(
                f"[flagReducedays = {flagReducedays}] minDays = {self.minDays} \nminStartTime = {self.minStartTime} \nminEndTime = {self.minEndTime} \nminTime = {self.minTime} \nnumber of groups = {len(self.Dec)}")
            print("====================================================================================================")
            self.Dec = self.reduceDays()
        if flagreduceTime:
            self.get_details()
            print(
                f"[flagreduceTime = {flagreduceTime}] minDays = {self.minDays} \nminStartTime = {self.minStartTime} \nminEndTime = {self.minEndTime} \nminTime = {self.minTime}\nnumber of groups = {len(self.Dec)}")
            print("====================================================================================================")
            self.Dec = self.reduceTime()
        if flagReduceStartTime:
            self.get_details()
            print(
                f"[flagReduceStartTime = {flagReduceStartTime}] minDays = {self.minDays} \nminStartTime = {self.minStartTime} \nminEndTime = {self.minEndTime} \nminTime = {self.minTime}\nnumber of groups = {len(self.Dec)}")
            print("====================================================================================================")
            self.Dec = self.reduceStartTime()
        if flagReduceEndTime:
            self.get_details()
            print(
                f"[flagReduceEndTime = {flagReduceEndTime}] minDays = {self.minDays} \nminStartTime = {self.minStartTime} \nminEndTime = {self.minEndTime} \nminTime = {self.minTime}\nnumber of groups = {len(self.Dec)}")
            print("====================================================================================================")
            self.Dec = self.reduceEndTime()
        if flagReduceTotalTime:
            self.get_details()
            print(
                f"[flagReduceTotalTime = {flagReduceTotalTime}] minDays = {self.minDays} \nminStartTime = {self.minStartTime} \nminEndTime = {self.minEndTime} \nminTime = {self.minTime}\nnumber of groups = {len(self.Dec)}")
            print("====================================================================================================")
            self.Dec = self.reduceTotalTime()
        # ------------------ end choices ------------------
        for key in self.Dec:
            print(key)
            print(self.Dec[key])
            print("*************")
        print("==================================end choices======================================================")
        print(f"number of groups = {len(self.Dec)}")
        # ------------------ GUI ------------------
        self.window = Tk()
        self.window.title('test')
        self.labels = []
        self.buttons = []
        self.window.geometry("1600x853")
        self.window.configure(bg="#ffffff")
        self.window.overrideredirect(1)
        canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=900,
            width=1600,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=path + r"\background.png")
        background = canvas.create_image(
            829.0, 386.0,
            image=background_img)
        # Label(relief="flat", bg="white", height=2, width=2, text=hours, bd=1.5, font=('Times', 16)).place(x=835, y=730)
        Label(self.window, text="Version 1.0").place(x=10, y=830)
        # Sharp Button Outline Dark Mode
        Exit = PhotoImage(file=path + r"\Sharp Button Outline Dark Mode.png")
        Button(
            master=self.window,
            image=Exit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Exit(master=self.window),
            relief="flat").place(x=10, y=10)
        
        imgNext = PhotoImage(file=path + r"\Next.png")
        bNext = Button(
            master=self.window,
            image=imgNext,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Next(),
            relief="flat")
        bNext.place(x=1178, y=293)
        
        imgPrevious = PhotoImage(file=path + r"\Previous.png")
        bPrevious = Button(
            master=self.window,
            image=imgPrevious,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_Previous(),
            relief="flat")
        bPrevious.place(x=1020, y=293)
        for i in range(25):
            self.buttons.append(Button(master=self.window, command=lambda: self.doNothing(), relief="flat", bg="#99ffcc", height=1, width=1,
                   text="test", bd=0))

        for i in range(10):
            line_label = []
            for txt in range(5):
                line_label.append(self.finalText(x=txt, y=i, color='white', txt=''))
            self.labels.append(line_label)
        self.show()
        self.window.mainloop()
        
    def button_Previous(self):
        if self.pointer != 0:
            self.pointer -= 1
        counter = 0
        for key in self.Dec:
            if counter == self.pointer:
                    self.show(dec={key:self.Dec[key]})
            counter+= 1
    def button_Next(self):
        if self.pointer != len(self.Dec)-1:
            self.pointer += 1
        counter = 0
        for key in self.Dec:
            if counter == self.pointer:
                    self.show(dec={key:self.Dec[key]})
            counter+= 1
    def show(self,dec = None): #change_l_lf_and_show
        l.clear()
        lf.clear()
        if dec == None:
            dec = self.Dec
        for key in dec:
            for k in key:
                str = k.__str__().split("-")
                lf.append([str[0], str[1], str[2], str[3], f"{str[4]}-{str[5]}"])
                for day in str[3].replace(' ', '').split(','):

                    if day == 'S':
                        result = 0
                    elif day == 'Sun':
                        result = 1
                    elif day == 'M':
                        result = 2
                    elif day == 'T':
                        result = 3
                    elif day == 'W':
                        result = 4
                    elif day == 'R':
                        result = 5
                    elif day == 'F':
                        result = 6
                    elif day == 'N/A':
                        result = 11
                    else:
                        raise Exception(f"Error in day ==> {day}")
                    l.append(
                        [2, self.calculatAllTime(str[4], str[5]), [int(str[4].split(':')[0]), int(str[4].split(':')[1])],result, str[0], k])
            break
        self.button_pointer = 0
        for i in range(25):  # make sure to clean all the 25 buttons
            self.buttons[i].place_forget()
        for section in l:

            # -------------- Calculating Y --------------
            h = section[3]
            calculatedY = 351
            while h > 0:
                calculatedY += 53
                h -= 1
            # -------------- Calculating Y --------------

            # -------------- Calculating X --------------
            hours = section[2][0]
            min = section[2][1]
            if hours == 2:
                hours = 14
            elif hours == 1:
                hours = 13
            elif hours == 3:
                hours = 15

            calculatedX = 145
            while hours > 7:
                hours -= 1
                calculatedX += 125
            if min > 0:
                calculatedX += int(125 * min / 60)

            # -------------- Calculating X --------------
            self.change_Button(h=int(section[0]), w=int(18 * section[1] / 60), x=calculatedX,
                               y=calculatedY, text=section[4])
            self.button_pointer += 1



        start = 0
        end = len(lf)
        if end > 10:
            end = 10

        self.dis_table_up(start=start, end=end, lf=lf)
    def get_details(self):
        self.minTime = None
        self.minStartTime = None
        self.minEndTime = None
        self.minDays = None
        for key in self.Dec:
            if self.minDays == None or len(self.Dec[key]['numberOfDays']) < self.minDays:
                self.minDays = len(self.Dec[key]['numberOfDays'])
            if self.minStartTime == None or float(self.Dec[key]['startTime'].replace(":", ".")) < float(self.minStartTime.replace(":", ".")):
                self.minStartTime = self.Dec[key]['startTime']
            if self.minEndTime == None or float(self.Dec[key]['endTime'].replace(":", ".")) < float(
                self.minEndTime.replace(":", ".")):
                self.minEndTime = self.Dec[key]['endTime']
            if self.minTime == None or float(self.Dec[key]['endTime'].replace(":", ".")) - float(self.Dec[key]['startTime'].replace(":", ".")) < float(
                self.minTime.replace(":", ".")):
                self.minTime = str(float(self.Dec[key]['endTime'].replace(":", ".")) - float(self.Dec[key]['startTime'].replace(":", ".")))


    def reduceTotalTime(self):
        dec = {}
        for key in self.Dec:
            if str(float(self.Dec[key]['endTime'].replace(":", ".")) - float(self.Dec[key]['startTime'].replace(":", "."))) == self.minTime:
                if key not in dec:
                    dec[key] = self.Dec[key]
        return dec
    def reduceDays(self):
        dec = {}
        for key in self.Dec:
            if len(self.Dec[key]['numberOfDays']) == self.minDays:
                if key not in dec:
                    dec[key] = self.Dec[key]
        return dec
    def reduceTime(self):
        dec = {}
        for key in self.Dec:
            if self.Dec[key]['totalTime'] == self.minTime:
                if key not in dec:
                    dec[key] = self.Dec[key]
        return dec

    def reduceStartTime(self):
        dec = {}
        for key in self.Dec:
            if self.Dec[key]['startTime'] == self.minStartTime:
                if key not in dec:
                    dec[key] = self.Dec[key]
        return dec

    def reduceEndTime(self):
        dec = {}
        for key in self.Dec:
            if self.Dec[key]['endTime'] == self.minEndTime:
                if key not in dec:
                    dec[key] = self.Dec[key]
        return dec


    def exit(self, event):
        self.window.attributes('-fullscreen', False)
    def doNothing(self):
        pass
    def dis_table_up(self, start, end, lf):
        for i in range(10):  # make sure to clean all the 10 Labels
            for partIndex in range(len(self.labels[i])):
                self.labels[i][partIndex].config(text='', bg='white')

        z = 0

        for i in range(start, end):
            i %= 10
            z += 1
            color = 'white'
            if z % 2 == 0:
                color = '#D9D9D9'

            for partIndex in range(5):
                self.labels[i][partIndex].config(text=lf[start + i][partIndex], bg=color)

    def finalText(self, x, y, color, txt):
        if x == 0:
            calculatedX = 1439
            calculatedW = 20
        elif x == 1:
            calculatedX = 1319
            calculatedW = 16
        elif x == 2:
            calculatedX = 1069
            calculatedW = 34
        elif x == 3:
            calculatedX = 841
            calculatedW = 31
        elif x == 4:
            calculatedX = 707
            calculatedW = 18
        elif x == 5:
            calculatedX = 546
            calculatedW = 22
        else:
            calculatedX =  388
            calculatedW = 21

        calculatedY = 34
        while y > 0:
            calculatedY += 25
            y -= 1

        lab = Label(master=self.window, relief="flat", bg=color, height=1, width=calculatedW, text=txt, bd=1.5, fg='black')
        lab.place(x=calculatedX, y=calculatedY)
        return lab


    def change_Button(self, h, w, x, y, text):
        self.buttons[self.button_pointer].config(height=h, width=w, text=text)
        self.buttons[self.button_pointer].place(x=x, y=y)


    def button_Exit(self, master):
        master.destroy()
    def calculatAllTime(self,strStartTime,strEndTime):
        start = strStartTime.split(":")
        end = strEndTime.split(":")
        start = int(start[0]) * 60 + int(start[1])
        end = int(end[0]) * 60 + int(end[1])
        return end - start



