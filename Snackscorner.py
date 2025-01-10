from tkinter import *
import math,random,os
from tkinter import messagebox
from time import strftime
import tkinter.font as tkFont

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Snacks Corner")
        self.login_screen()

    def login_screen(self):
        """Display the login screen."""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Variables
        self.username = StringVar()
        self.password = StringVar()

        # Login Frame
        login_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        login_frame.place(x=250, y=150, width=500, height=300)

        Label(login_frame, text="Login System", font=("times new roman", 20, "bold"), bg="cadetblue", fg="white").pack(side=TOP, fill=X)

        # Username Label and Entry
        Label(login_frame, text="Username", font=("times new roman", 15), bg="white").place(x=50, y=70)
        Entry(login_frame, textvariable=self.username, font=("times new roman", 15), bd=3, relief=SUNKEN).place(x=50, y=100, width=300)

        # Password Label and Entry
        Label(login_frame, text="Password", font=("times new roman", 15), bg="white").place(x=50, y=140)
        Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bd=3, relief=SUNKEN).place(x=50, y=170, width=300)

        # Buttons
        Button(login_frame, text="Login", command=self.login, font=("times new roman", 14, "bold"), bg="cadetblue", fg="white").place(x=50, y=220, width=150)
        Button(login_frame, text="Exit", command=self.root.quit, font=("times new roman", 14, "bold"), bg="red", fg="white").place(x=220, y=220, width=150)

        # Time Frame
        time_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        time_frame.place(x=800, y=150, width=500, height=300)

        self.time_label = Label(time_frame, font=("times new roman", 40, "bold"), bg="white", fg="black")
        self.time_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.update_time()

    def update_time(self):
        """Update the time label every second."""
        current_time = strftime("%H:%M:%S %p")
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)

    def login(self):
        """Handle login logic."""
        user_db = {"admin": "1234", "user1": "password"}

        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        elif self.username.get() in user_db and self.password.get() == user_db[self.username.get()]:
            messagebox.showinfo("Success", "Login Successful!")
            self.billing_screen()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def billing_screen(self):
        """Display the billing application."""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
#------------------------------------------------------------------------------------------#
        # Billing Screen Title
        bg_color = "#FFF8E1"
        title = Label(self.root, text="Vishal Snacks Corner", bd=12, relief=GROOVE, bg=bg_color, fg="#FF5722",
                      font=("Georgia", 30, "bold"), pady=2).pack(fill=X)
        #=================Variables===================#
        #=========Top Menu========#
        self.vadapav=IntVar()
        self.samosa=IntVar()
        self.SamosaPav=IntVar()
        self.Manchuriyan=IntVar()
        self.ManchuriyanPav=IntVar()
        self.bhajiPav=IntVar()
        self.bhaji=IntVar()
        self.Pattice=IntVar()
        #========Chaat==========#
        self.Panipuri=IntVar()
        self.Sukhapuri=IntVar()
        self.Sevpuri=IntVar()
        self.Dahipuri=IntVar()
        self.Chainese_Bhel=IntVar()
        self.Sukhabhel=IntVar()
        self.Gilabhel=IntVar()
        self.Ragdapuri=IntVar()
        #=======Top Snacks========#
        self.Sada_sandwich=IntVar()
        self.Toast_sandwich=IntVar()
        self.Cheese_Toast=IntVar()
        self.Cheese_Grilled=IntVar()
        self.Veg_burger=IntVar()
        self.Veg_Frankie=IntVar()
        self.Veg_Noodles=IntVar()
        self.Cheese_pizza=IntVar()
        #========Total Product Price & Tax variable========#
        self.Menu_price=StringVar()
        self.Chaat_price=StringVar()
        self.Snacks_price=StringVar()

        self.Menu_tax=StringVar()
        self.Chaat_tax=StringVar()
        self.Top_Snacks_tax=StringVar()

        #======customer=======#
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))


        #=====Top-Menu-Frame======
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Menu",font=("times new roman",15,"bold"),fg="#FF9800",bg=bg_color)
        F2.place(x=5,y=80,width=340,height=480)

        Vadapav_lbl=Label(F2,text="Vadapav",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Vadapav_txt=Entry(F2,width=10,textvariable=self.vadapav,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Samosa_lbl=Label(F2,text="Samosa",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Samosa_txt=Entry(F2,width=10,textvariable=self.samosa,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Samosa_Pav_lbl=Label(F2,text="Samosa Pav",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Samosa_Pav_txt=Entry(F2,width=10,textvariable=self.SamosaPav,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Manchuriyan_s_lbl=Label(F2,text="Manchuriyan",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Manchuriyan_s_txt=Entry(F2,width=10,textvariable=self.Manchuriyan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Manchuriyan_Pav_lbl=Label(F2,text="Manchuriyan Pav",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Manchuriyan_Pav_txt=Entry(F2,width=10,textvariable=self.ManchuriyanPav,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Bhaji_Pav=Label(F2,text="Bhaji pav",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Bhaji_Pav=Entry(F2,width=10,textvariable=self.bhajiPav,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        bhaji_lbl=Label(F2,text="Bhaji Plate",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        bhaji_txt=Entry(F2,width=10,textvariable=self.bhajiPav,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        Pattice_lbl=Label(F2,text="Pattice",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        Pattice_txt=Entry(F2,width=10,textvariable=self.Pattice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)

        #=====Chaat-Frame======
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Chaat",font=("times new roman",15,"bold"),fg="#FF9800",bg=bg_color)
        F3.place(x=345,y=80,width=325,height=480)

        g1_lbl=Label(F3,text="Pani Puri",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.Panipuri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Sukha Puri",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.Sukhapuri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_w_lbl=Label(F3,text="Sev Puri",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_w_txt=Entry(F3,width=10,textvariable=self.Sevpuri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_s_lbl=Label(F3,text="Dahi Puri",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_s_txt=Entry(F3,width=10,textvariable=self.Dahipuri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_g_lbl=Label(F3,text="Chainese bhel",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_g_txt=Entry(F3,width=10,textvariable=self.Chainese_Bhel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Sukha Bhel",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.Sukhabhel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Gila Bhel",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.Gilabhel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Ragda Puri",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.Ragdapuri,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)

        #=====Top-Snacks-Frame=========
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Top Snacks",font=("times new roman",15,"bold"),fg="#FF9800",bg=bg_color)
        F4.place(x=670,y=80,width=340,height=480)

        c1_lbl=Label(F4,text="Sada Sandwich",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.Sada_sandwich,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Toast Sandwich",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.Toast_sandwich,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_w_lbl=Label(F4,text="Cheese Toast",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_w_txt=Entry(F4,width=10,textvariable=self.Cheese_Toast,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_s_lbl=Label(F4,text="Cheese Grilled",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_s_txt=Entry(F4,width=10,textvariable=self.Cheese_Grilled,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_g_lbl=Label(F4,text="Veg Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_g_txt=Entry(F4,width=10,textvariable=self.Veg_burger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Veg Frankie",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.Veg_Frankie,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Veg Noodles",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.Veg_Noodles,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="Cheese Pizza",font=("times new roman",16,"bold"),bg=bg_color,fg="#4E342E").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.Cheese_pizza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)

        #=========Bill Area========#
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=80,width=350,height=480)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        #=========buttonFrame============#
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="#FF9800",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Menu Price",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.Menu_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Chaat Price",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.Chaat_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Snacks Price",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.Snacks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Menu Tax",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.Menu_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Chaat Tax",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.Chaat_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Top Snacks Tax",bg=bg_color,fg="#4E342E",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.Top_Snacks_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="#795548",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="#795548",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="#795548",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="#795548",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.T_M_F1=self.vadapav.get()*15
        self.T_M_F2=self.samosa.get()*12
        self.T_M_F3=self.SamosaPav.get()*18
        self.T_M_F4=self.Manchuriyan.get()*20
        self.T_M_F5=self.ManchuriyanPav.get()*15
        self.T_M_F6=self.bhajiPav.get()*15
        self.T_M_F7=self.bhaji.get()*25
        self.T_M_F8=self.Pattice.get()*18



        self.total_Menu_price=float(
                                    self.T_M_F1+
                                    self.T_M_F2+
                                    self.T_M_F3+
                                    self.T_M_F4+
                                    self.T_M_F5+
                                    self.T_M_F6+
                                    self.T_M_F7+
                                    self.T_M_F8
                                    )
        self.Menu_price.set("₹."+str(self.total_Menu_price))
        self.c_tax=round((self.total_Menu_price*0.0),0)
        self.Menu_tax.set("₹."+str(self.c_tax))

        self.T_C_M1=self.Panipuri.get()*25
        self.T_C_M2=self.Sukhapuri.get()*25
        self.T_C_M3=self.Sevpuri.get()*35
        self.T_C_M4=self.Dahipuri.get()*35
        self.T_C_M5=self.Chainese_Bhel.get()*20
        self.T_C_M6=self.Sukhabhel.get()*30
        self.T_C_M7=self.Gilabhel.get()*35
        self.T_C_M8=self.Ragdapuri.get()*35


        self.total_chaat_price=float(
                                    self.T_C_M1+
                                    self.T_C_M2+
                                    self.T_C_M3+
                                    self.T_C_M4+
                                    self.T_C_M5+
                                    self.T_C_M6+
                                    self.T_C_M7+
                                    self.T_C_M8
                                    )
        self.Chaat_price.set("₹."+str(self.total_chaat_price))
        self.g_tax=round((self.total_chaat_price*0.0),0)
        self.Chaat_tax.set("₹."+str(self.g_tax))

        self.T_S_M1=self.Sada_sandwich.get()*35
        self.T_S_M2=self.Toast_sandwich.get()*40
        self.T_S_M3=self.Cheese_Toast.get()*60
        self.T_S_M4=self.Cheese_Grilled.get()*100
        self.T_S_M5=self.Veg_burger.get()*50
        self.T_S_M6=self.Veg_Frankie.get()*40
        self.T_S_M7=self.Veg_Noodles.get()*60
        self.T_S_M8=self.Cheese_pizza.get()*120

        self.total_TSM_price=float(         
                                    self.T_S_M1+
                                    self.T_S_M2+
                                    self.T_S_M3+
                                    self.T_S_M4+
                                    self.T_S_M5+
                                    self.T_S_M6+
                                    self.T_S_M7+
                                    self.T_S_M8
                                    )                          
        self.Snacks_price.set("₹."+str(self.total_TSM_price)) 
        self.d_tax=round((self.total_TSM_price*0.0),0)
        self.Top_Snacks_tax.set("₹."+str(self.d_tax))

        self.Total_bill=float(  self.total_Menu_price+
                                self.total_chaat_price+
                                self.total_TSM_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
        )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome Vishal Snacks Corner\n")
        self.textarea.insert(END,f"\nBill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n food item\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")
    def bill_area(self):
        if self.Menu_price.get()=="₹.0.0" and self.Chaat_price.get()=="₹.0.0" and self.Snacks_price.get()=="₹.0.0":
            messagebox.showerror("Error","No Food Item Selected !")
        else:
            self.welcome_bill()
            #===Top Menu====
            if self.vadapav.get()!=0:
                self.textarea.insert(END,f"\n Vadapav\t\t{self.vadapav.get()}\t\t{self.T_M_F1}")
            if self.samosa.get()!=0:
                self.textarea.insert(END,f"\n Samosa\t\t{self.samosa.get()}\t\t{self.T_M_F2}")
            if self.SamosaPav.get()!=0:
                self.textarea.insert(END,f"\n SamosaPav\t\t{self.SamosaPav.get()}\t\t{self.T_M_F3}")
            if self.Manchuriyan.get()!=0:
                self.textarea.insert(END,f"\n Manchuriyan\t\t{self.Manchuriyan.get()}\t\t{self.T_M_F4}")
            if self.ManchuriyanPav.get()!=0:
                self.textarea.insert(END,f"\n ManchuriyanPav\t\t{self.ManchuriyanPav.get()}\t\t{self.T_M_F5}")
            if self.bhajiPav.get()!=0:
                self.textarea.insert(END,f"\n Bhajipav\t\t{self.bhajiPav.get()}\t\t{self.T_M_F6}")
            if self.bhaji.get()!=0:
                self.textarea.insert(END,f"\n Bhajipav\t\t{self.bhaji.get()}\t\t{self.T_M_F7}")
            if self.Pattice.get()!=0:
                self.textarea.insert(END,f"\n Pattice\t\t{self.Pattice.get()}\t\t{self.T_M_F8}")

            #====Chaat====
            if self.Panipuri.get()!=0:
                self.textarea.insert(END,f"\n Panipuri\t\t{self.Panipuri.get()}\t\t{self.T_C_M1}")
            if self.Sukhapuri.get()!=0:
                self.textarea.insert(END,f"\n Sukhapuri\t\t{self.Sukhapuri.get()}\t\t{self.T_C_M2}")
            if self.Sevpuri.get()!=0:
                self.textarea.insert(END,f"\n Sevpuri\t\t{self.Sevpuri.get()}\t\t{self.T_C_M3}")
            if self.Dahipuri.get()!=0:
                self.textarea.insert(END,f"\n Dahipuri\t\t{self.Dahipuri.get()}\t\t{self.T_C_M4}")
            if self.Chainese_Bhel.get()!=0:
                self.textarea.insert(END,f"\n Chainese Bhel\t\t{self.Chainese_Bhel.get()}\t\t{self.T_C_M5}")
            if self.Sukhabhel.get()!=0:
                self.textarea.insert(END,f"\n Sukhabhel\t\t{self.Sukhabhel.get()}\t\t{self.T_C_M6}")
            if self.Gilabhel.get()!=0:
                self.textarea.insert(END,f"\n Gilabhel\t\t{self.Gilabhel.get()}\t\t{self.T_C_M7}")
            if self.Ragdapuri.get()!=0:
                self.textarea.insert(END,f"\n Ragdapuri\t\t{self.Ragdapuri.get()}\t\t{self.T_C_M8}")

            #====Top Snacks====
            if self.Sada_sandwich.get()!=0:
                self.textarea.insert(END,f"\n Sada Sandwich\t\t{self.Sada_sandwich.get()}\t\t{self.T_S_M1}")
            if self.Toast_sandwich.get()!=0:
                self.textarea.insert(END,f"\n Toast Sandwich\t\t{self.Toast_sandwich.get()}\t\t{self.T_S_M2}")
            if self.Cheese_Toast.get()!=0:
                self.textarea.insert(END,f"\n Cheese Toast\t\t{self.Cheese_Toast.get()}\t\t{self.T_S_M3}")
            if self.Cheese_Grilled.get()!=0:
                self.textarea.insert(END,f"\n Cheese Grilled\t\t{self.Cheese_Grilled.get()}\t\t{self.T_S_M4}")
            if self.Veg_burger.get()!=0:
                self.textarea.insert(END,f"\n Veg Burger\t\t{self.Veg_burger.get()}\t\t{self.T_S_M5}")
            if self.Veg_Frankie.get()!=0:
                self.textarea.insert(END,f"\n Veg Frankie\t\t{self.Veg_Frankie.get()}\t\t{self.T_S_M6}")
            if self.Veg_Noodles.get()!=0:
                self.textarea.insert(END,f"\n Veg Noodles\t\t{self.Veg_Noodles.get()}\t\t{self.T_S_M7}")
            if self.Cheese_pizza.get()!=0:
                self.textarea.insert(END,f"\n Cheese Pizza\t\t{self.Cheese_pizza.get()}\t\t{self.T_S_M8}")

            self.textarea.insert(END,f"\n--------------------------------------")
            if self.Menu_tax.get()!="₹.0.0":
                self.textarea.insert(END,f"\n Menu Tax\t\t\t{self.Menu_tax.get()}")

            if self.Chaat_tax.get()!="₹.0.0":
                self.textarea.insert(END,f"\n Chaat Tax\t\t\t{self.Chaat_tax.get()}")

            if self.Top_Snacks_tax.get()!="₹.0.0":
                self.textarea.insert(END,f"\n Top Snacks Tax\t\t\t{self.Top_Snacks_tax.get()}")

            self.textarea.insert(END,f"\n--------------------------------------")
            self.textarea.insert(END,f"\n Total Bill :\t\t\t ₹. {self.Total_bill}")
            self.textarea.insert(END,f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w",encoding="utf-8")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved Sucessfully")
        else:
            return


    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you Really want to Clear? ")
        if op>0:

            #=========Top Menus========#
            self.vadapav.set(0)
            self.samosa.set(0)
            self.SamosaPav.set(0)
            self.Manchuriyan.set(0)
            self.ManchuriyanPav.set(0)
            self.bhajiPav.set(0)
            self.bhaji.set(0)
            self.Pattice.set(0)
            #========Chaat==========#
            self.Panipuri.set(0)
            self.Sukhapuri.set(0)
            self.Sevpuri.set(0)
            self.Dahipuri.set(0)
            self.Chainese_Bhel.set(0)
            self.Sukhabhel.set(0)
            self.Gilabhel.set(0)
            self.Ragdapuri.set(0)
            #=======Top Snacks Menu========#
            self.Sada_sandwich.set(0)
            self.Toast_sandwich.set(0)
            self.Cheese_Toast.set(0)
            self.Cheese_Grilled.set(0)
            self.Veg_burger.set(0)
            self.Veg_Frankie.set(0)
            self.Veg_Noodles.set(0)
            self.Cheese_pizza.set(0)
            #========Total Product Price & Tax variable========#
            self.Menu_price.set("")
            self.Chaat_price.set("")
            self.Snacks_price.set("")

            self.Menu_tax.set("")
            self.Chaat_tax.set("")
            self.Top_Snacks_tax.set("")

            #======customer=======#
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you Really want to exit? ")
        if op>0:
            self.root.destroy()
        
# Run the application
if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()