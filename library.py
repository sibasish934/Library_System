#creating a library management system
#========================== LIBRARY MANAGEMENT SYSTEM ========================================
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class libraryManagementsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1450x800+0+0")

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", font=("Times new Roman",50,"bold"), bd=20,bg="#7cd9c3",fg="black",relief=RIDGE,padx=2,pady=6)
        lbltitle.pack(side=TOP,fill="x")

        frame = Frame(self.root,bd=12,bg="powder blue",relief=RIDGE,padx=20)
        frame.place(x=0,y=130,width=1400,height=300)
#================================ varibles ==================================================================
        self.member_var = StringVar()
        self.sicno_var = StringVar()
        self.name_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.title_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.daysonbooks_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.latefine_var = StringVar()

        #=============================DataFrameleft==========================================
        dataframeleft = LabelFrame(frame,bd=12,text="Member Details", font=("Times new Roman",15,"bold"),bg="#7cd9c3",fg="green",relief=RIDGE)
        dataframeleft.place(x=0,y=5,width=650,height=267)

        lblmember = Label(dataframeleft,text="Member",bg="#7cd9c3",fg="black",font=("Arial",10,"bold"),padx= 2,pady= 6)
        lblmember.grid(row = 0,column = 0,sticky= "w")

        comMember= ttk.Combobox(dataframeleft,textvariable=self.member_var,font=("Arial",10,"bold"),width=19,state="readonly")
        comMember["value"] = ("Admin", "Student", "lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblsic_no = Label(dataframeleft,text="Sic-No",bg="#7cd9c3",fg="black",font=("Arial",10,"bold"),padx= 2,pady= 6)
        lblsic_no.grid(row=1,column=0,sticky = "w")
        txtsic_no = Entry(dataframeleft,textvariable=self.sicno_var,font=("Arial",10,"bold"),width = 19)
        txtsic_no.grid(row=1,column= 1)

        lblName = Label(dataframeleft, text="Name", bg="#7cd9c3", fg="black",font=("Arial", 10, "bold"), padx=2, pady=6)
        lblName.grid(row=2, column=0, sticky="w")
        txtName = Entry(dataframeleft,textvariable=self.name_var, font=("TArial", 10, "bold"), width=19)
        txtName.grid(row=2, column=1)

        lblAddress1 = Label(dataframeleft, text="Address", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=3, column=0, sticky="w")

        txtAddress1 = Entry(dataframeleft,textvariable=self.address1_var ,font=("Arial", 10, "bold"), width=19)
        txtAddress1.grid(row=3, column=1)

        lblAddress2 = Label(dataframeleft, text="Address", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=4, column=0, sticky="w")
        txtAddress2 = Entry(dataframeleft,textvariable=self.address2_var, font=("Arial", 10, "bold"), width=19)
        txtAddress2.grid(row=4, column=1)

        lblMobile = Label(dataframeleft, text="Mobile-no", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky="w")
        txtMobile = Entry(dataframeleft,textvariable=self.mobile_var ,font=("Arial", 10, "bold"), width=19)
        txtMobile.grid(row=5, column=1)

        lblBookid = Label(dataframeleft, text="BOOK-ID", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblBookid.grid(row=6, column=0, sticky="w")
        txtBookid = Entry(dataframeleft,textvariable=self.bookid_var ,font=("Arial", 10, "bold"), width=19)
        txtBookid.grid(row=6, column=1)

        lblbooktitle = Label(dataframeleft, text="Title", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblbooktitle.grid(row=0, column=2, sticky="w")
        txtBooktitle = Entry(dataframeleft,textvariable=self.title_var ,font=("Arial", 10, "bold"), width=22)
        txtBooktitle.grid(row=0, column=3)

        lblAuthor = Label(dataframeleft, text="Author", bg="#7cd9c3", fg="black",
                          font=("Arial",10,"bold"), padx=2, pady=6)
        lblAuthor.grid(row=1, column=2 ,sticky="w")
        txtauthor = Entry(dataframeleft,textvariable=self.author_var ,font=("Arial", 10, "bold"), width=19)
        txtauthor.grid(row=1, column=3)

        lbldateborrowed = Label(dataframeleft, text="Date", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lbldateborrowed.grid(row=2, column=2, sticky="w")
        txtdateborrowed = Entry(dataframeleft,textvariable=self.dateborrowed_var,font=('Arial', 10, "bold"), width=19)
        txtdateborrowed.grid(row=2, column=3)

        lblDatedue = Label(dataframeleft, text="Date-Due", bg="#7cd9c3", fg="black",
                          font=("Arial", 10, "bold"), padx=2, pady=6)
        lblDatedue.grid(row=3, column=2, sticky="w")
        txtDatedue = Entry(dataframeleft,textvariable=self.date_due_var,font=("Arial", 10, "bold"), width=19)
        txtDatedue.grid(row=3, column=3)

        lblDays_on_books = Label(dataframeleft, text="Date-on-Books", bg="#7cd9c3", fg="black",
                           font=("Arial", 10, "bold"), padx=2, pady=6)
        lblDays_on_books.grid(row=4, column=2, sticky="w")
        txtDays_on_books = Entry(dataframeleft,textvariable=self.daysonbooks_var,font=("Arial", 10, "bold"), width=19)
        txtDays_on_books.grid(row=4, column=3)

        lblDays_overdue = Label(dataframeleft, text="Date-OverDue", bg="#7cd9c3", fg="black",
                                 font=("Arial", 10, "bold"), padx=2, pady=6)
        lblDays_overdue.grid(row=5, column=2, sticky="w")
        txtDays_overdue = Entry(dataframeleft,textvariable=self.dateoverdue_var,font=("Arial", 10, "bold"), width=19)
        txtDays_overdue.grid(row=5, column=3)

        lbllatefee = Label(dataframeleft, text="Late-Fine", bg="#7cd9c3", fg="black",
                               font=("Arial", 10, "bold"), padx=2, pady=6)
        lbllatefee.grid(row=6, column=2, sticky="w")
        txtlatefee = Entry(dataframeleft,textvariable=self.latefine_var ,font=("Arial", 10, "bold"), width=19)
        txtlatefee.grid(row=6, column=3)

        #===============================DataframeRight======================================

        dataframeright = LabelFrame(frame, bd=12,text="Book Details", font=("Times new Roman", 15, "bold"),
                                   bg="#7cd9c3", fg="green", relief=RIDGE)
        dataframeright.place(x=660, y=4, width=550, height=267)

        self.txtbox = Text(dataframeright,font=("Arial",10,"bold"),width=45,height=12,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listBook = ["Python for everybody","Data-structures","Engineering Maths","Engineering Chemistry","Advanced Python",
                    "Basic Electronics","Semiconductors","Engineering Physics","Tech Magazines","Cloud Computing","Machine Learning",
                    "Artificial Intelligence","Programing with c","Advanced JavaScript","Java Programming","learn Basics Data structures",
                    "Data Structures by GauPai"]

        def selectbook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Python for everybody":
                self.bookid_var.set("PFE3456")
                self.title_var.set("Python For Everybody")
                self.author_var.set("Paul Berry")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Data-structures":
                self.bookid_var.set("DS19786")
                self.title_var.set("Data-structures")
                self.author_var.set("Sam Sinha")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Engineering Maths":
                self.bookid_var.set("EM12345")
                self.title_var.set("Engineering Maths")
                self.author_var.set("Erwin Kreyzig")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Engineering Chemistry":
                self.bookid_var.set("EC23345")
                self.title_var.set("Engineering Chemistry")
                self.author_var.set("Siba Prasad Nayak")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Advanced Python":
                self.bookid_var.set("APJ4563")
                self.title_var.set("Advanced Python")
                self.author_var.set("Amit Kumar")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Basic Electronics":
                self.bookid_var.set("BET5463")
                self.title_var.set("Basic Electronics")
                self.author_var.set("Ram Prasad Panda")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Semiconductors":
                self.bookid_var.set("SEM7865")
                self.title_var.set("Semiconductors")
                self.author_var.set("S.Chand")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")

            elif x == "Engineering Physics":
                self.bookid_var.set("EPJ9325")
                self.title_var.set("Engineering Physics")
                self.author_var.set("Bipin Tripathy")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")

            elif x == "Tech Magazines":
                self.bookid_var.set("TMY6783")
                self.title_var.set("Tech Magazines")
                self.author_var.set("Ankur Warikoo")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")

            elif x == "Cloud Computing":
                self.bookid_var.set("CCF5536")
                self.title_var.set("Cloud Computing")
                self.author_var.set("Devjyoti Mohanty")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Machine Learning":
                self.bookid_var.set("MLG5467")
                self.title_var.set("Machine Learning")
                self.author_var.set("Raj Kishore Swain")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Artificial Intelligence":
                self.bookid_var.set("AIR2346")
                self.title_var.set("Artificial Intelligence")
                self.author_var.set(" Stuart Russell ")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Programing with c":
                self.bookid_var.set("PWC9876")
                self.title_var.set("Programing with c")
                self.author_var.set("Dennis Ritchie")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Advanced JavaScript":
                self.bookid_var.set("AJX1234")
                self.title_var.set("Advanced Javascript")
                self.author_var.set("David Herman")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Java Programming":
                self.bookid_var.set("JPV4536")
                self.title_var.set("Java Programming")
                self.author_var.set("James Gosling")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")
            elif x == "Data Structures by GauPai":
                self.bookid_var.set("DSG576")
                self.title_var.set("Data Structures by GauPai")
                self.author_var.set("GauPai")
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=20)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.daysonbooks_var.set("15 days")
                self.latefine_var.set("RS.50")
                self.dateoverdue_var.set("No")

        listBox=Listbox(dataframeright,font=("Arial",10,"bold"),width=20,height=12)
        listBox.bind("<<ListboxSelect>>",selectbook)
        listBox.grid(row=0,column=0,padx=4)

        srollbar = Scrollbar(dataframeright)
        srollbar.grid(row=0,column=1,sticky="ns")
        srollbar.config(command=listBox.yview)
        for item in listBook:
            listBox.insert(END,item)


        #=============================buttons====================================================

        framebutton =Frame(self.root,bd=12,bg="#7cd9c3",relief=RIDGE,padx=20)
        framebutton.place(x=0,y=430,width=1400,height=70)

        btnaddData=Button(framebutton,text="ADD Data",command=self.add_data,font=("Arial",12,"bold"),width = 20,bg="black",fg="white")
        btnaddData.grid(row=0,column = 0)

        btnaddData = Button(framebutton,command=self.show_data, text="Show Data", font=("Arial", 12, "bold"), width=20, bg="black", fg="white")
        btnaddData.grid(row=0, column=1)

        btnaddData = Button(framebutton,command=self.update_data, text="Update Data", font=("Arial", 12, "bold"), width=20, bg="black", fg="white")
        btnaddData.grid(row=0, column=2)

        btnaddData = Button(framebutton,command=self.reset_data, text="Reset Data", font=("Arial", 12, "bold"), width=20, bg="black", fg="white")
        btnaddData.grid(row=0, column=3)

        btnaddData = Button(framebutton,command=self.delete_data, text="Delete Data", font=("Arial", 12, "bold"), width=20, bg="black", fg="white")
        btnaddData.grid(row=0, column=4)

        btnaddData = Button(framebutton,command=self.exit_data, text="Exit", font=("Arial", 12, "bold"), width=20, bg="black", fg="white")
        btnaddData.grid(row=0, column=5)

        #===========================Information Details========================================
        framedata = Frame(self.root, bd=12,bg="#7cd9c3", relief=RIDGE, padx=20)
        framedata.place(x=0, y=500, width=1300, height=150)

        table_frame=Frame(framedata, bd=6, relief=SUNKEN, bg="white")
        table_frame.place(x=0, y=2, width=1250, height=120)

        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        xscroll.pack(side=BOTTOM, fill="x")
        yscroll.pack(side=RIGHT, fill="y")

        self.library_table = ttk.Treeview(table_frame,column=("member type","sicno","name","Address1","Address2","Mobile no",
                                                            "Book Id","Title","Author","Date","Date-due","Days-on-Books",
                                                            "Date-OverDue","Late-Fine"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("member type",text="Member")
        self.library_table.heading("sicno", text="Sic-NO")
        self.library_table.heading("name", text="Name")
        self.library_table.heading("Address1", text="Address")
        self.library_table.heading("Address2", text="Address")
        self.library_table.heading("Mobile no", text="Mobile-no")
        self.library_table.heading("Book Id", text="Book-Id")
        self.library_table.heading("Title", text="Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Date", text="Date-borrowed")
        self.library_table.heading("Date-due", text="Date_due")
        self.library_table.heading("Days-on-Books", text="DaysonBooks")
        self.library_table.heading("Date-OverDue", text="Date-overDue")
        self.library_table.heading("Late-Fine", text="late-Fine")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("member type", width=125)
        self.library_table.column("sicno", width=100)
        self.library_table.column("name", width=100)
        self.library_table.column("Address1", width=100)
        self.library_table.column("Address2", width=100)
        self.library_table.column("Mobile no", width=100)
        self.library_table.column("Book Id", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Date", width=100)
        self.library_table.column("Date-due", width=100)
        self.library_table.column("Days-on-Books", width=100)
        self.library_table.column("Date-OverDue", width=100)
        self.library_table.column("Late-Fine", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="sibu@123",database="database1")
        mycursor = conn.cursor()
        mycursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),
        self.sicno_var.get(),self.name_var.get(),self.address1_var.get(),self.address2_var.get(),self.mobile_var.get(),
        self.bookid_var.get(),self.title_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.date_due_var.get(),
        self.daysonbooks_var.get(),self.dateoverdue_var.get(),self.latefine_var.get()))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("success","Member Has been added to the database successfully!!!")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="sibu@123",database="database1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        if rows != 0:
            self.library_table.delete(* self.library_table.get_children())
        for i in rows:
            self.library_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.sicno_var.set(row[1])
        self.name_var.set(row[2])
        self.address1_var.set(row[3])
        self.address2_var.set(row[4])
        self.mobile_var.set(row[5])
        self.bookid_var.set(row[6])
        self.title_var.set(row[7])
        self.author_var.set(row[8])
        self.dateborrowed_var.set(row[9])
        self.date_due_var.set(row[10])
        self.daysonbooks_var.set(row[11])
        self.dateoverdue_var.set(row[12])
        self.latefine_var.set(row[13])

    def show_data(self):
        self.txtbox.insert(END, "Member Type:-\t\t" + self.member_var.get() + "\n")
        self.txtbox.insert(END, "Sic-no:-\t\t" + self.sicno_var.get() + "\n")
        self.txtbox.insert(END, "Name:-\t\t" + self.name_var.get() + "\n")
        self.txtbox.insert(END, "Address:-\t\t" + self.address1_var.get() + "\n")
        self.txtbox.insert(END, "\t\t"+ self.address2_var.get() + "\n")
        self.txtbox.insert(END, "Mobile:-\t\t" + self.mobile_var.get() + "\n")
        self.txtbox.insert(END, "Book-ID:-\t\t" + self.bookid_var.get() + "\n")
        self.txtbox.insert(END, "Title:-\t\t" + self.title_var.get() + "\n")
        self.txtbox.insert(END, "Author:-\t\t" + self.author_var.get() + "\n")
        self.txtbox.insert(END, "Date-Borrowed:-\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END, "Date-Due:-\t\t" + self.date_due_var.get() + "\n")
        self.txtbox.insert(END, "Days With Book:-\t\t" + self.daysonbooks_var.get() + "\n")
        self.txtbox.insert(END, "Date-OverDue:-\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtbox.insert(END, "late-fee:-\t\t" + self.latefine_var.get() + "\n")


    def exit_data(self):
        exit_class = tkinter.messagebox.askyesno("libraryManagementSystem","Do you want to exit")
        if exit_class > 0:
            self.root.destroy()
            return
    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="sibu@123", database="database1")
        mycursor = conn.cursor()
        mycursor.execute(("update library set Member=%s,name=%s,Address1=%s,Address2=%s,mobile=%s,bookid=%s,booktitle=%s,"
                         "author=%s,dateborrowed=%s,Datedue=%s,Daysonbook=%s,dateOverdue=%s,latefine=%s where Sicno=%s"),
                         (self.member_var.get(),self.name_var.get(),self.address1_var.get(),self.address2_var.get(),self.mobile_var.get(),
        self.bookid_var.get(),self.title_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.date_due_var.get(),
        self.daysonbooks_var.get(),self.dateoverdue_var.get(),self.latefine_var.get(),self.sicno_var.get()))
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()

        messagebox.showinfo("success","Member has been updated successfully")



    def reset_data(self):
        self.member_var.set("")
        self.sicno_var.set("")
        self.name_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.title_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.date_due_var.set("")
        self.daysonbooks_var.set("")
        self.dateoverdue_var.set("")
        self.latefine_var.set("")
        self.txtbox.delete("1.0",END)

    def delete_data(self):
        if self.sicno_var.get() == "":
            messagebox.showerror("error","First select the Member you want to delete")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="sibu@123", database="database1")
            mycursor = conn.cursor()
            items_deleted = "delete from library where Sicno=%s"
            value = (self.sicno_var.get(),)
            mycursor.execute(items_deleted,value)
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            messagebox.showinfo("success","Member has been deleted Successfully")

if __name__ == '__main__':
    root = Tk()
    obj = libraryManagementsystem(root)
    root.mainloop()
