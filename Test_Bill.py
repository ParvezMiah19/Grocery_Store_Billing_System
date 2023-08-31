import unittest


class Test_Bill(unittest.TestCase):
    
      def test_product_total_controller(self):
       print(total_bill)
        self.total_bill = Product('cosmetics_price', 'grocery_price', dry_food_price)

      def test_bill_area_controllers(self):
        print(Generate_bill)

      def test_invoice_controller(self):
        print("Customer deatails are must")
        self.save_bill_controller=  {str(self.total_bill + (self.total_bill*self.vat))} 

      def test_clear_data_controller(self):
        print(self.all_product) 

      def test_find_bill_controller(self):
        print(customer_invoice)
       
      def test_exit_app(self):
        print("Exit", "Do You reall want to exit?")

      def test_save_bill_controller(self):
        print("save Bill,", "DO you want to save the bill")
        op=messagebox.showinfo("Saved", f"Invoice No:{self.bill_no.get()} Saved Suffessfully")

if __name__ == '__main__':
  unittest.main()        



