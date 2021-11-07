from tkinter import*
from tkinter import messagebox
import tkinter as tk

#ef7d4c
window=Tk()
window.geometry("1320x350")
window.title("Inventory Management")

productid=StringVar()
productname=StringVar()
Sellingprice=StringVar()
Quantity=StringVar()

#FUNCTION TO INSERT THE DETAILS
def insert():
    #GETTING THE INPUTS
    productid=str(Product_id_entery.get()).ljust(10)
    productname=str(Product_name_entery.get()).ljust(10)
    Sellingprice=str(Selling_price_entery.get()).ljust(10)
    Quantity=str(Quantity_entery.get()).ljust(10)
    Append_product_id = open("InventoryManagement.txt", "a")
    Read_product_id = open("InventoryManagement.txt", "r")
    Check_list = Read_product_id.read()

    # IF SELLING PRICE OR QUANTITY IS  NOT A NUMBER
    if (Sellingprice.rstrip().isnumeric() == False and Quantity.rstrip().isnumeric() == False):
        messagebox.showerror("Error", "Not a number")

    # IF PRODUCT ID IS ALREADY PRESENT IN THE TEXT FILE
    elif (productid in Check_list or productname in Check_list):
        messagebox.showwarning("Duplicate", "Duplicate entry")

    #TO COUNT THE NUMBER OF LINES
    else:
        no_of_lines=0
        with open("InventoryManagement.txt","r") as f:
            for line in f:
                no_of_lines+=1
        Append_product_id.write(f"{no_of_lines+1}\t\t\t{productid}\t\t\t{productname}\t\t\t{Sellingprice}\t\t\t{Quantity}\n")
        messagebox.showinfo("Info","Details Inserted")
    Product_id_entery.delete(first=0, last=100)
    Product_name_entery.delete(first=0, last=100)
    Selling_price_entery.delete(first=0, last=100)
    Quantity_entery.delete(first=0, last=100)


#FUNCTION TO EXIT THE WINDOW
def exitwindow():
    window.destroy()

#FUNCTION TO CHECK THE DETAILS
def viewdetails():
    Show_details.delete(0.0, tk.END)
    check = open('InventoryManagement.txt', 'r')
    rest = check.read()
    for a in rest[::-1]:
        Show_details.insert(0.0, a)


#TO CLEAR THE INFO
def clear():
    Product_id_entery.delete(first=0,last=100)
    Product_name_entery.delete(first=0,last=100)
    Selling_price_entery.delete(first=0,last=100)
    Quantity_entery.delete(first=0,last=100)
    Show_details.delete(0.0,tk.END)


#FRAME OF WINDOW
Input_frame=LabelFrame(window,bd=2,text="Inventory Management",relief="solid", font=("arial", 10, "bold"))
Input_frame.pack(fill="both",expand="yes")

#TO REMOVE BORDER FROM LABEL PUT bd=0
#LABEL OF INVENTORY MANAGEMENT
"""Title1=Label(window, text="Inventory Management", width=22, fg="black", relief="solid", font=("arial", 10, "bold"))
Title1.place(x=10, y=13)
"""
#LABEL OF PRODUCT LIST
Title2=Label(window, text="Product List",width=136,height=1, fg="black", relief="solid", font=("arial", 10, "bold"))
Title2.place(x=200, y=12)

#LABEL OF PRODUCT ID
Product_id_label=Label(window, text="Product ID: ", bd=0 ,fg="black", relief="solid", font=("arial", 10, "bold"))
Product_id_label.place(x=10, y=40)

#LABEL OF PRODUCT NAME
Product_name_label=Label(window, text="Product Name: ",  bd=0 , fg="black", relief="solid", font=("arial", 10, "bold"))
Product_name_label.place(x=10, y=100)

#LABEL OF SELLING PRICE
Product_name_label=Label(window, text="Selling Price: ", bd=0 ,  fg="black", relief="solid", font=("arial", 10, "bold"))
Product_name_label.place(x=10, y=155)

#LABEL OF QUANTITY
Product_name_label=Label(window, text="Quantity: ",  bd=0 , fg="black", relief="solid", font=("arial", 10, "bold"))
Product_name_label.place(x=10, y=215)

#LABEL OF PRODUCT LIST
#LABEL OF PRODUCT LIST ITEM NO
Item_no_label=Label(window, text="Item no.", width=25,fg="black", relief="solid", font=("arial", 10, "bold"))
Item_no_label.place(x=200, y=35)

#LABEL OF PRODUCT LIST PRODUCT ID
Product_list_id_label=Label(window, text="Product ID", width=26,fg="black", relief="solid", font=("arial", 10, "bold"))
Product_list_id_label.place(x=410, y=35)

#LABEL OF PRODUCT LIST NAME
Product_list_name_label=Label(window, text="Name",width=25, fg="black", relief="solid", font=("arial", 10, "bold"),)
Product_list_name_label.place(x=630, y=35)

#LABEL OF PRODUCT LIST SELLING PRICE
Product_list_name_label=Label(window, text="Selling price",width=25, fg="black", relief="solid", font=("arial", 10, "bold"))
Product_list_name_label.place(x=845, y=35)

#LABEL OF PRODUCT LIST QUANTITY
Product_list_name_label=Label(window, text="Quantity",width=29, fg="black", relief="solid", font=("arial", 10, "bold"))
Product_list_name_label.place(x=1060, y=35)

#SHOW INFORMATION
#VIEW AREA OF DETAILS
Show_details=tk.Text(window, fg="black", bg="light blue", relief="solid", width=122, height=15, font=("bold"))
Show_details.place(x=200, y=60)

#ENTRY FIELD
#ENTRY FIELD OF PRODUCT ID
Product_id_entery=Entry(window)
Product_id_entery.place(x=10,y=70)

#ENTRY FIELD OF PRODUCT NAME
Product_name_entery=Entry(window)
Product_name_entery.place(x=10,y=130)

#ENTRY FIELD OF SELLING PRICE
Selling_price_entery=Entry(window)
Selling_price_entery.place(x=10,y=185)

#ENTRY FIELD OF QUANTITY
Quantity_entery=Entry(window)
Quantity_entery.place(x=10,y=240)

#BUTTONS
#BUTTON FOR INSERTING  DETAILS
Insert_details_button=Button(window, text="Insert", width=7, fg="black", bg="aqua", font=("arial",10,"bold"),command=insert)
Insert_details_button.place(x=10,y=270)

#VIEW INFORMATION ENTERD BUTTON
Show_details_button=Button(window, text="Show", width=7, fg="black", bg="aqua", font=("arial",10,"bold"),command=viewdetails)
Show_details_button.place(x=90, y=270)

#CLEAR BUTTON
Clear_details_button=Button(window,text="Clear",width=7,fg="black",bg="orange",font=("arial",10,"bold"),command=clear)
Clear_details_button.place(x=10,y=310)

#EXIT BUTTON
Exit_button=Button(window,text="Exit",width=7,fg="black",bg="red",font=("arial",10,"bold"),command=exitwindow)
Exit_button.place(x=90,y=310)

window.mainloop()
