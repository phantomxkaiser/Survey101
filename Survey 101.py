import tkMessageBox
from Tkinter import *
from tkMessageBox import *
import sys

master = Tk()

# the size of the windows
master.geometry('600x600')
# the title
master.title("Survey 101")

#Question
q1 = 'Students in my class treat one another with respect.'
q2 = 'You did not feel safe traveling to and from school.'
q3 = 'I participate regularly in class.'
q4 = 'Do your parents usually speak a language other than English at home?'
q5 = 'You were being bullied or harassed by other students.'

#Message Box question Yes and No to close the windows
def callback():
    if askyesno('Verify', 'Do you really want to quit?'): # when you clock "Close" button, you will ask whether u want to quit or not
        master.destroy() # if you pick yes, the windows will close down and unsave
    else:
        showinfo('No', 'Quit has been cancelled') # if you pick "no", the window will not close

# Option Answers:
op1 = 'Strong Disagree'
op2 = 'Somewhat Disagree'
op3 = 'Somewhat Agree'
op4 = 'Strongly Agree'
op5 = 'Never'
op6 = 'Once or Twice'
op7 = 'A Few Times a Year'
op8 = 'Several Times a Year'
op9 = 'Yes'
op10 = 'No'

def var_states():
    answers= [op1,op2,op3,op4,op5,op6,op7,op8,op9,op10]
    print "Question 1 answer is",answers[var1.get()-1]
    print "Question 2 answer is",answers[var2.get()-1]
    print "Question 3 answer is",answers[var3.get()-1]
    print "Question 4 answer is",answers[var4.get()-1]
    print "Question 5 answer is",answers[var5.get()-1]

    f = open('The outcomes.txt', 'w')  # Open file
    f.write("Question 1 answer is " +answers[var1.get()-1]+"\n") # write the file
    f.write("Question 2 answer is "+answers[var2.get()-1]+"\n") # write the file
    f.write("Question 3 answer is "+answers[var3.get()-1]+"\n")# write the file
    f.write("Question 4 answer is "+answers[var4.get()-1]+"\n")# write the file
    f.write("Question 5 answer is "+answers[var5.get()-1]+"\n")# write the file
    f.close()  # Close the file
    master.destroy()

# focus one one answer to click on only
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

#question 1
Label(master, text = q1).pack()

#Answer option answer
#the answer button that you can choose
radio1 = Radiobutton(master, text = op1, variable=var1, value = 1).pack(anchor=W)
radio2 = Radiobutton(master, text = op2, variable=var1, value = 2).pack(anchor=W)
radio3 = Radiobutton(master, text = op3, variable=var1, value = 3).pack(anchor=W)
radio4 = Radiobutton(master, text = op4, variable=var1, value = 4).pack(anchor=W)

#question 2

Label(master, text = q2).pack()

# the answer button that you can choose
radio5 = Radiobutton(master, text = op5, variable=var2, value = 5).pack(anchor=W)
radio6 = Radiobutton(master, text = op6, variable=var2, value = 6).pack(anchor=W)
radio7 = Radiobutton(master, text = op7, variable=var2, value = 7).pack(anchor=W)
radio8 = Radiobutton(master, text = op8, variable=var2, value = 8).pack(anchor=W)

#Question 3
Label(master, text = q3).pack()
# the answer button that you can choose

radio9 = Radiobutton(master, text = op1, variable=var3, value = 1).pack(anchor=W)
radio10 = Radiobutton(master, text = op2, variable=var3, value = 2).pack(anchor=W)
radio11 = Radiobutton(master, text = op3, variable=var3, value = 3).pack(anchor=W)
radio12 = Radiobutton(master, text = op4, variable=var3, value = 4).pack(anchor=W)

#Question 4
Label(master, text = q4).pack()

# the answer button that you can choose
radio12 = Radiobutton(master, text = op9, variable=var4, value = 9).pack(anchor=W)
radio13 = Radiobutton(master, text = op10, variable=var4, value = 10).pack(anchor=W)

#Question 5
Label(master, text = q5).pack()
# the answer button that you can choose

radio5 = Radiobutton(master, text = op5, variable=var5, value = 5).pack(anchor=W)
radio6 = Radiobutton(master, text = op6, variable=var5, value = 6).pack(anchor=W)
radio7 = Radiobutton(master, text = op7, variable=var5, value = 7).pack(anchor=W)
radio8 = Radiobutton(master, text = op8, variable=var5, value = 8).pack(anchor=W)

#close the windows or submit the answer for the survey
button1 = Button(master, text = 'Submit', command = var_states).pack(side=RIGHT)
button2 = Button(text = 'Close', command = callback).pack(side=RIGHT)

mainloop()
