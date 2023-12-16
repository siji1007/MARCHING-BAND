import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, Button,Entry,Frame,ttk, messagebox
import sqlite3

class CustomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CNSC Marching Band")
        self.master.geometry("800x700")
        self.master.resizable(False, False)

        self.create_widgets_background()
        self.create_widgets_buttons()
        self.create_widgets_entry()
        #self.create_widgets_frames()
        self.create_widgets_treeview()

    def create_widgets_background(self):
        original_image = Image.open("Dashboard.png")
        width, height = 800, 700
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

    def create_widgets_buttons(self):

        #SEARCH BUTTON
        SEARCH_image = Image.open("SEARCH.png")
        resized_image = SEARCH_image.resize((50, 25), Image.LANCZOS)
        self.SEARCH_image = ImageTk.PhotoImage(resized_image)
        self.SEARCH_button = Button(self.canvas, image=self.SEARCH_image, bd=0, height=25, width=50, compound='center', relief=tk.FLAT,highlightthickness=0, command=self.search_entry_by_id_and_name)
        self.SEARCH_button.place(x=517, y=105)


        #ADD BUTTON 
        ADD_IMAGE = Image.open("ADD_IMAGE.png")
        resized_ADD_image = ADD_IMAGE.resize((30, 25), Image.LANCZOS)
        self.ADD_IMAGE = ImageTk.PhotoImage(resized_ADD_image)
        self.ADD_button = Button(self.canvas, image=self.ADD_IMAGE, bd=0, height=25, width=30, compound='center', relief=tk.FLAT,highlightthickness=0,  command=self.add_entry_to_database)
        self.ADD_button.place(x=591, y=105)

        #UPDATE BUTTON
        UPDATE_IMAGE = Image.open("UPDATE.png")
        resized_UPDATE_image = UPDATE_IMAGE.resize((56, 25), Image.LANCZOS)
        self.UPDATE_IMAGE = ImageTk.PhotoImage(resized_UPDATE_image)
        self.UPDATE_button = Button(self.canvas, image=self.UPDATE_IMAGE, bd=0, height=25, width=56, compound='center', relief=tk.FLAT,highlightthickness=0,command=self.update_selected_entry)
        self.UPDATE_button.place(x=630, y=105)

        #DELETE BUTTON
        DELETE_IMAGE = Image.open("DELETE.png")
        resized_DELETE_image = DELETE_IMAGE.resize((56, 25), Image.LANCZOS)
        self.DELETE_IMAGE = ImageTk.PhotoImage(resized_DELETE_image)
        self.DELETE_button = Button(self.canvas, image=self.DELETE_IMAGE, bd=0, height=25, width=56, compound='center', relief=tk.FLAT,highlightthickness=0,command=self.delete_selected_entry)
        self.DELETE_button.place(x=693, y=105)


    def create_widgets_entry(self):
        default_value = "Search"
        

        self.SEARCH_ENTRY = Entry(self.canvas, width=16, font=('Arial', 14),bd=0, bg="#993333",fg="white")
        self.SEARCH_ENTRY.place(x=340, y=106)

        # Set default value
        self.SEARCH_ENTRY.insert(0, default_value)
        self.SEARCH_ENTRY.bind("<FocusIn>", self.clear_default_value)
        self.SEARCH_ENTRY.bind("<KeyRelease>", lambda event: self.search_entry_by_id_and_name())



        #MEMBER_NAME ENTRY 
        default_value_ENTRIES ="INPUT TEXT"
        self.MEMBERNAME_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.MEMBERNAME_ENTRY.place(x=60, y=210)
        self.MEMBERNAME_ENTRY.insert(0, default_value_ENTRIES)
        self.MEMBERNAME_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #AGE
        self.AGE_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.AGE_ENTRY.place(x=60, y=265)
        self.AGE_ENTRY.insert(0, default_value_ENTRIES)
        self.AGE_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #DEPARTMENT
        self.DEPARTMENT_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.DEPARTMENT_ENTRY.place(x=60, y=320)
        self.DEPARTMENT_ENTRY.insert(0, default_value_ENTRIES)
        self.DEPARTMENT_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #BAND POSITION
        self.POSITION_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.POSITION_ENTRY.place(x=433, y=210)
        self.POSITION_ENTRY.insert(0, default_value_ENTRIES)
        self.POSITION_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #ADDRESS
        self.ADDRESS_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.ADDRESS_ENTRY.place(x=433, y=265)
        self.ADDRESS_ENTRY.insert(0, default_value_ENTRIES)
        self.ADDRESS_ENTRY.bind("<FocusIn>", self.clear_default_value)


    def create_widgets_treeview(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("band_members.db")
        c = conn.cursor()

        # Create the 'members' table if it doesn't exist
        c.execute("""CREATE TABLE IF NOT EXISTS members (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    FirstName TEXT,
                    Age INTEGER,
                    Department TEXT,
                    Position TEXT,
                    Address TEXT
                    )""")
        conn.commit()

        # Fetch data from the database
        c.execute("SELECT * FROM members")
        rows = c.fetchall()

        conn.close()

        columns = ("ID", "NAME", "AGE", "DEPARTMENT", "POSITION", "ADDRESS")
        maroon_color = "#420303"

        # Create Style instance
        style = ttk.Style()
        style.configure(f"{maroon_color}.Treeview", background=maroon_color)

        self.treeview = ttk.Treeview(self.canvas, columns=columns, show="headings", height=9, style=f"{maroon_color}.Treeview")
        self.treeview.place(x=30, y=390)

        # Insert data from the database into the Treeview
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=121, anchor="center")

        for data in rows:
            self.treeview.insert("", tk.END, values=data, tags="white_text")

        # Define a tag with white text color
        self.treeview.tag_configure("white_text", foreground="white")

        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)



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
            self.DEPARTMENT_ENTRY.insert(0, item_data[3])  # Department
            self.POSITION_ENTRY.delete(0, tk.END)
            self.POSITION_ENTRY.insert(0, item_data[4])  # Position
            self.ADDRESS_ENTRY.delete(0, tk.END)
            self.ADDRESS_ENTRY.insert(0, item_data[5])  # Address



    def delete_selected_entry(self):
        # Get the selected item
        selected_item = self.treeview.selection()

        if selected_item:
            # Ask for confirmation before deleting
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected entry?")
            if confirm:
                # Fetch data from the selected item
                item_data = self.treeview.item(selected_item, "values")
                
                # Connect to the database
                conn = sqlite3.connect("band_members.db")
                c = conn.cursor()

                # Delete the selected entry from the 'members' table using the ID
                c.execute("DELETE FROM members WHERE ID = ?", (item_data[0],))

                # Commit changes and close the connection
                conn.commit()
                conn.close()

                self.MEMBERNAME_ENTRY.delete(0, tk.END)
                self.AGE_ENTRY.delete(0, tk.END)
                self.DEPARTMENT_ENTRY.delete(0, tk.END)
                self.POSITION_ENTRY.delete(0, tk.END)
                self.ADDRESS_ENTRY.delete(0, tk.END)

                # Update Treeview with the new data
                self.create_widgets_treeview()


    def clear_default_value(self, event):
        # Clear default value when the entry is clicked
        if self.SEARCH_ENTRY.get() == "Search":
            self.SEARCH_ENTRY.delete(0, tk.END)
        if self.MEMBERNAME_ENTRY.get() and self.AGE_ENTRY.get() and self.DEPARTMENT_ENTRY.get() and self.POSITION_ENTRY.get() and self.ADDRESS_ENTRY.get() == "INPUT TEXT":
            self.MEMBERNAME_ENTRY.delete(0,tk.END)
            self.AGE_ENTRY.delete(0,tk.END)
            self.DEPARTMENT_ENTRY.delete(0,tk.END)
            self.POSITION_ENTRY.delete(0,tk.END)
            self.ADDRESS_ENTRY.delete(0,tk.END)

    
    def add_entry_to_database(self):
 # Get entry values
        member_name = self.MEMBERNAME_ENTRY.get()
        age = self.AGE_ENTRY.get()
        department = self.DEPARTMENT_ENTRY.get()
        position = self.POSITION_ENTRY.get()
        address = self.ADDRESS_ENTRY.get()

        # Check if any of the required fields is empty
        if not (member_name and age and department and position and address):
            messagebox.showwarning("Incomplete Entry", "Please fill in all the required fields.")
            return

        # Connect to the database
        conn = sqlite3.connect("band_members.db")
        c = conn.cursor()

        # Insert data into the 'members' table
        c.execute("INSERT INTO members (FirstName, Age, Department, Position, Address) VALUES (?, ?, ?, ?, ?)",
                  (member_name, age, department, position, address))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Clear entry values
        self.MEMBERNAME_ENTRY.delete(0, tk.END)
        self.AGE_ENTRY.delete(0, tk.END)
        self.DEPARTMENT_ENTRY.delete(0, tk.END)
        self.POSITION_ENTRY.delete(0, tk.END)
        self.ADDRESS_ENTRY.delete(0, tk.END)

        # Update Treeview with the new data
        self.create_widgets_treeview()



    def update_selected_entry(self):
            # Get the selected item
            selected_item = self.treeview.selection()

            if selected_item:
                # Fetch data from the selected item
                item_data = self.treeview.item(selected_item, "values")

                # Get updated values from the entry widgets
                updated_name = self.MEMBERNAME_ENTRY.get()
                updated_age = self.AGE_ENTRY.get()
                updated_department = self.DEPARTMENT_ENTRY.get()
                updated_position = self.POSITION_ENTRY.get()
                updated_address = self.ADDRESS_ENTRY.get()

                # Connect to the database
                conn = sqlite3.connect("band_members.db")
                c = conn.cursor()

                # Update the selected entry in the 'members' table using the ID
                c.execute("""
                    UPDATE members 
                    SET FirstName = ?, Age = ?, Department = ?, Position = ?, Address = ?
                    WHERE ID = ?
                """, (updated_name, updated_age, updated_department, updated_position, updated_address, item_data[0]))

                # Commit changes and close the connection
                conn.commit()
                conn.close()

                # Clear entry values
                self.MEMBERNAME_ENTRY.delete(0, tk.END)
                self.AGE_ENTRY.delete(0, tk.END)
                self.DEPARTMENT_ENTRY.delete(0, tk.END)
                self.POSITION_ENTRY.delete(0, tk.END)
                self.ADDRESS_ENTRY.delete(0, tk.END)

                # Update Treeview with the new data
                self.create_widgets_treeview()


    def search_entry_by_id_and_name(self):
            # Get the search term from the entry widget
            search_term = self.SEARCH_ENTRY.get().strip()

            # Connect to the database
            conn = sqlite3.connect("band_members.db")
            c = conn.cursor()

            # Search for entries by ID or Name
            c.execute("SELECT * FROM members WHERE ID = ? OR FirstName LIKE ?", (search_term, f'%{search_term}%'))
            rows = c.fetchall()

            conn.close()

            # Clear the Treeview
            for item in self.treeview.get_children():
                self.treeview.delete(item)

            # Insert data into the Treeview
            for data in rows:
                self.treeview.insert("", tk.END, values=data, tags="white_text")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.run()
