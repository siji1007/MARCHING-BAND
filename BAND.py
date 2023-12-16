import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from tkinter import Tk, Button,Entry,Frame

class CustomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CNSC Marching Band")
        self.master.geometry("800x700")
        self.master.resizable(False, False)

        self.create_widgets_background()
        self.create_widgets_buttons()
        self.create_widgets_entry()
        self.create_widgets_frames()

    def create_widgets_background(self):
        original_image = Image.open("Dashboard.png")
        width, height = 800, 700
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_image)

        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

    def create_widgets_buttons(self):
        original_image = Image.open("FILTER.png")
        resized_image = original_image.resize((60, 20), Image.LANCZOS)
        self.search_image = ImageTk.PhotoImage(resized_image)

        self.search_button = Button(self.canvas, image=self.search_image, bd=0, height=20, width=60, compound='center')
        self.search_button.place(x=567, y=106)




    def create_widgets_entry(self):
        default_value = "Search"
        

        self.SEARCH_ENTRY = Entry(self.canvas, width=16, font=('Arial', 14),bd=0, bg="#993333",fg="white")
        self.SEARCH_ENTRY.place(x=385, y=106)

        # Set default value
        self.SEARCH_ENTRY.insert(0, default_value)
        self.SEARCH_ENTRY.bind("<FocusIn>", self.clear_default_value)



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
        self.POSITION_ENTRY.place(x=395, y=210)
        self.POSITION_ENTRY.insert(0, default_value_ENTRIES)
        self.POSITION_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #ADDRESS
        self.ADDRESS_ENTRY = Entry(self.canvas, width=27, font=('Arial', 10,),bd=0, bg="#212121",fg="white")
        self.ADDRESS_ENTRY.place(x=395, y=265)
        self.ADDRESS_ENTRY.insert(0, default_value_ENTRIES)
        self.ADDRESS_ENTRY.bind("<FocusIn>", self.clear_default_value)

        #



    #FRAMES HERE
    def create_widgets_frames(self):
        self.FORM_2 = tk.Frame(self.master, bg="#212121")
        self.FORM_2.place(x=380, y=300, width=270, height=60)

       



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

    


    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.run()
