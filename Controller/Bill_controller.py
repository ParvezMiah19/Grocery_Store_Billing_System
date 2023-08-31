from tkinter import*
import math
import random
import mysql.connector
from tkinter import messagebox
import os


class Bill_Controller:
    #def __init__(self, root):

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