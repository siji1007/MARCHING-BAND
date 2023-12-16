import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk

class CustomApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CNSC Marching Band")
        self.master.geometry("1200x650")
        self.master.resizable(False, False)

        self.create_widgets_background()

        # Create ttkbootstrap styled widgets
        self.create_widgets_buttons()

        self.create_widgets_entry()

    def create_widgets_background(self):
        # Load the background image
        original_image = Image.open("Dashboard.png")

        # Resize the image while maintaining the aspect ratio
        width, height = 1200, 650
        resized_image = original_image.resize((width, height), Image.LANCZOS)

        # Convert the Image object to PhotoImage
        self.bg_image = ImageTk.PhotoImage(resized_image)

        # Create a Canvas widget to place the background image
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)

        # Place the resized background image on the Canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

    def create_widgets_buttons(self):
        self.test_button = ttk.Button(self.canvas, text="hello", bootstyle="blue-outline")
        self.test_button.pack(pady=10)

    def create_widgets_entry(self):
        # Create the entry widget with a custom background color
        self.SEARCH_ENTRY = ttk.Entry(self.canvas, width=47, bootstyle="info")
        self.SEARCH_ENTRY.place(x=520, y=100)

        # Configure the background color
        self.SEARCH_ENTRY.configure(style="info.TEntry", background="maroon")

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.run()
