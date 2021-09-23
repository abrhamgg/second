from tkinter import*
root = Tk()
root.geometry("500x500")
root.title("scenario")

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


label = Label(text="Welcome \n please enter your name",font="Algerian 20")
label.grid(row=0, column=0)

entry = Entry()
entry.grid(row=1,column=0)

label1 = Label(text="1. who lives in the first corner",font="liberation 15")
label1.grid(row=3, column=0)

entry1 = Entry()
entry1.grid(row=3,column=1)

label2 = Label(text="2. who lives in the middle",font="liberation 15")
label2.grid(row=4, column=0)

entry2 = Entry()
entry2.grid(row=4,column=1)

label3 = Label(text="3. enter the person who live between B and G",font="liberation 15")
label3.grid(row=5, column=0)

entry3 = Entry()
entry3.grid(row=5,column=1)

label4 = Label(text="4. who is the neighbour of A",font="liberation 15")
label4.grid(row=6, column=0)
entry4 = Entry()
entry4.grid(row=6,column=1)

label5 = Label(text="5. how many houses are between A and G",font="liberation 15")
label5.grid(row=7, column=0)
entry5 = Entry()
entry5.grid(row=7,column=1)

button = Button(text="evaluate",font="liberation 15 bold",bg="red",fg="white", command=bool)
button.grid(row=8,column=0,columnspan=1)

output_label = Label(font="liberation 15 ")
output_label.grid(row=9,column=0)



root.mainloop()