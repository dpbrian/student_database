#frontend

from tkinter import*
import tkinter.messagebox
import backend

class Student:

    def __init__(self, root): #what does this mean?
        self.root = root 
        self.root.title("Student Database Management System")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        #==================================== Functions ======================================#
        def exitFunc():
            exitFunc = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if exitFunc > 0:
                root.destroy()
            return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtLastname.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtgender.delete(0, END)
            self.txtaddress.delete(0, END)
            self.txtMobile.delete(0, END)

        def addData():
            if(len(StdID.get()) != 0):
                backend.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(),\
                                    Address.get(), Mobile.get())
                studentlist.delete(0,END) #what ever is already on the list gets deleted
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(),\
                                     Address.get(), Mobile.get()))
       
        def DisplayData():
            studentlist.delete(0,END)
            for row in backend.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd  
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, sd[2])
            self.txtLastname.delete(0, END)
            self.txtLastname.insert(END, sd[3])
            self.txtDob.delete(0, END)
            self.txtDob.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtgender.delete(0, END)
            self.txtgender.insert(END, sd[6])
            self.txtaddress.delete(0, END)
            self.txtaddress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])

        def DeleteData():
            if(len(StdID.get()) != 0):
                backend.deleteData(sd[0])
                clearData()
                DisplayData()

        #search and update are at 57:00

        #==================================== Frames ======================================#
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8 , bg="Ghost White", relief = RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTit = Label(TitleFrame, font=('arial', 47, 'bold'),
         text="Student Database Management System", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10,
         bg="Ghost White", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief = RIDGE,
         bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief = RIDGE,
         bg="Ghost White", font=('arial', 20, 'bold'), text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300,  padx=31, pady=3, relief = RIDGE,
         bg="Ghost White", font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        

        #==================================== Labels and Entry Widget ======================================#
        
        #Student ID input
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Student ID", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)

        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        #First name input
        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="First Name", padx=2, pady=4, bg="Ghost White")
        self.lblFirstname.grid(row=1, column=0, sticky=W)

        self.txtFirstname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Firstname, width=39)
        self.txtFirstname.grid(row=1, column=1)

        #Last name input
        self.lblLastname = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Last Name", padx=2, pady=4, bg="Ghost White")
        self.lblLastname.grid(row=2, column=0, sticky=W)

        self.txtLastname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Lastname, width=39)
        self.txtLastname.grid(row=2, column=1)

        #DOB input
        self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="DOB", padx=2, pady=4, bg="Ghost White")
        self.lblDob.grid(row=3, column=0, sticky=W)

        self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Dob, width=39)
        self.txtDob.grid(row=3, column=1)

        #Age input
        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Age", padx=2, pady=4, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)

        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        #Gender input
        self.lblgender = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Gender", padx=2, pady=4, bg="Ghost White")
        self.lblgender.grid(row=5, column=0, sticky=W)

        self.txtgender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Gender, width=39)
        self.txtgender.grid(row=5, column=1)

        #Address input
        self.lbladdress = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Address", padx=2, pady=4, bg="Ghost White")
        self.lbladdress.grid(row=6, column=0, sticky=W)

        self.txtaddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Address, width=39)
        self.txtaddress.grid(row=6, column=1)

        #Mobile input
        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'),
         text="Mobile", padx=2, pady=4, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)

        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),
         textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        #==================================== ListBox & ScrollBar Widget ======================================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns') #what is sticky?

        studentlist = Listbox(DataFrameRIGHT,  width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)
        

        #==================================== Button Widget ===================================================#

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.displayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.displayData.grid(row=0, column=1)

        self.clearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.clearData.grid(row=0, column=2)

        self.deleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.deleteData.grid(row=0, column=3)

        self.searchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.searchData.grid(row=0, column=4)

        self.updateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.updateData.grid(row=0, column=5)
        
        self.exitApp = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=exitFunc)
        self.exitApp.grid(row=0, column=6)

if __name__=='__main__': #what does this mean?
    root = Tk()
    application = Student(root)
    root.mainloop()

