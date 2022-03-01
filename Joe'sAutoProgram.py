import CarClass as c
import CustomerClass as cc
import ServiceQuoteClass as sqc 

Acura = c.Car("Acura","MDX","2018")
print("First Car Type:",Acura.get_make(),Acura.get_model(),Acura.get_year())


Acura.set_make("Dodge")
Acura.set_model("Challenger")
Acura.set_year("2012")

print("Second Car Type:",Acura.get_make(),Acura.get_model(),Acura.get_year())


Shreya = cc.Customer("Shreya","2115 South 11th Street","(713)614-1364")
print("First Customer Information:",Shreya.get_name(),Shreya.get_address(),Shreya.get_phone())

Shreya.set_name("Blake")
Shreya.set_address("909 Baylor Ave")
Shreya.set_phone("(832)674-8429")

print("Second Customer Information:",Shreya.get_name(),Shreya.get_address(),Shreya.get_phone())

OilChange = sqc.ServiceQuote(35,20)
print("First Customer Price:",OilChange.get_labor_charges(),OilChange.get_parts_charges(),'$',format(OilChange.get_sales_tax(),',.2f'),'$',format(OilChange.get_total_charges(),',.2f'))

OilChange.set_parts_charges(45)
OilChange.set_labor_charges(30)
print("Second Customer Price:",OilChange.get_labor_charges(),OilChange.get_parts_charges(),'$',format(OilChange.get_sales_tax(),',.2f'),'$',format(OilChange.get_total_charges(),',.2f'))
