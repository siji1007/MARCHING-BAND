import tkinter as tk
from tkinter import ttk
import mysql.connector

def show_database_info():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  # Change to your MySQL username
            password="POGIako2003",  # Change to your MySQL password
            database="band"  # Change to your database name
        )
        cursor = conn.cursor()

        # Fetch data from the MySQL database
        cursor.execute("SELECT * FROM members")  # Change to your table name
        data = cursor.fetchall()

        # Insert data into the Treeview
        for row in data:
            tree.insert("", "end", values=row)

        # Display the connected database in the label
        db_info_label.config(text=f"Connected to: {conn.database}")

    except mysql.connector.Error as e:
        # Handle MySQL errors
        print(f"MySQL Error: {e}")

    finally:
        # Close the database connection in the 'finally' block to ensure it's closed
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Create the main window
root = tk.Tk()
root.title("MySQL Data in Treeview")

# Create a label to display the connected database
db_info_label = tk.Label(root, text="Not connected to any database")
db_info_label.pack(pady=10)

# Create a Treeview widget
tree = ttk.Treeview(root)
column_names = ["Column1", "Column2", "Column3"]
tree["columns"] = tuple(column_names)
tree.heading("#0", text="ID")
for col in column_names:
    tree.heading(col, text=col)

# Create a button to trigger showing the database info
show_info_button = tk.Button(root, text="Show Database Info", command=show_database_info)
show_info_button.pack(pady=10)

# Pack the Treeview widget
tree.pack(expand=True, fill=tk.BOTH)

# Run the Tkinter event loop
root.mainloop()
