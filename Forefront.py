from Tkinter import
#creating a blank window
root = Tk()
topFrame = Frame(root)
topFrame.pack()
#frame at the bottom of the window
bottomFrame = Frame(root)
bottomFrame.pack(side=bottom)
label_1 = Label(root, text="Enter email address"
label_2 = Label(root, text="Enter password"
entry_1 = Entry(root)
#entry_2 = Entry(root)
                
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
#grid layout used to arrange labels and entries in the interface
                
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
#allows the check button to span across to columns
c.grid(columnspan=2)
                

button1 = Button(topFrame, text="Login", fg="red")
button2 = Button(topFrame, text="Forgot Password", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)

one = Label(root, text="One", bg="black", fg="red"
one.pack()
two = Label(root, text="Two", bg="black", fg="green"
#add a parameter that fill as long as the X value of the parent
two.pack(fill=X)




#allows the window to remain on the scream until exited
root.mainloop()
