from tkinter import*
import math
import random
import mysql.connector
from tkinter import messagebox
import os


class Bill_model:
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