'''
Purpose         : Final project - "Sales System for ABC Stationery Shop"
Date            : 25.12.2020
'''


from tkinter import *
import tkinter.messagebox


# Create log in window

login = Tk()
login.title("ABC Stationery Shop")
login.configure(background='#a3c2ab')
login.minsize(width=500, height=450)
login.maxsize(width=600, height=600)

# create log in label

lbl0 = Label(login, bg="#a3c2ab", font="Cambria 50 bold", text="Log in ", fg="#000033")
lbl0.place(relx=0.35, rely=0.03, relwidth=0.4, relheight=0.18)

# connect sqlite3
#conn = sqlite3.connect("Sales_Data.db")
#a = conn.cursor()
# a.execute("""CREATE TABLE username_password(Positions TEXT,User_Names TEXT,Passwords TEXT)""")
# a.execute("""CREATE TABLE Price_list(Item_Type PRIMARY KEY ,Item_Name TEXT,Price CURRENCY,Aailable_Stock NUMBER,
# Total_Price CURRENCY)""")
# a.execute("""CREATE TABLE Goods_Sold_list(Item_Type PRIMARY KEY ,Item_Name TEXT,Num_of_sold_items NUMBER,Price CURRENCY)""")
# a.execute("""CREATE TABLE Inventory_list(Item_Type PRIMARY KEY ,Item_Name TEXT,Num_of_sold_items NUMBER,Update_inventory NUMBER )""")
# with conn:
# conn.execute("INSERT INTO Inventory_list(Item_Name)VALUES('Keytag')")
# conn.commit()
# conn.close()

# define user name & password label

u_name = Label(login, bg="#a3c2ab", font="impact 20", text="User Name :", fg="black")
u_name.place(relx=0.01, rely=0.3, relwidth=0.5, relheight=0.09)
password = Label(login, bg="#a3c2ab", font="impact 20", text="Password :", fg="black")
password.place(relx=0.01, rely=0.5, relwidth=0.5, relheight=0.09)

# define user name & password entry

u_name = Entry(login, width=20, bg="white")
u_name.place(relx=0.45, rely=0.3, relwidth=0.4, relheight=0.09)
password = Entry(login, width=20, bg="white")
password.place(relx=0.45, rely=0.5, relwidth=0.4, relheight=0.09)

# proceses
#1.create exit function

def back():
    ext = tkinter.messagebox.askyesno("ABC Stationery Shop", "Confirm if you want to exit")
    if ext > 0:
        login.destroy()
        return
Button(login, text="Back", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6", command=back).place(
    relx=0.2, rely=0.68, relwidth=0.2, relheight=0.06)

# create a function for log in to home window

def clicked():
    if u_name.get() == "admin" and password.get() == "admin" or u_name.get() == "ADMIN" and password.get() == "ADMIN":
        home = Tk()
        home.title("ABC Stationery Shop")
        home.configure(background='#008080')
        home.minsize(width=1100, height=700)
        home.maxsize(width=1100, height=700)

        # create a frame

        frame = Frame(home)
        frame.place(relx=0.5, rely=0, relwidth=0.7, relheight=0.999)
        lbl = Label(frame, font="Cambria 40 bold", fg="#000033", text="Welcome to \n ABC Stationery Shop !",
                    padx=0.1, pady=0.1)
        lbl.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.4)

        # img=ImageTK.PhotoImage(frame,Image.open("C:\Users\Padmasiri\Desktop\Python Project\pythonProject\New folder\
        # Logo.png"))
        # mylbl=Label(frame,image=img)
        # mylbl.place(relx=0, rely=0.5, relwidth=0.7, relheight=0.15)

        # create home page label

        lblh = Label(home, bg="#008080", font="impact 30", text="Home Page", fg="black")
        lblh.place(relx=0, rely=0.05, relwidth=0.2, relheight=0.09)

        # create a function for exit in home window

        def bck():
            ext = tkinter.messagebox.askyesno("ABC Stationery Shop", "Confirm if you want to exit")
            if ext > 0:
                home.destroy()
                return

        Button(home, text="Back", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6", command=bck).place(
            relx=0.1, rely=0.5, relwidth=0.2, relheight=0.06)

        # create payment system window with button clicked

        def clicked():
            paymentsystem = Tk()
            paymentsystem.title("ABC Stationery Shop")
            paymentsystem.configure(background='#008080')
            paymentsystem.minsize(width=1000, height=700)
            paymentsystem.maxsize(width=1000, height=700)


            titlelbl = Label(paymentsystem, font="Cambria 30 bold", fg="#000033", bg="#008080",
                             text="ABC Stationery Shop \n Sales Management System.", padx=0.1, pady=0.1)
            titlelbl.place(relx=0.17, rely=0, relwidth=0.7, relheight=0.15)
            frame1 = Frame(paymentsystem, bg="#ffccff")
            frame1.place(relx=0, rely=0.15, relwidth=0.999, relheight=0.39)

            # define 10 labels for first 10 item types & item names

            lbl = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text=" 1. CR 40pages", padx=0,
                        pady=0)
            lbl.place(relx=0, rely=0, relwidth=0.15, relheight=0.1)
            lbl2 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="2. CR 80pages", padx=0,
                         pady=0)
            lbl2.place(relx=0, rely=0.1, relwidth=0.15, relheight=0.1)
            lbl3 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="  3. CR 120pages", padx=0,
                         pady=0)
            lbl3.place(relx=0, rely=0.2, relwidth=0.15, relheight=0.1)
            lbl4 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="  4. CR 180pages", padx=0,
                         pady=0)
            lbl4.place(relx=0, rely=0.3, relwidth=0.15, relheight=0.1)
            lbl5 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="  5. CR 200pages", padx=0,
                         pady=0)
            lbl5.place(relx=0, rely=0.4, relwidth=0.15, relheight=0.1)
            lbl6 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="6. Ex 40pages", padx=0,
                         pady=0)
            lbl6.place(relx=0, rely=0.5, relwidth=0.15, relheight=0.1)
            lbl7 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="7. Ex 80pages", padx=0,
                         pady=0)
            lbl7.place(relx=0, rely=0.6, relwidth=0.15, relheight=0.1)
            lbl8 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="  8. Ex 120pages", padx=0,
                         pady=0)
            lbl8.place(relx=0, rely=0.7, relwidth=0.15, relheight=0.1)
            lbl9 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="  9. Ex 180pages", padx=0,
                         pady=0)
            lbl9.place(relx=0, rely=0.8, relwidth=0.15, relheight=0.1)
            lbl10 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text=" 10. Ex 200pages", padx=0,
                          pady=0)
            lbl10.place(relx=0, rely=0.9, relwidth=0.15, relheight=0.1)

            # define 10 entries for enter quantities

            en1 = Entry(frame1, width=20, bg="white" )
            en1.place(relx=0.17, rely=0.01, relwidth=0.05, relheight=0.08)
            en1.insert(0,int(0))
            en2 = Entry(frame1, width=20, bg="white")
            en2.place(relx=0.17, rely=0.1, relwidth=0.05, relheight=0.08)
            en2.insert(0, int(0))
            en3 = Entry(frame1, width=20, bg="white")
            en3.place(relx=0.17, rely=0.2, relwidth=0.05, relheight=0.08)
            en3.insert(0, int(0))
            en4 = Entry(frame1, width=20, bg="white")
            en4.place(relx=0.17, rely=0.3, relwidth=0.05, relheight=0.08)
            en4.insert(0, int(0))
            en5 = Entry(frame1, width=20, bg="white")
            en5.place(relx=0.17, rely=0.4, relwidth=0.05, relheight=0.08)
            en5.insert(0, int(0))
            en6 = Entry(frame1, width=20, bg="white")
            en6.place(relx=0.17, rely=0.5, relwidth=0.05, relheight=0.08)
            en6.insert(0, int(0))
            en7 = Entry(frame1, width=20, bg="white")
            en7.place(relx=0.17, rely=0.6, relwidth=0.05, relheight=0.08)
            en7.insert(0, int(0))
            en8 = Entry(frame1, width=20, bg="white")
            en8.place(relx=0.17, rely=0.7, relwidth=0.05, relheight=0.08)
            en8.insert(0, int(0))
            en9 = Entry(frame1, width=20, bg="white")
            en9.place(relx=0.17, rely=0.8, relwidth=0.05, relheight=0.08)
            en9.insert(0, int(0))
            en10 = Entry(frame1, width=20, bg="white")
            en10.place(relx=0.17, rely=0.9, relwidth=0.05, relheight=0.08)
            en10.insert(0,int(0))

            # define 10 labels for 11-20 item types & item names

            lbl11 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="11. A4 (1 sheet)")
            lbl11.place(relx=0.3, rely=0, relwidth=0.2, relheight=0.1)
            lbl12 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="12. Colour A4 (1 sheet)")
            lbl12.place(relx=0.33, rely=0.1, relwidth=0.2, relheight=0.1)
            lbl13 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="13. Writing papers")
            lbl13.place(relx=0.311, rely=0.2, relwidth=0.2, relheight=0.1)
            lbl14 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="14. Pen")
            lbl14.place(relx=0.261, rely=0.3, relwidth=0.2, relheight=0.1)
            lbl15 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="15. Gel pen")
            lbl15.place(relx=0.278, rely=0.4, relwidth=0.2, relheight=0.1)
            lbl16 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="16. Pencil")
            lbl16.place(relx=0.271, rely=0.5, relwidth=0.2, relheight=0.1)
            lbl17 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="17. Color pencil pack")
            lbl17.place(relx=0.32, rely=0.6, relwidth=0.2, relheight=0.1)
            lbl18 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="18. Eraser")
            lbl18.place(relx=0.273, rely=0.7, relwidth=0.2, relheight=0.1)
            lbl19 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="19. Pencil sharpner")
            lbl19.place(relx=0.311, rely=0.8, relwidth=0.2, relheight=0.1)
            lbl20 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="20. Ruler")
            lbl20.place(relx=0.267, rely=0.9, relwidth=0.2, relheight=0.1)

            # define entries for enter quantities

            en11 = Entry(frame1, width=20, bg="white")
            en11.place(relx=0.55, rely=0.01, relwidth=0.05, relheight=0.08)
            en11.insert(0, int(0))
            en12 = Entry(frame1, width=20, bg="white")
            en12.place(relx=0.55, rely=0.1, relwidth=0.05, relheight=0.08)
            en12.insert(0, int(0))
            en13 = Entry(frame1, width=20, bg="white")
            en13.place(relx=0.55, rely=0.2, relwidth=0.05, relheight=0.08)
            en13.insert(0, int(0))
            en14 = Entry(frame1, width=20, bg="white")
            en14.place(relx=0.55, rely=0.3, relwidth=0.05, relheight=0.08)
            en14.insert(0, int(0))
            en15 = Entry(frame1, width=20, bg="white")
            en15.place(relx=0.55, rely=0.4, relwidth=0.05, relheight=0.08)
            en15.insert(0, int(0))
            en16 = Entry(frame1, width=20, bg="white")
            en16.place(relx=0.55, rely=0.5, relwidth=0.05, relheight=0.08)
            en16.insert(0, int(0))
            en17 = Entry(frame1, width=20, bg="white")
            en17.place(relx=0.55, rely=0.6, relwidth=0.05, relheight=0.08)
            en17.insert(0, int(0))
            en18 = Entry(frame1, width=20, bg="white")
            en18.place(relx=0.55, rely=0.7, relwidth=0.05, relheight=0.08)
            en18.insert(0, int(0))
            en19 = Entry(frame1, width=20, bg="white")
            en19.place(relx=0.55, rely=0.8, relwidth=0.05, relheight=0.08)
            en19.insert(0, int(0))
            en20 = Entry(frame1, width=20, bg="white")
            en20.place(relx=0.55, rely=0.9, relwidth=0.05, relheight=0.08)
            en20.insert(0, int(0))

            # define 10 labels for "20-30" item types & item names

            lbl21 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="21. Scissors")
            lbl21.place(relx=0.679, rely=000, relwidth=0.2, relheight=0.09)
            lbl22 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="22. Highlighters")
            lbl22.place(relx=0.696, rely=0.08, relwidth=0.2, relheight=0.07)
            lbl23 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="23. Glue bottle")
            lbl23.place(relx=0.69, rely=0.16, relwidth=0.2, relheight=0.09)
            lbl24 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="24. Marker")
            lbl24.place(relx=0.673, rely=0.24, relwidth=0.2, relheight=0.09)
            lbl25 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="25. Stepler machine")
            lbl25.place(relx=0.712, rely=0.34, relwidth=0.2, relheight=0.09)
            lbl26 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="26. Stepler pin")
            lbl26.place(relx=0.69, rely=0.44, relwidth=0.2, relheight=0.09)
            lbl27 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="27. Pecil box")
            lbl27.place(relx=0.681, rely=0.54, relwidth=0.2, relheight=0.09)
            lbl28 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="28. Files")
            lbl28.place(relx=0.661, rely=0.64, relwidth=0.2, relheight=0.09)
            lbl29 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="29. Folders")
            lbl29.place(relx=0.672, rely=0.74, relwidth=0.2, relheight=0.09)
            lbl30 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="30. Key tag")
            lbl30.place(relx=0.671, rely=0.82, relwidth=0.2, relheight=0.09)
            lbl31 = Label(frame1, font="Cambria 15 ", fg="#000033", bg="#ffccff", text="31. bags")
            lbl31.place(relx=0.66, rely=0.91, relwidth=0.2, relheight=0.09)

            # define entries for enter quantities

            en21 = Entry(frame1, width=20, bg="white")
            en21.place(relx=0.93, rely=0.0, relwidth=0.05, relheight=0.07)
            en21.insert(0, int(0))
            en22 = Entry(frame1, width=20, bg="white")
            en22.place(relx=0.93, rely=0.086, relwidth=0.05, relheight=0.07)
            en22.insert(0, int(0))
            en23 = Entry(frame1, width=20, bg="white")
            en23.place(relx=0.93, rely=0.17, relwidth=0.05, relheight=0.07)
            en23.insert(0, int(0))
            en24 = Entry(frame1, width=20, bg="white")
            en24.place(relx=0.93, rely=0.26, relwidth=0.05, relheight=0.07)
            en24.insert(0, int(0))
            en25 = Entry(frame1, width=20, bg="white")
            en25.place(relx=0.93, rely=0.36, relwidth=0.05, relheight=0.07)
            en25.insert(0, int(0))
            en26 = Entry(frame1, width=20, bg="white")
            en26.place(relx=0.93, rely=0.46, relwidth=0.05, relheight=0.07)
            en26.insert(0, int(0))
            en27 = Entry(frame1, width=20, bg="white")
            en27.place(relx=0.93, rely=0.56, relwidth=0.05, relheight=0.07)
            en27.insert(0, int(0))
            en28 = Entry(frame1, width=20, bg="white")
            en28.place(relx=0.93, rely=0.67, relwidth=0.05, relheight=0.07)
            en28.insert(0, int(0))
            en29 = Entry(frame1, width=20, bg="white")
            en29.place(relx=0.93, rely=0.75, relwidth=0.05, relheight=0.07)
            en29.insert(0, int(0))
            en30 = Entry(frame1, width=20, bg="white")
            en30.place(relx=0.93, rely=0.84, relwidth=0.05, relheight=0.07)
            en30.insert(0, int(0))
            en31 = Entry(frame1, width=20, bg="white")
            en31.place(relx=0.93, rely=0.92, relwidth=0.05, relheight=0.07)
            en31.insert(0,int(0))



            # define processing labels

            num_ud_itm_l = Label(paymentsystem, font="Cambria 15 bold ", fg="#000033", bg="#008080",
                                 text="Number of Items ", padx=0, pady=0)
            num_ud_itm_l.place(relx=0.03, rely=0.58, relwidth=0.2, relheight=0.1)
            tot_lbl = Label(paymentsystem, font="Cambria 15 bold ", fg="#000033", bg="#008080",
                            text="Total quantity price ", padx=0, pady=0)
            tot_lbl.place(relx=0.53, rely=0.58, relwidth=0.219, relheight=0.09)
            disc_lbl = Label(paymentsystem, font="Cambria 15 bold ", fg="#000033", bg="#008080",
                             text="Discount price ", padx=0, pady=0)
            disc_lbl.place(relx=0.032, rely=0.66, relwidth=0.17, relheight=0.09)
            net_p_lbl = Label(paymentsystem, font="Cambria 15 bold ", fg="#000033", bg="#008080", text="Net Price ",
                              padx=0, pady=0)
            net_p_lbl.place(relx=0.529, rely=0.66, relwidth=0.13, relheight=0.1)


            # Processes
            #create a function for payment system's calculations

            def cal():
                num1=int(en1.get())
                num2=int(en2.get())
                num3=int(en3.get())
                num4 = int(en4.get())
                num5 = int(en5.get())
                num6 = int(en6.get())
                num7 = int(en7.get())
                num8 = int(en8.get())
                num9 = int(en9.get())
                num10 = int(en10.get())
                num11 = int(en11.get())
                num12 = int(en12.get())
                num13 = int(en13.get())
                num14 = int(en14.get())
                num15 = int(en15.get())
                num16 = int(en16.get())
                num17 = int(en17.get())
                num18 = int(en18.get())
                num19 = int(en19.get())
                num20 = int(en20.get())
                num21 = int(en21.get())
                num22= int(en22.get())
                num23 = int(en23.get())
                num24 = int(en24.get())
                num25 = int(en25.get())
                num26= int(en26.get())
                num27 = int(en27.get())
                num28 = int(en28.get())
                num29 = int(en29.get())
                num30= int(en30.get())
                num31 = int(en31.get())


                num_item=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15+num16+num17+num18+num19+num20+num21+num22+num23+num24+num25+num26+num27+num28+num29+num30+num31

                tot=(float(num1*40)+(num2*80)+(num3*100)+(num4*150)+(num5*180)+(num6*20)+(num7*30)+(num8*60)+(num9*80)+(num10*100)+(num11*3)+(num12*5)+(num13*180)+(num14*10)+(num15*20)+(num16*10)+(num17*100)+(num18*10)+(num20*20)+(num21*20)+(num22*100)+(num23*20)+(num24*80)+(num25*80)+(num26*50)+(num27*300)+(num28*40)+(num29*60)+(num30*10)+(num31*500))

                if tot>=3000:
                    disc=tot*0.1
                else:
                    disc=0
                netpay=tot-disc

                global item_en, home
                global tot_en
                global disc_en
                global netp_en

                # create labels for display info

                item_en = Label(paymentsystem, width=20, bg="white", text=num_item)
                item_en.place(relx=0.25, rely=0.61, relwidth=0.2, relheight=0.05)
                tot_en = Label(paymentsystem, width=20, bg="white",text=tot)
                tot_en.place(relx=0.75, rely=0.61, relwidth=0.2, relheight=0.05)
                disc_en =Label(paymentsystem, width=20, bg="white",text=disc)
                disc_en.place(relx=0.25, rely=0.69, relwidth=0.2, relheight=0.05)
                netp_en = Label(paymentsystem, width=20, bg="white",text=netpay)
                netp_en.place(relx=0.75, rely=0.69, relwidth=0.2, relheight=0.05)
                return item_en,tot_en,disc,netp_en

            # create a exit function

            def ext():
                ext = tkinter.messagebox.askyesno("ABC Stationery Shop", "Confirm if you want to exit")
                if ext > 0:
                    paymentsystem.destroy()
                    return

            # create a function for clear data

            def clear():
                en1.delete(0,100)
                en1.insert(0,int(0))
                en2.delete(0,100)
                en2.insert(0, int(0))
                en3.delete(0,100)
                en3.insert(0, int(0))
                en4.delete(0,100)
                en4.insert(0, int(0))
                en5.delete(0,100)
                en5.insert(0, int(0))
                en6.delete(0,100)
                en6.insert(0, int(0))
                en7.delete(0,100)
                en7.insert(0, int(0))
                en8.delete(0,100)
                en8.insert(0, int(0))
                en9.delete(0,100)
                en9.insert(0, int(0))
                en10.delete(0,100)
                en10.insert(0, int(0))
                en11.delete(0,100)
                en11.insert(0, int(0))
                en12.delete(0,100)
                en12.insert(0, int(0))
                en13.delete(0,100)
                en13.insert(0, int(0))
                en14.delete(0,100)
                en14.insert(0, int(0))
                en15.delete(0,100)
                en15.insert(0, int(0))
                en16.delete(0,100)
                en16.insert(0, int(0))
                en17.delete(0,100)
                en17.insert(0, int(0))
                en18.delete(0,100)
                en18.insert(0, int(0))
                en19.delete(0,100)
                en19.insert(0, int(0))
                en20.delete(0,100)
                en20.insert(0, int(0))
                en21.delete(0,100)
                en21.insert(0, int(0))
                en22.delete(0,100)
                en22.insert(0, int(0))
                en23.delete(0,100)
                en23.insert(0, int(0))
                en24.delete(0,100)
                en24.insert(0, int(0))
                en25.delete(0,100)
                en25.insert(0, int(0))
                en26.delete(0, 100)
                en26.insert(0, int(0))
                en27.delete(0, 100)
                en27.insert(0, int(0))
                en28.delete(0, 100)
                en28.insert(0, int(0))
                en29.delete(0, 100)
                en29.insert(0, int(0))
                en30.delete(0, 100)
                en30.insert(0, int(0))
                en31.delete(0, 100)
                en31.insert(0, int(0))

                item_en, tot_en, disc, netp_en=cal()
                item_en.pack_forget()
                tot_en.pack_forget()
                netp_en.pack_forget()
                return

            # define enter, back and clear buttons

            Button(paymentsystem, text="Enter", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6", command=cal).place(
                relx=0.4, rely=0.54, relwidth=0.2, relheight=0.06)


            Button(paymentsystem, text="Back", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6", command=ext).place(
                relx=0.15,rely=0.85, relwidth=0.2, relheight=0.06)
            Button(paymentsystem, text="Clear", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6",command=clear).place(
                relx=0.65,rely=0.85,relwidth=0.2,relheight=0.06)

        # define payment system button

        Button(home, text="Payment System", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6",
               command=clicked).place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.06)


    # enter invalid user name or password display messagebox

    else:
        tkinter.messagebox.askyesno("ABC Stationery Shop", "Invalid user name or password")


    home.mainloop()

# dfine continue button

Button(login, text="Continue", font="Calibri 14 bold", fg="#ffff99", bg="#00ace6", command=clicked).place(
    relx=0.6, rely=0.68, relwidth=0.2, relheight=0.06)

login.mainloop()
