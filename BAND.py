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

        self.SEARCH_ENTRY = Entry(self.canvas, width=22, font=('Arial', 11, "bold"), bg="#993333",fg="white")
        self.SEARCH_ENTRY.place(x=385, y=106)

        # Set default value
        self.SEARCH_ENTRY.insert(0, default_value)
        self.SEARCH_ENTRY.bind("<FocusIn>", self.clear_default_value)


    #FRAMES HERE
    def create_widgets_frames(self):
        self.FORM_1 = tk.Frame(self.master, bg="black")
        self.FORM_1.place(x=29, y=185, width=300, height=185)

        self.FORM_2 = tk.Frame(self.master, bg="black")
        self.FORM_2.place(x=358, y=185, width=300, height=185)

    def clear_default_value(self, event):
        # Clear default value when the entry is clicked
        if self.SEARCH_ENTRY.get() == "Search":
            self.SEARCH_ENTRY.delete(0, tk.END)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.run()
