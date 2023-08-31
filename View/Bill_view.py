from tkinter import*
import math
import random
import mysql.connector
from tkinter import messagebox
import os


class Bill_view:
    def __init__(self, root):
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