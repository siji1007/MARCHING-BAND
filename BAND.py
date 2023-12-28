import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Button,Entry,Frame,ttk, messagebox,Label
import mysql.connector
import pandas as pd 
import os
from email.message import EmailMessage
import smtplib
import ssl

class CustomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CNSC MARCHING BAND M-R")
        self.master.iconbitmap(r'LOGO.ico')
        self.master.geometry("800x700")
        self.master.resizable(False, False)

        self.LOGIN_FORM()
    
    #LOGOUT FUNTION TO CALL THIS ON THE LOGOUT BUTTON, DESTORY ALL WIDGETS OF THE CURRENT DISPLAY AND DISPLAY THE LOGIN FORM
    def logout(self):
    # Destroy all widgets on the main dashboard
        for widget in self.master.winfo_children():
            widget.destroy()

        # Recreate login form
        self.LOGIN_FORM()
        
    #DISPLAY THE LOGIN FORM...
    def LOGIN_FORM(self):
        original_image = Image.open("Dashboard_login.png")
        width, height = 800, 700
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        default_value_ENTRIES_username ="INPUT USERNAME"
        self.USERNAME_ENTRY = Entry(self.canvas, width=18, font=('Arial', 10,),bd=0, bg="#560F14",fg="white")
        self.USERNAME_ENTRY.place(x=345, y=320)
        self.USERNAME_ENTRY.insert(0, default_value_ENTRIES_username)
        self.USERNAME_ENTRY.bind("<FocusIn>", self.clear_default_value_LOGIN)

        
        self.PASSWORD_ENTRY = Entry(self.canvas, width=18, font=('Arial', 10,),bd=0, bg="#560F14",fg="white",show="*")
        self.PASSWORD_ENTRY.place(x=345, y=382)
        self.PASSWORD_ENTRY.bind("<FocusIn>", self.clear_default_value_LOGIN)
        
        HIDE_IMAGE =Image.open('SHOW.png')
        resize_HIDE_IMAGE = HIDE_IMAGE.resize((20,20), Image.LANCZOS)
        self.HIDE_IMAGE = ImageTk.PhotoImage(resize_HIDE_IMAGE)
        self.HIDE_IMAGE_BUTTON = Button(self.canvas, image= self.HIDE_IMAGE,bd=0,height= 20,width=20, compound='center', relief=tk.FLAT, highlightthickness=0, command=self.toggle_password_visibility)
        self.HIDE_IMAGE_BUTTON.place(x=465, y=383)


        LOGIN_IMAGE = Image.open("LOGIN_BUTTON.png")
        resized_LOGIN_image = LOGIN_IMAGE.resize((152, 23), Image.LANCZOS)
        self.LOGIN_IMAGE = ImageTk.PhotoImage(resized_LOGIN_image)
        self.LOGIN_button = Button(self.canvas, image=self.LOGIN_IMAGE, bd=0, height=23, width=152, compound='center', relief=tk.FLAT,highlightthickness=0,command=self.show)
        self.LOGIN_button.place(x=320, y=433)



        SIGNUP_IMAGE = Image.open("SIGNUP.png")
        resized_SIGNUP_image = SIGNUP_IMAGE.resize((59, 25), Image.LANCZOS)
        self.SIGNUP_IMAGE = ImageTk.PhotoImage(resized_SIGNUP_image)
        self.SIGNUP_button = Button(self.canvas, image=self.SIGNUP_IMAGE, bd=0, height=25, width=59, compound='center', relief=tk.FLAT,highlightthickness=0)
        self.SIGNUP_button.place(x=419, y=466)



    def toggle_password_visibility(self):
        current_show_state = self.PASSWORD_ENTRY.cget("show")
        if current_show_state:
            # Password is currently hidden, so show it
            self.PASSWORD_ENTRY.config(show="")
        else:
            # Password is currently shown, so hide it
            self.PASSWORD_ENTRY.config(show="*")

    #CLEAR THE SPECIFIC ENTRY ON LOGIN ENTRIES
    def clear_default_value_LOGIN(self, event):
        # Check the entry that currently has focus and clear it if necessary
        focused_entry = self.master.focus_get()

        if focused_entry == self.USERNAME_ENTRY and focused_entry.get() == "INPUT USERNAME":
            focused_entry.delete(0, tk.END)
        elif focused_entry == self.PASSWORD_ENTRY and focused_entry.get() == "INPUT PASSWORD":
            focused_entry.delete(0, tk.END)

    #SHOW THE LANDING MAIN PAGE
    def show_main_widgets(self):
        # Destroy login form widgets
        self.USERNAME_ENTRY.destroy()
        self.PASSWORD_ENTRY.destroy()
        self.LOGIN_button.destroy()

        # Create main widgets

        self.change_background("Dashboard.png")

        
        self.create_widgets_buttons()
        self.create_widgets_entry()
        self.create_widgets_treeview()
        self.update_next_member_id()

    #CHANGING THE BACKGROUND OF THE WINDOW BECAUSE THE LOGIN FORM AND MAIN PAGE ARE NOT THE SAME BACKRGROUND PNG
    def change_background(self, image_path):
        original_image = Image.open("Dashboard.png")
        width, height = 800, 700
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.bg_image_MAIN = ImageTk.PhotoImage(resized_image)

        # Delete existing canvas
        self.canvas.destroy()

        # Create a new canvas with the updated background image
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image_MAIN)

    def show(self):
        username = self.USERNAME_ENTRY.get()
        password = self.PASSWORD_ENTRY.get()
        
        if username == "ADMIN" and password == "ADMIN":
            self.show_main_widgets()

           

        else:
            # Show an error message or take other actions if login fails
            messagebox.showerror("Login Failed", "Invalid username or password.")


    #HERE'S ALL BUTTONS
    def create_widgets_buttons(self):

        #SEARCH BUTTON
        SEARCH_image = Image.open("SEARCH.png")
        resized_image = SEARCH_image.resize((50, 25), Image.LANCZOS)
        self.SEARCH_image = ImageTk.PhotoImage(resized_image)
        self.SEARCH_button = Button(self.canvas, image=self.SEARCH_image, bd=0, height=25, width=50, compound='center', relief=tk.FLAT,highlightthickness=0)
        self.SEARCH_button.place(x=506, y=75)
        self.SEARCH_button.bind("<ButtonRelease-1>", self.search_entry_by_id_and_name)


        #ADD BUTTON 
        ADD_IMAGE = Image.open("ADD_IMAGE.png")
        resized_ADD_image = ADD_IMAGE.resize((30, 25), Image.LANCZOS)
        self.ADD_IMAGE = ImageTk.PhotoImage(resized_ADD_image)
        self.ADD_button = Button(self.canvas, image=self.ADD_IMAGE, bd=0, height=25, width=30, compound='center', relief=tk.FLAT,highlightthickness=0)
        self.ADD_button.place(x=565, y=74)
        self.ADD_button.bind("<ButtonRelease-1>", self.add_member)

        #UPDATE BUTTON
        UPDATE_IMAGE = Image.open("UPDATE.png")
        resized_UPDATE_image = UPDATE_IMAGE.resize((56, 25), Image.LANCZOS)
        self.UPDATE_IMAGE = ImageTk.PhotoImage(resized_UPDATE_image)
        self.UPDATE_button = Button(self.canvas, image=self.UPDATE_IMAGE, bd=0, height=25, width=56, compound='center', relief=tk.FLAT,highlightthickness=0)
        self.UPDATE_button.place(x=600, y=74)
        self.UPDATE_button.bind("<ButtonRelease-1>", self.update_member)

        #DELETE BUTTON
        DELETE_IMAGE = Image.open("DELETE.png")
        resized_DELETE_image = DELETE_IMAGE.resize((56, 25), Image.LANCZOS)
        self.DELETE_IMAGE = ImageTk.PhotoImage(resized_DELETE_image)
        self.DELETE_button = Button(self.canvas, image=self.DELETE_IMAGE, bd=0, height=25, width=56, compound='center', relief=tk.FLAT,highlightthickness=0)
        self.DELETE_button.place(x=660, y=74)
        self.DELETE_button.bind("<ButtonRelease-1>", self.delete_member)

        #CLEAR BUTTON
        CLEAR_IMAGE = Image.open("CLEAR.png")
        resized_CLEAR_image = CLEAR_IMAGE.resize((56, 25), Image.LANCZOS)
        self.CLEAR_IMAGE = ImageTk.PhotoImage(resized_CLEAR_image)
        self.CLEAR_button = Button(self.canvas, image=self.CLEAR_IMAGE, bd=0, height=25, width=56, compound='center', relief=tk.FLAT,highlightthickness=0,command=self.clear_entries)
        self.CLEAR_button.place(x=718, y=74)

        #GENERATE BUTTON
        GENERATE_IMAGE = Image.open("GENERATE.png")
        resized_GENERATE_image = GENERATE_IMAGE.resize((100, 25), Image.LANCZOS)
        self.GENERATE_IMAGE = ImageTk.PhotoImage(resized_GENERATE_image)
        self.GENERATE_button = Button(self.canvas, image=self.GENERATE_IMAGE, bd=0, height=25, width=100, compound='center', relief=tk.FLAT,highlightthickness=0, command=lambda: self.GENERATE(selected_instrument=self.selected_instrument.get()))
        self.GENERATE_button.place(x=680, y=668)


        #LOGOUT BUTTON
        LAGOUT_IMAGE = Image.open("LOGOUT.png")
        resized_LAGOUT_image = LAGOUT_IMAGE.resize((80, 25), Image.LANCZOS)
        self.LAGOUT_IMAGE = ImageTk.PhotoImage(resized_LAGOUT_image)
        self.LAGOUT_button = Button(self.canvas, image=self.LAGOUT_IMAGE, bd=0, height=25, width=80, compound='center', relief=tk.FLAT,highlightthickness=0,command=self.logout)
        self.LAGOUT_button.place(x=700, y=8)

    
    #FUNCTION TO GENERATE THE REPORT TO EXCEL
    def GENERATE(self, selected_instrument=None):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="POGIako2003",
                database="band"
            )
            cursor = conn.cursor(dictionary=True)

            # Build the SQL query based on the selected instrument
            sql_query = """
                SELECT m.MemberID, m.MemberName, m.Gender, m.Department, m.UniformSize, m.Address, m.Age, i.Instrument, i.BandPosition
                FROM members m
                LEFT JOIN instruments i ON m.MemberID = i.MemberID
            """
            if selected_instrument and selected_instrument != "None":
                sql_query += "WHERE i.Instrument = %s"
                cursor.execute(sql_query, (selected_instrument,))
            else:
                cursor.execute(sql_query)

            rows = cursor.fetchall()

            conn.close()

            # Create a DataFrame from the fetched data
            df = pd.DataFrame(rows)

            # Specify the Excel file path
            excel_file_path = "members_data.xlsx"

            # Write the DataFrame to an Excel file
            df.to_excel(excel_file_path, index=False)
            os.system(f"start excel {excel_file_path}")

            messagebox.showinfo("Success", f"Data exported to {excel_file_path}")

            email_account=self.EMAIL_ENTRY.get()
            if email_account == "INPUT HERE" or email_account == None:
                messagebox.showinfo("Info", "Can't send the email")
                pass
            else:
                messagebox.showinfo("Info", "Done")
                self.send_excel_email(email_account, excel_file_path)



        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")


    #SEND EXCEL TO ACC
    def send_excel_email(self, recipient_email, excel_file_path):
        try:
            email_sender = 'smartcook23@gmail.com'
            email_password = 'asflajdmsabuomwh'
            subject = 'Data Export from Your App'
            body = 'Hello, THIS IS THE RECORD OF BAND MEMBERS.'

            # Create the EmailMessage object
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = recipient_email
            em['Subject'] = subject
            em.set_content(body)

            # Attach the Excel file
            with open(excel_file_path, 'rb') as f:
                attachment_data = f.read()
            filename = os.path.basename(excel_file_path)
            em.add_attachment(attachment_data, maintype='application', subtype='octet-stream', filename=filename)

            # Send the email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(em)

        except Exception as e:
            print(f"Email sending error: {e}")

        finally:
            # Remove the Excel file after sending
            os.remove(excel_file_path)

    #CLEAR ALL ENTRIES 
    def clear_entries(self):
        self.MEMBERNAME_ENTRY.delete(0, tk.END)
        self.AGE_ENTRY.delete(0, tk.END)
        self.GENDER_ENTRY.delete(0, tk.END)
        self.DEPARTMENT_ENTRY.delete(0, tk.END)
        self.UNIFORM_ENTRY.delete(0, tk.END)
        self.INSTRUMENT_ENTRY.delete(0, tk.END)
        self.POSITION_ENTRY.delete(0, tk.END)
        self.ADDRESS_ENTRY.delete(0, tk.END)


    #WIDGETS FOR ENTRIES
    def create_widgets_entry(self):
     
        

        self.SEARCH_ENTRY = Entry(self.canvas, width=16, font=('Arial', 14),bd=0, bg="#993333",fg="white")
        self.SEARCH_ENTRY.place(x=329, y=75)

    # Set default value
        self.SEARCH_ENTRY.bind("<FocusIn>", self.clear_default_value)
        self.SEARCH_ENTRY.bind("<KeyRelease>", lambda event: self.search_entry_by_id_and_name(event))
        



        #MEMBER_NAME ENTRY 
        default_value_ENTRIES ="INPUT HERE"
        self.MEMBERNAME_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.MEMBERNAME_ENTRY.place(x=58, y=183)
        self.MEMBERNAME_ENTRY.insert(0, default_value_ENTRIES)
        self.MEMBERNAME_ENTRY.bind("<FocusIn>", self.clear_default_value)



        #AGE
        self.AGE_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.AGE_ENTRY.place(x=58, y=235)
        self.AGE_ENTRY.insert(0, default_value_ENTRIES)
        self.AGE_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #GENDER
        self.GENDER_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.GENDER_ENTRY.place(x=58, y=280)
        self.GENDER_ENTRY.insert(0, default_value_ENTRIES)
        self.GENDER_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #DEPARTMENT
        self.DEPARTMENT_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.DEPARTMENT_ENTRY.place(x=57, y=332)
        self.DEPARTMENT_ENTRY.insert(0, default_value_ENTRIES)
        self.DEPARTMENT_ENTRY.bind("<FocusIn>", self.clear_default_value)


        """THIS IS THE SECOND FORM"""
        #UNIFORM SIZE
        self.UNIFORM_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.UNIFORM_ENTRY.place(x=440, y=183)
        self.UNIFORM_ENTRY.insert(0, default_value_ENTRIES)
        self.UNIFORM_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #INSTRUMENT
        self.INSTRUMENT_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.INSTRUMENT_ENTRY.place(x=440, y=235)
        self.INSTRUMENT_ENTRY.insert(0, default_value_ENTRIES)
        self.INSTRUMENT_ENTRY.bind("<FocusIn>", self.clear_default_value)


        #BAND POSITION
        self.POSITION_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.POSITION_ENTRY.place(x=440, y=280)
        self.POSITION_ENTRY.insert(0, default_value_ENTRIES)
        self.POSITION_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #ADDRESS
        self.ADDRESS_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.ADDRESS_ENTRY.place(x=440, y=332)
        self.ADDRESS_ENTRY.insert(0, default_value_ENTRIES)
        self.ADDRESS_ENTRY.bind("<FocusIn>", self.clear_default_value)

        self.selected_instrument = tk.StringVar()

        # List of instrument options
        instrument_options = ["None", "Clarinet", "Baritone", "Saxophone Soprano", "Tuba", "Trumpet", "Bass Drum", "Quintom", "Flute", "Cymbal", "Snare", "French Horn"]

        self.instrument_dropdown = ttk.Combobox(self.canvas, textvariable=self.selected_instrument, values=instrument_options, state="readonly")
        self.instrument_dropdown.set("Filter by Instruments")
        self.instrument_dropdown.place(x=650, y=412)
        self.instrument_dropdown.bind("<<ComboboxSelected>>", self.filter_by_instrument)


        email_label = tk.Label(self.canvas, text="Email:", font=('Arial', 10), bg="#560F14", fg="white")
        email_label.place(x=430, y=670)

        self.EMAIL_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#32A927",fg="white")
        self.EMAIL_ENTRY.place(x=480, y=673)
        self.EMAIL_ENTRY.insert(0, default_value_ENTRIES)
        self.EMAIL_ENTRY.bind("<FocusIn>", self.clear_default_value)




    #SHOW HERE THE TREEVIEW
    def create_widgets_treeview(self):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="POGIako2003",
                database="band"
            )
            cursor = conn.cursor(dictionary=True)

            # Updated SELECT statement to join the members and instruments tables
            cursor.execute(
                """
                SELECT m.MemberID, m.MemberName, m.Gender, m.Department, m.UniformSize, m.Address, m.Age, i.Instrument, i.BandPosition
                FROM members m
                LEFT JOIN instruments i ON m.MemberID = i.MemberID
                """
            )
            rows = cursor.fetchall()

            conn.close()

            columns = ("ID", "NAME","AGE", "GENDER", "DEPARTMENT", "UNIFORMSIZE", "ADDRESS", "INSTRUMENTS","POSITION")
            maroon_color = "#420303"

            # Create Style instance
            style = ttk.Style()
            style.configure(f"{maroon_color}.Treeview", background=maroon_color)

            # Adjusted the x-coordinate of the Treeview widget
            self.treeview = ttk.Treeview(self.canvas, columns=columns, show="headings", height=10, style=f"{maroon_color}.Treeview")
            self.treeview.place(x=5, y=435)

             # Create a vertical scrollbar
            scrollbar = ttk.Scrollbar(self.canvas, orient="vertical", command=self.treeview.yview)
            scrollbar.place(x=777, y=435, height=225)  # Adjust the x, y, and height as needed

            # Configure the Treeview to use the scrollbar
            self.treeview.configure(yscrollcommand=scrollbar.set)



            max_widths = [len(col) * 10 for col in columns]  # Initial widths based on column names

            for data in rows:
                mapped_data = [data.get(col, "") for col in columns]
                for i, value in enumerate(mapped_data):
                    max_widths[i] = max(max_widths[i], len(str(value)) * 10)

            for i, col in enumerate(columns):
                # Manually set the width for the 'MemberName' column
                if col == "NAME":
                    self.treeview.column(col, width=max_widths[i] + 100, anchor="center")
                # Manually set the width for the 'Instrument' column
                elif col in "INSTRUMENTS":
                    self.treeview.column(col, width=max_widths[i] + 20, anchor="center")
                elif col in "POSITION":
                    self.treeview.column(col, width=max_widths[i] + 30, anchor="center")
                else:
                    self.treeview.column(col, width=max_widths[i], anchor="center")
                self.treeview.heading(col, text=col)



            for data in rows:
                mapped_data = [data.get(col, "") for col in ("MemberID", "MemberName", "Age", "Gender", "Department", "UniformSize", "Address", "Instrument", "BandPosition")]
                self.treeview.insert("", tk.END, values=mapped_data, tags="white_text")

            # Define a tag with white text color
            self.treeview.tag_configure("white_text", foreground="white")

            # Correct the binding for the left mouse button release event
            self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)

        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")


    #BINDING THE TREEVIEW CLICK TO THE ENTRY BOXE'S
    def on_treeview_click(self, event):
        # Get the selected item
        selected_item = self.treeview.selection()

        if selected_item:
            # Fetch data from the selected item
            item_data = self.treeview.item(selected_item, "values")

            # Update entry widgets with selected data
            self.MEMBERNAME_ENTRY.delete(0, tk.END)
            self.MEMBERNAME_ENTRY.insert(0, item_data[1])  # FirstName
            self.AGE_ENTRY.delete(0, tk.END)
            self.AGE_ENTRY.insert(0, item_data[2])  # Age
            self.DEPARTMENT_ENTRY.delete(0, tk.END)
            self.DEPARTMENT_ENTRY.insert(0, item_data[4])  # Department
            self.POSITION_ENTRY.delete(0, tk.END)
            self.POSITION_ENTRY.insert(0, item_data[8])  # Position
            self.ADDRESS_ENTRY.delete(0, tk.END)
            self.ADDRESS_ENTRY.insert(0, item_data[6])  # Address
            #GENDER
            self.GENDER_ENTRY.delete(0, tk.END)
            self.GENDER_ENTRY.insert(0, item_data[3]) 
            #UNIFORM
            self.UNIFORM_ENTRY.delete(0, tk.END)
            self.UNIFORM_ENTRY.insert(0, item_data[5]) 
            #INSTRUMENT
            self.INSTRUMENT_ENTRY.delete(0, tk.END)
            self.INSTRUMENT_ENTRY.insert(0, item_data[7]) 
            

    #CLEAR THE VALUE ON THE SPECIFIC ENTRY WHEN I CLICK IT
    def clear_default_value(self, event):
        # Clear default value when the entry is clicked
        if self.SEARCH_ENTRY.get() == "Search" and event.widget == self.SEARCH_ENTRY:
            self.SEARCH_ENTRY.delete(0, tk.END)

        # Check the entry that currently has focus and clear it if necessary
        focused_entry = self.master.focus_get()
        if focused_entry and focused_entry != self.SEARCH_ENTRY:
            if focused_entry.get() == "INPUT HERE":
                focused_entry.delete(0, tk.END)

    #FILTERING THE SPECIFIC OPTION ON DROPDOWN AND DISPLAY IT TO TREEVIEW REALTIME
    def filter_by_instrument(self, event):
      
        selected_instrument = self.selected_instrument.get()

        # Reset the filtration if "None" is selected
        if selected_instrument == "None":
            self.search_entry_by_id_and_name(None)
            return

        # Add logic to filter the Treeview based on the selected instrument
        self.search_entry_by_id_and_name(None, selected_instrument)

        # Call the method to initially populate the Treeview with data based on the selected instrument
        if selected_instrument != "Filter by Instruments":
            self.search_entry_by_id_and_name(None, selected_instrument)
        else:
            self.search_entry_by_id_and_name(None)

    #SEARCH REALTIME BUY ID, NAME AND SELECTED OPTION ON THE DROPDOWN
    def search_entry_by_id_and_name(self, event, selected_instrument=None):
        search_term = self.SEARCH_ENTRY.get().strip()
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="POGIako2003",
                database="band"
            )
            cursor = conn.cursor(dictionary=True)

            if not search_term:
                if selected_instrument and selected_instrument != "Filter by Instruments":
                    # Filter by selected instrument
                    cursor.execute(
                        """
                        SELECT m.MemberID, m.MemberName, m.Gender, m.Department, m.UniformSize, m.Address, m.Age, i.Instrument, i.BandPosition
                        FROM members m
                        LEFT JOIN instruments i ON m.MemberID = i.MemberID
                        WHERE i.Instrument = %s
                        """,
                        (selected_instrument,)
                    )
                else:
                    # Display all records
                    cursor.execute(
                        """
                        SELECT m.MemberID, m.MemberName, m.Gender, m.Department, m.UniformSize, m.Address, m.Age, i.Instrument, i.BandPosition
                        FROM members m
                        LEFT JOIN instruments i ON m.MemberID = i.MemberID
                        """
                    )
            else:
                # Search for entries by MemberID, MemberName, or Instrument
                cursor.execute(
                    """
                    SELECT m.MemberID, m.MemberName, m.Gender, m.Department, m.UniformSize, m.Address, m.Age, i.Instrument, i.BandPosition
                    FROM members m
                    LEFT JOIN instruments i ON m.MemberID = i.MemberID
                    WHERE m.MemberID = %s OR m.MemberName LIKE %s OR i.Instrument LIKE %s
                    """,
                    (search_term, f'%{search_term}%', f'%{search_term}%')
                )
            rows = cursor.fetchall()

            conn.close()

            max_widths = [len(col) * 10 for col in ("ID", "NAME", "GENDER", "DEPARTMENT", "UNIFORMSIZE", "ADDRESS", "AGE", "INSTRUMENTS", "POSITION")]

            # Clear the Treeview
            self.treeview.delete(*self.treeview.get_children())  # Use * to unpack the tuple

            # Insert data into the Treeview
            for data in rows:
                mapped_data = [data.get(col, "") for col in ("MemberID", "MemberName", "Age", "Gender", "Department", "UniformSize", "Address", "Instrument", "BandPosition")]
                self.treeview.insert("", tk.END, values=mapped_data, tags="white_text")

        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")


    #THE INCREMENTATION OF CURRENT MAX ID REALTIME 
    def update_next_member_id(self):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="POGIako2003",
                database="band"
            )
            cursor = conn.cursor()

            # Fetch the maximum MemberID from the members table
            cursor.execute("SELECT MAX(MemberID) FROM members")
            max_member_id = cursor.fetchone()[0]

            # Set next_member_id to the maximum MemberID + 1
            self.next_member_id = max_member_id + 1 if max_member_id is not None else 1

            conn.close()

        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")

    #DYNAMICALLY UPDATE THE ID REALTIME
    def get_next_member_id(self):
        # Dynamically update the next_member_id before returning it
        self.update_next_member_id()
        return self.next_member_id

    #FUNCTION FOR UPDATE BUTTON THE CONNECTION OF PYTHON AND MARIADB
    def update_member(self, event):
        # Get the selected item
        selected_item = self.treeview.selection()

        if selected_item:
            # Fetch data from the selected item
            item_data = self.treeview.item(selected_item, "values")
            
            # Get updated data from entry widgets
            member_name = self.MEMBERNAME_ENTRY.get()
            age = self.AGE_ENTRY.get()
            gender = self.GENDER_ENTRY.get()
            department = self.DEPARTMENT_ENTRY.get()
            uniform_size = self.UNIFORM_ENTRY.get()
            instrument = self.INSTRUMENT_ENTRY.get()
            position = self.POSITION_ENTRY.get()
            address = self.ADDRESS_ENTRY.get()

            # Validate required fields (you can add more validation as needed)
            if not member_name or not age or not gender or not department:
                messagebox.showerror("Error", "Please fill in all required fields.")
                return

            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="POGIako2003",
                    database="band"
                )
                cursor = conn.cursor()

                # Update the member information
                cursor.execute(
                    """
                    UPDATE members
                    SET MemberName=%s, Age=%s, Gender=%s, Department=%s, UniformSize=%s, Address=%s
                    WHERE MemberID=%s
                    """,
                    (member_name, age, gender, department, uniform_size, address, item_data[0])  # item_data[0] is the MemberID
                )

                # Update the instrument information
                cursor.execute(
                    """
                    UPDATE instruments
                    SET Instrument=%s, BandPosition=%s
                    WHERE MemberID=%s
                    """,
                    (instrument, position, item_data[0])  # item_data[0] is the MemberID
                )

                conn.commit()

                # Update the Treeview to display the updated member
                self.search_entry_by_id_and_name(None)  # Call the search function to refresh the Treeview

                messagebox.showinfo("Success", "Member updated successfully.")

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {e}")

            finally:
                if conn:
                    conn.close()


    #ADD FUNCTION TO ADD MEMBER
    def add_member(self, event):
        # Get data from entry widgets
        member_name = self.MEMBERNAME_ENTRY.get()
        age = self.AGE_ENTRY.get()
        gender = self.GENDER_ENTRY.get()
        department = self.DEPARTMENT_ENTRY.get()
        uniform_size = self.UNIFORM_ENTRY.get()
        instrument = self.INSTRUMENT_ENTRY.get()
        position = self.POSITION_ENTRY.get()
        address = self.ADDRESS_ENTRY.get()

        # Validate required fields (you can add more validation as needed)
        if not member_name or not age or not gender or not department:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="POGIako2003",
                database="band"
            )
            cursor = conn.cursor()

            # Get the next available MemberID
            member_id = self.get_next_member_id()

            # Insert the new member information
            cursor.execute(
                """
                INSERT INTO members (MemberID, MemberName, Age, Gender, Department, UniformSize, Address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (member_id, member_name, age, gender, department, uniform_size, address)
            )

            # Insert the instrument information
            cursor.execute(
                """
                INSERT INTO instruments (MemberID, Instrument, BandPosition)
                VALUES (%s, %s, %s)
                """,
                (member_id, instrument, position)
            )

            conn.commit()

            # Append the new member directly to the Treeview
            mapped_data = (member_id, member_name, age, gender, department, uniform_size, address, instrument, position)
            self.treeview.insert("", tk.END, values=mapped_data, tags="white_text")

            messagebox.showinfo("Success", "Member added successfully.")

            self.MEMBERNAME_ENTRY.delete(0, tk.END)
            self.AGE_ENTRY.delete(0, tk.END)
            self.GENDER_ENTRY.delete(0, tk.END)
            self.DEPARTMENT_ENTRY.delete(0, tk.END)
            self.UNIFORM_ENTRY.delete(0, tk.END)
            self.INSTRUMENT_ENTRY.delete(0, tk.END)
            self.POSITION_ENTRY.delete(0, tk.END)
            self.ADDRESS_ENTRY.delete(0, tk.END)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}, Please fill correctly all the entry.")

        finally:
            if conn:
                conn.close()


    #DELETE FUNCTION TO DELETE MEMBER
    def delete_member(self, event):
        # Get the selected item
        selected_item = self.treeview.selection()

        if selected_item:
            # Fetch data from the selected item
            item_data = self.treeview.item(selected_item, "values")

            # Get MemberID
            member_id = item_data[0]

            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="POGIako2003",
                    database="band"
                )
                cursor = conn.cursor()

                # Delete the instrument information first
                cursor.execute("DELETE FROM instruments WHERE MemberID = %s", (member_id,))

                # Delete the member information
                cursor.execute("DELETE FROM members WHERE MemberID = %s", (member_id,))

                conn.commit()

                # Remove the selected item directly from the Treeview
                self.treeview.delete(selected_item)

                messagebox.showinfo("Success", "Member deleted successfully.")

                # Clear the entry widgets
                self.MEMBERNAME_ENTRY.delete(0, tk.END)
                self.AGE_ENTRY.delete(0, tk.END)
                self.GENDER_ENTRY.delete(0, tk.END)
                self.DEPARTMENT_ENTRY.delete(0, tk.END)
                self.UNIFORM_ENTRY.delete(0, tk.END)
                self.INSTRUMENT_ENTRY.delete(0, tk.END)
                self.POSITION_ENTRY.delete(0, tk.END)
                self.ADDRESS_ENTRY.delete(0, tk.END)

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"MySQL Error: {e}")

            finally:
                if conn:
                    conn.close()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.run()