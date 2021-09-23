from tkinter import*

root = Tk()

root.geometry("500x500")

def show_frame(frame):
    frame.tkraise()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = Frame(root)
frame2 = Frame(root)


frame1.grid(row=0, column=0, sticky="nsew")

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")


label1 = Label(frame1, text="Welcome Please Read the following  scenario \n and press enter to continue ",font="calibri  20", fg="blue")
label1.grid(row=0, column=0)

label2 =Label(frame1, text="1. A lives in the corner house.\n"
                           "2. C is between E and G.\n"
                           "3. there is 1 house between D and F.\n"
                           "4. F is neighbour of G\n"
                           "5. There are two houses between A and G.", font="corbel 15")
label2.grid(row=1, column=0)

frame1_btn = Button(frame1, text="Enter",bg="green",font="liberation 15", command=lambda: show_frame(frame2))
frame1_btn.grid(row=3, column=0)

button = Button(frame2, text="back", font="liberation 15",bg="green",command=lambda: show_frame(frame1))
button.grid(row=10, column=0)





def bool():
    name = str(entry.get())
    A = str(entry1.get())
    B = str(entry2.get())
    C = str(entry3.get())
    D = str(entry4.get())
    E = str(entry5.get())
    question = 0
    score=0
    if A == "D" or A == "d":
        score += 1
        question += 1
        entry1.configure(bg="green")
    elif A != "D" or A != "d":
        score +=0
        question += 1
        entry1.configure(bg="red")
    if B == "G" or B == "g":
        score += 1
        question += 1
        entry2.configure(bg="green")
    elif B != "G" or B != "g":
        score +=0
        question += 1
        entry2.configure(bg="red")
    if C == "F" or B == "f":
        score +=0
        question += 1
        entry3.configure(bg="red")
    elif C != "F" or B != "f":
        score +=0
        question += 1
        entry3.configure(bg="red")
    if D == "E" or D == "e":
        score +=0
        question += 1
        entry4.configure(bg="red")
    elif D != "E" or D != "e":
        score +=0
        question += 1
        entry4.configure(bg="red")
    if E == 3:
        score +=0
        question += 1
        entry5.configure(bg="red")
    elif E != 3:
        score +=0
        question += 1
        entry5.configure(bg="red")

    output_label.configure(text=f"{ name}your score is {score}/{question}")


label = Label(frame2,text="Welcome \n please enter your name",font="Algerian 20")
label.grid(row=0, column=0)

entry = Entry(frame2)
entry.grid(row=1,column=0)

label1 = Label(frame2,text="1. who lives in the first corner",font="liberation 15")
label1.grid(row=3, column=0)

entry1 = Entry(frame2)
entry1.grid(row=3,column=1)

label2 = Label(frame2,text="2. who lives in the middle",font="liberation 15")
label2.grid(row=4, column=0)

entry2 = Entry(frame2)
entry2.grid(row=4,column=1)

label3 = Label(frame2,text="3. enter the person who live between B and G",font="liberation 15")
label3.grid(row=5, column=0)

entry3 = Entry(frame2)
entry3.grid(row=5,column=1)

label4 = Label(frame2,text="4. who is the neighbour of A",font="liberation 15")
label4.grid(row=6, column=0)
entry4 = Entry(frame2)
entry4.grid(row=6,column=1)

label5 = Label(frame2,text="5. how many houses are between A and G",font="liberation 15")
label5.grid(row=7, column=0)
entry5 = Entry(frame2)
entry5.grid(row=7,column=1)

button = Button(frame2,text="evaluate",font="liberation 15 bold",bg="red",fg="white", command=bool)
button.grid(row=8,column=0,columnspan=1)

output_label = Label(frame2,font="liberation 15 ")
output_label.grid(row=9,column=0)


show_frame(frame1)

root.mainloop()