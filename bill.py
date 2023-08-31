from tkinter import*
import math
import random
import mysql.connector
from tkinter import messagebox
import os


class Bill_app:
    def __init__(self, root):

        # ===========================MODEL PART OF (MVC)==========================
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Grocery_Billing_system")
        mycursor = mydb.cursor()
        # =============getting data for Cosmetic items============
        self.soap = IntVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='soap'")
        self.soap = mycursor.fetchall()
        self.face_cream = StringVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='face Cream'")
        self.face_cream = mycursor.fetchall()
        self.hair_gel = StringVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='Hair Gel'")
        self.hair_gel = mycursor.fetchall()
        self.loation = StringVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='Loation'")
        self.loation = mycursor.fetchall()
        self.shampoo = StringVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='Shampoo'")
        self.shampoo = mycursor.fetchall()
        self.hair_oil = StringVar()
        mycursor.execute(
            "SELECT price FROM Cosmetics_items WHERE Product_Name='Hair Oil'")
        self.hair_oil = mycursor.fetchall()
        self.cosmetics_price = StringVar()

        # ==================Getting Data for Grocery Items=================
        self.rice = list
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='Rice'")
        self.rice = mycursor.fetchall()
        self.chicken = StringVar()
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='Chicken'")
        self.Chicken = mycursor.fetchall()
        self.soyaOil = StringVar()
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='Soyabean oil'")
        self.soyaOil = mycursor.fetchall()
        self.beef = StringVar()
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='Beef'")
        self.beef = mycursor.fetchall()
        self.dal = StringVar()
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='Dal'")
        self.dal = mycursor.fetchall()
        self.onion = StringVar()
        mycursor.execute(
            "SELECT price FROM Grocery_Items WHERE Product_Name='onion'")
        self.onion = mycursor.fetchall()
        self.grocery_price = StringVar()

        # ==================Fetching data for Dry_Food=============
        self.lays = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='lays'")
        self.lays = mycursor.fetchall()
        self.pringles = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='pringles'")
        self.pringles = mycursor.fetchall()
        self.kitkat = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='kitkat'")
        self.kitkat = mycursor.fetchall()
        self.ferro = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='Ferro Rocher'")
        self.ferro = mycursor.fetchall()
        self.weafer = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='weafers'")
        self.weafer = mycursor.fetchall()
        self.snikers = StringVar()
        mycursor.execute(
            "SELECT price FROM Dry_food_Items WHERE Product_Name='snikers'")
        self.snikers = mycursor.fetchall()
        self.dry_food_price = StringVar()

        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software For grocery shop")

        # ======================= View(UI)Part of (MVC)======================
        # will be making individual frames
        bg_color = "#074463"
        fields_font = "times new roman"
        title = Label(self.root, text="Billing Software", bd=23, relief=GROOVE, bg=bg_color, fg="white", font=(
            fields_font, 30, "bold"), pady=2).pack(fill=X)

        # =================Variables=======================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.hair_gel = IntVar()
        self.loation = IntVar()
        self.shampoo = IntVar()
        self.hair_oil = IntVar()
        self.cosmetics_price = StringVar()
        self.rice = IntVar()
        self.chicken = IntVar()
        self.soyaOil = IntVar()
        self.beef = IntVar()
        self.dal = IntVar()
        self.onion = IntVar()
        self.grocery_price = StringVar()
        self.lays = IntVar()
        self.pringles = IntVar()
        self.kitkat = IntVar()
        self.ferro = IntVar()
        self.weafer = IntVar()
        self.snikers = IntVar()
        self.dry_food_price = StringVar()
        # ====this varibale is for VAT/TAX only which is 5% fixed======
        self.vat = 0.05
        # ===========Customer variables==============
        self.c_name = StringVar()
        self.c_phone = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no = StringVar()
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===========Custmer Infor label===================
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=(
            fields_font, 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        # ======for Customer name=======
        customer_label = Label(F1, text="Customer Name", bg=bg_color, fg="white",
                               font=(fields_font, 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cName_txtEntry = Entry(F1, width=20, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        # =====for Customer Phone========
        cPhone_label = Label(F1, text="Phone Number", bg=bg_color, fg="white",
                             font=(fields_font, 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cPhone_txtEntry = Entry(F1, width=20, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        # ========for Bil Search============
        c_bill_label = Label(F1, text="Bill No", bg=bg_color, fg="white",
                             font=(fields_font, 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txtEntry = Entry(F1, width=12, textvariable=self.bill_no, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)
        search_btn = Button(F1, text="Search", width=10,
                            bd=7, font="arial 12 bold").grid(row=0, column=6, padx=6, pady=10)

        # ==========Products Frame=========
        F2 = LabelFrame(self.root, text="Cosmetic Items", bd=10, relief=GROOVE, font=(
            fields_font, 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=170, width=325, height=380)

        #product = 1, Cosmetics
        soap_lbl = Label(F2, text="Bath Soap", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        # product=2, Cosmetics=================
        face_cream_lbl = Label(F2, text="Face Cream", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        #product= 3, cosmetics
        hair_gel_lbl = Label(F2, text="Men's Hair gel", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt = Entry(F2, width=10, textvariable=self.hair_gel, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        #product = 4 , cosmetics
        loation_lbl = Label(F2, text="Body Loation", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.loation, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        # product = 5, cosmetics=================
        shampoo_lbl = Label(F2, text="Shampoo", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        shampoo_txt = Entry(F2, width=10, textvariable=self.shampoo, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # product = 6 , cosmetics================
        hair_oil_lbl = Label(F2, text="Hair Oil", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        oil_txt = Entry(F2, width=10, textvariable=self.hair_oil, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # =====================Grocery Items=================
        F3 = LabelFrame(self.root, text="Grocery Items", bd=10, relief=GROOVE, font=(
            fields_font, 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=170, width=325, height=380)

        #product = 1, Grocery
        g1_lbl = Label(F3, text="Rice", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        # product=2, Grocery=================
        g2_lbl = Label(F3, text="Soyabean Oil", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.soyaOil, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        #product= 3, Grocery
        g3_lbl = Label(F3, text="Deshi Chiken(per Kg)", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.chicken, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        #product = 4 , Grocery
        g4_lbl = Label(F3, text="Booter Daal", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.dal, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        # product = 5, Grocery=================
        g5_lbl = Label(F3, text="Beef", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.beef, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # product = 6 , Grocery================
        g6_lbl = Label(F3, text="Indian Onion(per kg)", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.onion, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ====================Imported Dry Food Items===================
        F4 = LabelFrame(self.root, text="Dry Food Items", bd=10, relief=GROOVE, font=(
            fields_font, 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=170, width=325, height=380)

        #product = 1, dryFood
        f1_lbl = Label(F4, text="Lays Chips", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        f1_txt = Entry(F4, width=10, textvariable=self.lays, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        # product=2, dryFood=================
        f2_lbl = Label(F4, text="Pringles", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        f2_txt = Entry(F4, width=10, textvariable=self.pringles, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        #product= 3, dryFood
        f3_lbl = Label(F4, text="Kitkat", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        f3_txt = Entry(F4, width=10, textvariable=self.kitkat, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        #product = 4 , dryFood
        f4_lbl = Label(F4, text="Snikers", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        f4_txt = Entry(F4, width=10, textvariable=self.snikers, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        # product = 5, dryFood=================
        f5_lbl = Label(F4, text="Mama Weafers", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        f5_txt = Entry(F4, width=10, textvariable=self.weafer, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # product = 6 , dryFood================
        f6_lbl = Label(F4, text="Ferro Rocher Choco Bar", font=(
            fields_font, 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        f6_txt = Entry(F4, width=10, textvariable=self.ferro, font=(
            fields_font, 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ====================bill area=================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=400)
        bill_title = Label(
            F5, text="Invoice", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================Menu=================
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color,
                        text="Bill Menu", font=(fields_font, 15, "bold"), fg="lightgreen")
        F6.place(x=0, y=600, relwidth=1, relheight=1)

        m1_lbl = Label(F6, text="Total bill for Cosmatic items", font=(
            fields_font, 14, "bold"), bg=bg_color, fg="white").grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetics_price, font="arial 10 bold", bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total bill for Grocery items", font=(
            fields_font, 14, "bold"), bg=bg_color, fg="white").grid(row=1, column=0, padx=10, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total bill for Dry items", font=(
            fields_font, 14, "bold"), bg=bg_color, fg="white").grid(row=3, column=0, padx=10, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.dry_food_price, font="arial 10 bold", bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=1)

        vat_lbl = Label(F6, text="5% Vat will be Added", font=(
            fields_font, 17, "bold"), bg=bg_color, fg="white").grid(row=0, column=2, padx=10, pady=1)

       
        # =============== for the buttons on the menu==============
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=740, width=585, relheight=1)

        total_btn = Button(btn_f, text="make Total", command=self.product_total_controller, font=("arial", 17, "bold"), bg="cadetblue",
                           fg="black", pady=15).grid(row=0, column=10, padx=5, pady=5)

        generate_btn = Button(btn_f, text="Generate Bill", command=self.invoice_controller, font=("arial", 17, "bold"), bg="cadetblue",
                              fg="black", pady=15).grid(row=0, column=11, padx=5, pady=5)

        Clear_btn = Button(btn_f, text="Clear", font=("arial", 17, "bold"), bg="cadetblue",
                           fg="black", command=self.clear_data_controller, pady=15).grid(row=0, column=12, padx=5, pady=5)

        Exit_btn = Button(btn_f, text="Exit", command=self.exit_app, font=("arial", 17, "bold"), bg="cadetblue",
                          fg="black", pady=15).grid(row=0, column=13, padx=5, pady=5)
        self.bill_area_controllers()

    # ====================controllerS of (MVC)=========================

    def product_total_controller(self):
        # self.cosmetic_p=[]
        self.total_bill = 0
        self.c_soap_p = self.soap.get()*40 
        self.f_c_p = (self.face_cream.get()*300)
        self.l_p = (self.loation.get()*250)
        self.h_g_p = (self.hair_gel.get()*220)
        self.h_o_p = (self.hair_oil.get()*80)
        self.sham_p = (self.shampoo.get()*400)
        # self.cosmetic_p=[self.c_soap_p,self.f_c_p,self.l_p,self.h_g_p,self.]

        self.total_cosmetics_price = float(self.c_soap_p +
                                          self.f_c_p +
                                          self.l_p +
                                          self.h_g_p +
                                          self.h_o_p +
                                          self.sham_p
                                          )
        self.total_bill = self.total_bill+self.total_cosmetics_price
        self.cosmetics_price.set("BDT "+str(self.total_cosmetics_price))

        self.rice_p = (self.rice.get()*30)
        self.daal_p = (self.dal.get()*300)
        self.chicken_p = (self.chicken.get()*300)
        self.beef_p = (self.beef.get()*550)
        self.onion_p = (self.onion.get()*80)
        self.soya_p = (self.soyaOil.get()*340)

        self.total_grocery_price = (self.rice_p +
                                    self.daal_p +
                                    self.chicken_p +
                                    self.beef_p +
                                    self.onion_p +
                                    self.soya_p

                                    )
        self.total_bill = self.total_bill+self.total_grocery_price

        self.grocery_price.set("BDT"+str(self.total_grocery_price))

        self.pringles_p = (self.pringles.get()*180)
        self.kitkat_p = (self.kitkat.get()*30)
        self.lays_p = (self.lays.get()*25)
        self.weafer_p = (self.weafer.get()*20)
        self.snikers_p = (self.snikers.get()*50)
        self.ferro_p = (self.ferro.get()*300)
        self.total_dry_food_price = (self.pringles_p +
                                     self.kitkat_p +
                                     self.lays_p +
                                     self.weafer_p +
                                     self.snikers_p +
                                     self.ferro_p
                                     )
        self.total_bill = self.total_bill+self.total_dry_food_price

        self.dry_food_price.set("BDT"+str(self.total_dry_food_price))
        #self.total_bill = 0.0
        
# ================Bill Area controller================

    def bill_area_controllers(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome TO BRACU Grocery\n\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(
            END, f"\n====================================== ")
        self.txtarea.insert(
            END, f"\n Products\t\tQuantity\t\tPrice")
        self.txtarea.insert(
            END, f"\n =====================================")
        
        pass

    def invoice_controller(self):
        if self.c_name.get() == "" or self.c_phone.get == "":
            messagebox.showerror("Error", "Customer deatails are must")
        else:
            self.bill_area_controllers()

            # ==============for Cosmetics===============
            if self.soap.get() != 0:
                self.txtarea.insert(
                    END, f"\n Soap\t\t{self.soap.get()}\t\t{self.c_soap_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(
                    END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.f_c_p}")
            if self.hair_gel.get() != 0:
                self.txtarea.insert(
                    END, f"\n Hair gel\t\t{self.hair_gel.get()}\t\t{self.h_g_p}")
            if self.hair_oil.get() != 0:
                self.txtarea.insert(
                    END, f"\n Hair oil\t\t{self.hair_oil.get()}\t\t{self.h_o_p}")
            if self.loation.get() != 0:
                self.txtarea.insert(
                    END, f"\n Loation\t\t{self.loation.get()}\t\t{self.l_p}")
            if self.shampoo.get() != 0:
                self.txtarea.insert(
                    END, f"\n shampoo\t\t{self.shampoo.get()}\t\t{self.sham_p}")

            # ==================for Gorcery items===========
            if self.rice.get() != 0:
                self.txtarea.insert(
                    END, f"\n Rice\t\t{self.rice.get()}\t\t{self.rice_p}")
            if self.beef.get() != 0:
                self.txtarea.insert(
                    END, f"\n Beef\t\t{self.beef.get()}\t\t{self.beef_p}")
            if self.chicken.get() != 0:
                self.txtarea.insert(
                    END, f"\n Chicken\t\t{self.chicken.get()}\t\t{self.chicken_p}")
            if self.dal.get() != 0:
                self.txtarea.insert(
                    END, f"\n Dal\t\t{self.dal.get()}\t\t{self.daal_p}")
            if self.soyaOil.get() != 0:
                self.txtarea.insert(
                    END, f"\n Soyabean Oil\t\t{self.soyaOil.get()}\t\t{self.soya_p}")
            if self.onion.get() != 0:
                self.txtarea.insert(
                    END, f"\n Onion\t\t{self.onion.get()}\t\t{self.onion_p}")

            # =================for dry foods=================
            if self.pringles.get() != 0:
                self.txtarea.insert(
                    END, f"\n Pringles\t\t{self.pringles.get()}\t\t{self.pringles_p}")
            if self.kitkat.get() != 0:
                self.txtarea.insert(
                    END, f"\n kitkat\t\t{self.kitkat.get()}\t\t{self.kitkat_p}")
            if self.weafer.get() != 0:
                self.txtarea.insert(
                    END, f"\n Mama weafers\t\t{self.weafer.get()}\t\t{self.weafer_p}")
            if self.lays.get() != 0:
                self.txtarea.insert(
                    END, f"\n Lays\t\t{self.lays.get()}\t\t{self.lays_p}")
            if self.ferro.get() != 0:
                self.txtarea.insert(
                    END, f"\n Ferro Rocher\t\t{self.ferro.get()}\t\t{self.ferro_p}")
            if self.snikers.get() != 0:
                self.txtarea.insert(
                    END, f"\n Snikers\t\t{self.snikers.get()}\t\t{self.snikers_p}")
                

            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Total : \t\t\t    Tk. {str(self.total_bill)}") 
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Vat(5%) : \t\t\t    pct. {str(self.vat)}") 
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill(incl.VAT) : \t\t\tTk. {str(self.total_bill + (self.total_bill*self.vat))}") 
           
            self.save_bill_controller()

    # =================Clear Field controller==================

    def clear_data_controller(self):
        self.soap.set(0)
        self.face_cream.set(0)
        self.hair_gel.set(0)
        self.loation.set(0)
        self.shampoo.set(0)
        self.hair_oil.set(0)
        self.cosmetics_price.set("")
        self.rice.set(0)
        self.chicken.set(0)
        self.soyaOil.set(0)
        self.beef.set(0)
        self.dal.set(0)
        self.onion.set(0)
        self.grocery_price.set("")
        self.lays.set(0)
        self.pringles.set(0)
        self.kitkat.set(0)
        self.ferro.set(0)
        self.weafer.set(0)
        self.snikers.set(0)
        self.dry_food_price.set("")
        # ===========Customer variables==============
        self.c_name.set("")
        self.c_phone.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
    # ============Find Bill controller==========================

    def find_bill_controller(self):
        present = "no"
        for i in os.listdir("Customer's_invoice/"):
            if i.split('.'[0] == self.search_bill.get()):
                f1 = open("Customer's_invoice/{i}", "w")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, f1)
                f1.close()
                present = "yes"
            if present == "no":
                messagebox.showerror("Error", "invalid bill Number")

    # ==============Exit App=======================
    def exit_app(self):
        op = messagebox.askyesnocancel("Exit", "Do You reall want to exit?")
        if op > 0:
            self.root.destroy()

    # =============Save bill controller=============
    def save_bill_controller(self):
        op = messagebox.askyesno("save Bill,", "DO you want to save the bill")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Customer's_invoice" +
                      str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo(
                "Saved", f"Invoice No:{self.bill_no.get()} Saved Suffessfully")
        else:
            return


root = Tk()
obj = Bill_app(root)
root.mainloop()
